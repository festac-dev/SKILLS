#!/usr/bin/env python3
"""Inspect explicit cache paths; apply a reviewed, unchanged plan within one root."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import stat
import subprocess
import sys

PROTECTED = {'.git', '.local', 'data', 'storage', 'uploads', 'secrets',
             'out', 'assets', '.venv', 'venv'}
DEPENDENCY_CACHES = {'.cache', '.vite', '.vite-temp'}


def scoped_path(root, name):
    rel = Path(name)
    if rel.is_absolute() or not rel.parts or '..' in rel.parts:
        raise ValueError(f'Expected a nonempty relative path: {name}')
    if any(part in PROTECTED for part in rel.parts):
        raise ValueError(f'Protected state or deliverable: {name}')
    if 'node_modules' in rel.parts:
        i = rel.parts.index('node_modules')
        if i + 1 == len(rel.parts) or rel.parts[i + 1] not in DEPENDENCY_CACHES:
            raise ValueError(f'Installed dependency, not a cache: {name}')
    path = root
    for part in rel.parts:
        path = path / part
        if path.is_symlink():
            raise ValueError(f'Symlink in target path: {name}')
    if path == root or not path.is_relative_to(root):
        raise ValueError(f'Target escapes root: {name}')
    if not path.exists():
        raise ValueError(f'Target is missing: {name}')
    return path


def tracked_files(path):
    """Use literal pathspecs so brackets and glob characters cannot hide files."""
    result = subprocess.run(['git', '-C', str(path.parent), 'rev-parse',
                             '--show-toplevel'], capture_output=True, text=True)
    if result.returncode:
        if 'not a git repository' in result.stderr.lower():
            return []
        raise ValueError(f'Cannot establish Git ownership of {path.name}')
    repo = Path(result.stdout.strip()).resolve()
    relative = path.relative_to(repo).as_posix()
    result = subprocess.run(['git', '--literal-pathspecs', '-C', str(repo),
                             'ls-files', '-z', '--', relative], capture_output=True)
    if result.returncode:
        raise ValueError(f'Cannot inspect tracked files under {relative}')
    return [p for p in result.stdout.split(b'\0') if p]


def busy_pids(target):
    """Best-effort Linux check; runtime ownership still requires human/agent review."""
    proc = Path('/proc')
    if not proc.is_dir():
        return []
    found = set()
    for process in proc.iterdir():
        if not process.name.isdigit() or int(process.name) == os.getpid():
            continue
        try:
            cwd = (process / 'cwd').resolve(strict=True)
            paths = [cwd]
            # Inspect paths only. Never print commands or read process environments.
            for token in (process / 'cmdline').read_bytes().split(b'\0'):
                value = os.fsdecode(token).split('=', 1)[-1]
                if value and '\n' not in value and len(value) < 4096:
                    p = Path(value)
                    paths.append((p if p.is_absolute() else cwd / p).resolve())
            for fd in (process / 'fd').iterdir():
                try:
                    value = os.readlink(fd)
                    if value.startswith('/'):
                        paths.append(Path(value.removesuffix(' (deleted)')).resolve())
                except OSError:
                    pass
            if any(p == target or p.is_relative_to(target) for p in paths):
                found.add(int(process.name))
        except (OSError, ValueError):
            continue
    return sorted(found)


def inspect(root, name):
    target = scoped_path(root, name)
    if tracked_files(target):
        raise ValueError(f'Tracked content must be handled explicitly: {name}')
    pids = busy_pids(target)
    if pids:
        raise ValueError(f'Target is used by process IDs {pids}: {name}')
    digest = hashlib.sha256()
    count = total = 0
    stack = [target]
    while stack:
        path = stack.pop()
        info = path.lstat()
        relative = path.relative_to(target).as_posix()
        if (path.name in {'.git', 'PG_VERSION', 'postmaster.pid'}
                or path.name == '.env' or path.name.startswith('.env.')
                or path.name.endswith(('.db', '.sqlite', '.sqlite3', '-wal', '-shm'))):
            raise ValueError(f'Runtime, credential or repository marker inside {name}: {relative}')
        row = [relative, info.st_mode, info.st_size, info.st_mtime_ns,
               info.st_ino, info.st_dev, info.st_nlink]
        if stat.S_ISLNK(info.st_mode):
            row.append(os.readlink(path))
        elif stat.S_ISDIR(info.st_mode):
            stack.extend(sorted(path.iterdir(), reverse=True))
        elif stat.S_ISREG(info.st_mode):
            count += 1
            total += info.st_size
        else:
            raise ValueError(f'Special file inside {name}: {relative}')
        digest.update(json.dumps(row, ensure_ascii=True).encode())
    return {'path': target.relative_to(root).as_posix(), 'files': count,
            'bytes': total, 'fingerprint': digest.hexdigest()}


def make_plan(root, names):
    root = Path(root).resolve(strict=True)
    if not root.is_dir() or root == Path(root.anchor):
        raise ValueError('Choose a specific workspace directory')
    paths = [scoped_path(root, name) for name in names]
    if not paths:
        raise ValueError('Provide explicit paths after inspecting their purpose')
    for i, path in enumerate(paths):
        if any(path == other or path.is_relative_to(other) or other.is_relative_to(path)
               for other in paths[:i]):
            raise ValueError('Duplicate or overlapping cleanup targets')
    return {'schema_version': 1, 'root': str(root),
            'entries': [inspect(root, str(path.relative_to(root))) for path in paths]}


def apply_plan(root, plan):
    root = Path(root).resolve(strict=True)
    if plan.get('schema_version') != 1 or not isinstance(plan.get('root'), str):
        raise ValueError('Plan schema/root mismatch')
    planned_root = Path(plan['root']).resolve(strict=True)
    if not root.samefile(planned_root):
        raise ValueError('Plan schema/root mismatch')
    # Bind-mounted/PRoot aliases can name the same directory differently.
    root = planned_root
    fresh = make_plan(root, [entry['path'] for entry in plan['entries']])
    if fresh != plan:
        raise ValueError('Cleanup targets changed; inspect a fresh plan')
    removed = []
    for entry in plan['entries']:
        # Recheck just before deletion in case an earlier deletion took time.
        if inspect(root, entry['path']) != entry:
            raise ValueError(f'Target changed during cleanup: {entry["path"]}')
        path = scoped_path(root, entry['path'])
        if path.is_dir():
            if not shutil.rmtree.avoids_symlink_attacks:
                raise ValueError('This platform lacks fd-safe directory deletion')
            shutil.rmtree(path)
        else:
            path.unlink()
        removed.append(entry)
        print(json.dumps({'removed': entry['path'], 'logical_bytes': entry['bytes']}), flush=True)
    return removed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--path', action='append', default=[])
    parser.add_argument('--apply-plan', type=Path)
    args = parser.parse_args()
    try:
        if args.apply_plan:
            if args.path:
                parser.error('--path and --apply-plan are mutually exclusive')
            apply_plan(args.root, json.loads(args.apply_plan.read_text()))
        else:
            print(json.dumps(make_plan(args.root, args.path), indent=2))
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f'Cleanup refused: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
