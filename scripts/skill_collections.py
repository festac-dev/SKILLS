#!/usr/bin/env python3
"""Find and validate the nine skill collections stored directly under SKILLS."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path, PurePosixPath
import re

ROOT = Path(__file__).resolve().parents[1]
COLLECTIONS = {'openai-plugins','anthropic-skills','vercel-agent-skills','jeffallan-skills',
               'alireza-skills','superpowers','awesome-copilot','scientific-agent-skills','awesome-claude-skills'}
COMPATIBILITY = '## SKILLS compatibility'


def registry(root=ROOT):
    data = json.loads((root/'COLLECTIONS.json').read_text())
    if data.get('schema_version')!=1 or {r['directory'] for r in data['collections']}!=COLLECTIONS:
        raise ValueError('Expected the nine requested direct skill collections')
    return data


def search(query, root=ROOT, limit=12):
    words=set(re.findall(r'[\w-]+',query.casefold()))
    results=[]
    for row in registry(root)['skills']:
        title=set(re.findall(r'[\w-]+',(row['name']+' '+row['path'].replace('-',' ')).casefold()))
        body=set(re.findall(r'[\w-]+',row['description'].casefold()))
        score=6*len(words&title)+len(words&body)
        if score:results.append({'resource':row['path'],'name':row['name'],'description':row['description'],
                                 'collection':row['collection'],'score':score})
    return sorted(results,key=lambda r:(-r['score'],r['resource']))[:limit]


def validate(root=ROOT, deep=True):
    errors=[]
    try:
        data=registry(root)
        if len(data['collections'])!=9:
            raise ValueError('Duplicate collection records')
        names=set()
        expected=set()
        for row in data['skills']:
            rel=PurePosixPath(row['path'])
            if rel.parts[0] not in COLLECTIONS or '..' in rel.parts or rel.is_absolute():
                raise ValueError('Skill is not directly within its collection')
            if row['name'] in names or not re.fullmatch(r'[a-z0-9-]{1,64}',row['name']):
                raise ValueError('Invalid or colliding skill name: '+row['name'])
            if not isinstance(row['description'],str) or not row['description'].strip() or len(row['description'])>1024:
                raise ValueError('Skill description exceeds the common format limit')
            names.add(row['name']);expected.add(row['path'])
            path=root/row['path']
            text=path.read_text()
            match=re.search(r'^name:\s*([^\n]+)',text,re.M)
            if not text.startswith('---\n') or not match or match[1].strip()!=row['name'] or COMPATIBILITY not in text:
                raise ValueError('Missing namespace or compatibility guidance: '+row['path'])
            header_keys=set(re.findall(r'^([a-z][a-z0-9_-]*):',text.split('---',2)[1],re.M))
            if header_keys-{'name','description','license','compatibility','metadata'}:
                raise ValueError('Active upstream execution headers: '+row['path'])
            if row['collection']!=rel.parts[0]:raise ValueError('Mismatched collection identity')
        actual=set()
        for collection in data['collections']:
            directory=root/collection['directory']
            if not directory.is_dir() or not re.fullmatch(r'[a-f0-9]{40}',collection['revision']):
                raise ValueError('Missing collection or source revision')
            for host_dir in ['.claude','.codex','.gemini','.hermes','.vibe']:
                if (directory / host_dir).exists():
                    raise ValueError('Active upstream host directory: '+collection['directory'])
            inventory={r['path']:r for r in collection['files']}
            present=set()
            for p in directory.rglob('*'):
                if '__pycache__' in p.parts or '.pytest_cache' in p.parts:continue
                rel=p.relative_to(root).as_posix()
                if p.is_symlink():raise ValueError('Unresolved import symlink: '+rel)
                if not p.is_file():continue
                present.add(rel)
                if p.name=='SKILL.md':actual.add(rel)
                if p.name in {'AGENTS.md','CLAUDE.md','.mcp.json','.app.json','hooks.json'}:
                    raise ValueError('Active upstream host instructions/configuration: '+rel)
                if rel not in inventory:raise ValueError('Unindexed collection file: '+rel)
                if deep and hashlib.sha256(p.read_bytes()).hexdigest()!=inventory[rel]['sha256']:
                    raise ValueError('Changed collection file: '+rel)
            if present!=set(inventory):raise ValueError('Incomplete supporting-file inventory: '+collection['directory'])
            if collection['skill_count']!=sum(p.startswith(collection['directory']+'/') for p in expected):
                raise ValueError('Incorrect collection skill count')
        if actual!=expected:raise ValueError('Incomplete skill inventory')
    except (OSError,ValueError,KeyError,TypeError) as exc:errors.append(str(exc))
    return errors


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=['list','search','validate'])
    parser.add_argument('query',nargs='?')
    parser.add_argument('--root',type=Path,default=ROOT)
    args=parser.parse_args()
    try:
        if args.command=='search':
            if not args.query:parser.error('search requires a topic')
            print(json.dumps(search(args.query,args.root),indent=2))
        elif args.command=='list':
            data=registry(args.root)
            print(json.dumps([{k:v for k,v in r.items() if k!='files'} for r in data['collections']],indent=2))
        else:
            errors=validate(args.root)
            if errors:raise ValueError('; '.join(errors))
            data=registry(args.root)
            print(f"PASS: 9 direct collections; {len(data['skills'])} uniquely named skills; supporting files, compatibility and source digests")
        return 0
    except (OSError,ValueError,KeyError,TypeError) as exc:
        print('ERROR: '+str(exc));return 1


if __name__=='__main__':raise SystemExit(main())
