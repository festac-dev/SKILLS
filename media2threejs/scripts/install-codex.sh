#!/usr/bin/env bash
set -euo pipefail
force=0
if [[ "${1:-}" == "--force" ]]; then force=1; elif [[ $# -gt 0 ]]; then echo "usage: $0 [--force]" >&2; exit 2; fi
repo_dir="$(cd "$(dirname "$0")/.." && pwd -P)"
skills_dir="${HOME}/.agents/skills"
target="${skills_dir}/media2threejs"
mkdir -p "$skills_dir"
if [[ -e "$target" || -L "$target" ]]; then
  if [[ $force -ne 1 ]]; then echo "Refusing to replace existing $target (use --force)." >&2; exit 1; fi
  if [[ ! -L "$target" ]]; then echo "Refusing to replace non-symlink $target." >&2; exit 1; fi
  unlink "$target"
fi
ln -s "$repo_dir" "$target"
echo "Installed media2threejs -> $repo_dir"
echo "Verify: test -f '$target/SKILL.md' && sed -n '1,8p' '$target/SKILL.md'"
