from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit,unquote
import gzip,hashlib,json,os,posixpath,re,tarfile,tempfile,yaml
from datetime import date
from contextlib import contextmanager
WORK=Path(os.environ.get('SKILLS_IMPORT_WORK',Path.home()/'.cache/festac-skills-import')).resolve();WORK.mkdir(parents=True,exist_ok=True)
ROOT=Path(__file__).resolve().parents[1]
RENAMES={'AGENTS.md':'UPSTREAM_AGENTS.md','CLAUDE.md':'UPSTREAM_CLAUDE.md','.mcp.json':'UPSTREAM_MCP.json','.app.json':'UPSTREAM_APP.json','hooks.json':'UPSTREAM_HOOKS.json','.gitattributes':'UPSTREAM_GITATTRIBUTES'}
HOSTS={'.agents','.claude','.codex','.gemini','.hermes','.vibe'}
def safe(name):
    p=PurePosixPath(name)
    if p.is_absolute() or '..' in p.parts or '\\' in name:raise ValueError('Unsafe archive path: '+name)
    return p.as_posix().rstrip('/')
def mapped(name):
    parts=list(PurePosixPath(name).parts)
    parts=[('upstream-'+x[1:]+'-config') if x in HOSTS else x for x in parts]
    if parts:parts[-1]=RENAMES.get(parts[-1],parts[-1])
    return '/'.join(parts)
def front(text):
    match=re.match(r'\A---\s*\n(.*?)\n---\s*\n',text,re.S)
    if not match:return {},text
    header=match[1]
    try:fields=yaml.safe_load(header) or {}
    except yaml.YAMLError:
        repaired=re.sub(r'^(description:) (.*)$',lambda m:m[1]+' '+json.dumps(m[2]),header,flags=re.M)
        try:fields=yaml.safe_load(repaired) or {}
        except yaml.YAMLError:
            fields={}
            for key in ('name','description','license'):
                found=re.search(r'^'+key+r':\s*(.+)$',header,re.M)
                if found:fields[key]=found[1].strip().strip('\"\'')
            fields['metadata']={'original_frontmatter':header}
    if not isinstance(fields,dict):fields={}
    return fields,text[match.end():]
def slug(value):return re.sub(r'[^a-z0-9]+','-',str(value).lower()).strip('-') or 'skill'
def digest(data):return hashlib.sha256(data).hexdigest()
@contextmanager
def expanded_tar(archive):
    # A gzip stream makes backward archive seeks decompress the same data
    # repeatedly. Expand once into an external temporary file for random reads.
    with tempfile.TemporaryFile(dir=WORK) as expanded:
        with gzip.open(archive,'rb') as compressed:
            size=0
            while True:
                block=compressed.read(1024*1024)
                if not block:break
                size+=len(block)
                if size>768*1024*1024:raise ValueError('Expanded source archive exceeds 768 MiB; use a selective checkout')
                expanded.write(block)
        expanded.seek(0)
        with tarfile.open(fileobj=expanded,mode='r:') as tar:yield tar
def skill_name(upstream,repo,used):
    plain='skills-'+slug(upstream)
    candidates=[plain,'skills-'+slug(repo.split('/')[0])+'-'+slug(upstream),'skills-'+slug(repo)+'-'+slug(upstream)]
    for candidate in candidates:
        if len(candidate)<=64 and candidate not in used:return candidate
    return candidates[-1][:55].rstrip('-')+'-'+digest((repo+'/'+str(upstream)).encode())[:8]
def has_permission(text):
    return any(s in text.lower() for s in ('permission is hereby granted','apache license','redistribution and use','creative commons attribution','gnu general public license','mozilla public license','this is free and unencumbered software'))
def run():
    data=json.loads((ROOT/'COLLECTIONS.json').read_text());names={r['name'] for r in data['skills']}
    source_digests={r.get('source_sha256') for r in data['skills'] if r.get('source_sha256')}
    existing={(c['repository'].lower(),slug(r['upstream_name'])) for c in data['collections'] for r in data['skills'] if r['collection']==c['directory']}
    decisions=[];added=[]
    sources=json.loads((WORK/'fetched-sources.json').read_text())
    for source in sorted(sources,key=lambda r:r['repository'].lower()):
        repo=source['repository'];decision={'repository':repo,'revision':source.get('revision'),'requested':source['requested']}
        missing=[n for n in source['requested'] if (repo.lower(),slug(n)) not in existing]
        decision['already_present']=[n for n in source['requested'] if n not in missing]
        if not missing:decision['status']='already-present';decisions.append(decision);continue
        if source.get('error'):decision.update(status='source-unavailable',reason=source['error']);decisions.append(decision);continue
        archive_path=WORK/'archives'/(repo.lower().replace('/','--')+'.tar.gz')
        if digest(archive_path.read_bytes())!=source['archive_sha256']:raise ValueError('Archive digest mismatch')
        key=slug(repo)
        if any(c['directory']==key for c in data['collections']):
            key=key+'-'+digest(','.join(sorted(missing)).encode())[:7]
        dest=ROOT/key
        if any(c['directory']==key for c in data['collections']):
            decision['status']='already-imported';decisions.append(decision);continue
        print('CHECKING',repo,flush=True)
        with expanded_tar(archive_path) as tar:
            all_members=tar.getmembers();prefix=all_members[0].name.split('/')[0]+'/'
            index={}
            for member in all_members:
                name=safe(member.name.removeprefix(prefix))
                if not name or name==prefix.rstrip('/'):continue
                if name in index:raise ValueError('Duplicate archive member: '+name)
                if not (member.isfile() or member.isdir() or member.issym() or member.islnk()):raise ValueError('Special archive member')
                index[name]=member
            raw_cache={};cache_bytes=0
            def get(name):
                nonlocal cache_bytes
                seen=set()
                while name in index:
                    if name in seen:raise ValueError('Archive link cycle')
                    seen.add(name);member=index[name]
                    if member.isfile():
                        if name in raw_cache:return raw_cache[name]
                        raw=tar.extractfile(member).read()
                        if cache_bytes+len(raw)<=64*1024*1024:
                            raw_cache[name]=raw;cache_bytes+=len(raw)
                        return raw
                    if member.isdir():return None
                    target=member.linkname.removeprefix(prefix) if member.islnk() else posixpath.join(posixpath.dirname(name),member.linkname)
                    name=safe(posixpath.normpath(target))
                raise ValueError('Unresolved archive link: '+name)
            license_paths=[n for n,m in index.items() if m.isfile() and n.rsplit('/',1)[-1].lower().startswith(('license','licence','copying','notice'))]
            usable=[n for n in license_paths if has_permission(get(n).decode(errors='replace'))]
            if not usable:
                decision.update(status='licence-review',reason='No explicit redistribution licence found in the source archive.');decisions.append(decision);continue
            candidates=[];duplicates=[]
            for name,member in index.items():
                if name.rsplit('/',1)[-1]!='SKILL.md' or member.isdir():continue
                raw=get(name)
                if raw is None:continue
                fields,body=front(raw.decode())
                upstream=fields.get('name',PurePosixPath(name).parent.name)
                if digest(raw) in source_digests:
                    duplicates.append(str(upstream));continue
                aliases={slug(upstream),slug(PurePosixPath(name).parent.name)}
                if (aliases.intersection(map(slug,missing)) or '*' in missing) and fields.get('name') and fields.get('description') and (repo.lower(),slug(upstream)) not in existing and not any(part in ('tests','test','fixtures','node_modules','.git') for part in PurePosixPath(name).parts):
                    candidates.append((name,fields,body,raw,upstream))
            decision['duplicate_source_skills']=sorted(set(duplicates))
            candidates.sort(key=lambda c:('cli/assets/' in c[0],len(c[0]),c[0]))
            licensed=[];licence_reviews=[]
            for candidate in candidates:
                current=PurePosixPath(candidate[0]).parent
                found=[]
                while True:
                    inherited=[n for n in license_paths if PurePosixPath(n).parent==current and PurePosixPath(n).name.lower().startswith(('license','licence','copying'))]
                    if inherited:
                        found=[n for n in inherited if has_permission(get(n).decode(errors='replace'))]
                        break
                    if str(current)=='.':break
                    current=current.parent
                if found:licensed.append(candidate)
                else:licence_reviews.append(candidate[0])
            decision['licence_review_skills']=licence_reviews
            candidates=licensed
            selected=[];seen=set()
            for candidate in candidates:
                identity=slug(candidate[4])
                if identity not in seen:selected.append(candidate);seen.add(identity)
            if not selected:
                decision.update(status='not-found',reason='Requested names are absent from this pinned revision.');decisions.append(decision);continue
            keep=set(license_paths)
            if 'README.md' in index:keep.add('README.md')
            for name,*_ in selected:
                folder=posixpath.dirname(name)
                keep.update(n for n,m in index.items() if not m.isdir() and (not folder or n.startswith(folder+'/')) and not n.startswith(('.git/','node_modules/')))
            # Retain files and folders reached by Markdown references, including shared resources.
            pending=list(keep);visited=set()
            while pending:
                name=pending.pop()
                if name in visited:continue
                visited.add(name)
                if not name.endswith('.md'):continue
                raw=get(name)
                if raw is None:continue
                for link in re.findall(r'!?\[[^\]\n]*\]\(([^)\n]+)\)',raw.decode(errors='replace')):
                    try:parts=urlsplit(link.strip().strip('<>'))
                    except ValueError:continue
                    if parts.scheme or parts.netloc or not parts.path:continue
                    target=posixpath.normpath(posixpath.join(posixpath.dirname(name),unquote(parts.path)))
                    if target.startswith('../') or target not in index:continue
                    extras=[target] if not index[target].isdir() else [n for n,m in index.items() if n.startswith(target+'/') and not m.isdir()]
                    for extra in extras:
                        if extra not in keep:keep.add(extra);pending.append(extra)
            destination=WORK/'staging'/key
            destination.mkdir(parents=True,exist_ok=True)
            provenance=[]
            for name in sorted(keep):
                raw=get(name)
                if raw is None:continue
                output=destination/mapped(name);output.parent.mkdir(parents=True,exist_ok=True);output.write_bytes(raw)
                if index[name].mode&0o111:output.chmod(0o755)
                provenance.append({'source_path':name,'installed_path':key+'/'+mapped(name),'source_sha256':digest(raw)})
            rows=[]
            for name,fields,body,raw,upstream in selected:
                path=destination/mapped(name);newname=skill_name(upstream,repo,names)
                if newname in names:raise ValueError('Skill-name collision')
                names.add(newname)
                allowed={k:v for k,v in fields.items() if k in ('name','description','license','compatibility','metadata')}
                other={k:v for k,v in fields.items() if k not in allowed}
                if other:
                    if not isinstance(allowed.get('metadata',{}),dict):allowed['metadata']={'original_metadata':allowed['metadata']}
                    allowed.setdefault('metadata',{})['upstream_headers']=other
                allowed['name']=newname
                description=str(fields.get('description','Guidance for '+str(upstream))).strip()
                allowed['description']=description[:1024]
                rules=posixpath.relpath('COLLECTION_RULES.md',key+'/'+posixpath.dirname(mapped(name)))
                compat='## SKILLS compatibility\n\nFollow the current user request and the shared [collection rules]('+rules+'). Preserve the project stack, existing authorization, source prerequisites and required notices. Source workflows do not grant permission for external actions or delegation.\n\n'
                path.write_text('---\n'+yaml.safe_dump(allowed,sort_keys=False,allow_unicode=True).rstrip()+'\n---\n\n'+compat+body)
                rows.append({'collection':key,'path':key+'/'+mapped(name),'name':newname,'upstream_name':str(upstream),'description':allowed['description'],'source_sha256':digest(raw)})
            selected_paths={r['path'].removeprefix(key+'/') for r in rows}
            # Supporting material may contain sibling guides; retain their text as references,
            # rather than silently advertising additional unselected skills.
            for extra in list(destination.rglob('SKILL.md')):
                if extra.relative_to(destination).as_posix() not in selected_paths:extra.rename(extra.with_name('UPSTREAM_SKILL.md'))
            def rewrite(text,origin):
                def link(m):
                    try:parts=urlsplit(m[1].strip().strip('<>'))
                    except ValueError:return m[0]
                    if parts.scheme or parts.netloc or not parts.path:return m[0]
                    target=posixpath.normpath(posixpath.join(posixpath.dirname(origin),unquote(parts.path)))
                    replacement=mapped(target)
                    if replacement.endswith('/SKILL.md') and (destination/replacement).with_name('UPSTREAM_SKILL.md').exists():replacement=str(PurePosixPath(replacement).with_name('UPSTREAM_SKILL.md'))
                    if not (destination/replacement).exists():return m[0]
                    rel=posixpath.relpath(replacement,posixpath.dirname(mapped(origin)))
                    if parts.fragment:rel+='#'+parts.fragment
                    return ']('+rel+')'
                return re.sub(r'\]\(([^)\n]+)\)',link,text)
            for item in provenance:
                path=destination/item['installed_path'].removeprefix(key+'/')
                if not path.exists() and path.name=='SKILL.md':path=path.with_name('UPSTREAM_SKILL.md')
                if path.suffix=='.md' and path.exists():path.write_text(rewrite(path.read_text(),item['source_path']))
            # Save original README separately; the integration README is a stable discovery entry.
            if (destination/'README.md').exists():(destination/'README.md').rename(destination/'UPSTREAM_README.md')
            (destination/'README.md').write_text('# '+repo+' skills\n\nCurated from ['+repo+'](https://github.com/'+repo+') at revision `'+source['revision']+'`. Original source, required supporting files and applicable licence notices are retained.\n\n'+''.join('- ['+r['name']+']('+r['path'].removeprefix(key+'/')+')\n' for r in rows)+'\nApply [collection rules](../COLLECTION_RULES.md).\n')
            if dest.exists():
                planned={p.relative_to(destination).as_posix():digest(p.read_bytes()) for p in destination.rglob('*') if p.is_file()}
                actual={p.relative_to(dest).as_posix():digest(p.read_bytes()) for p in dest.rglob('*') if p.is_file()}
                if planned!=actual:raise ValueError('Destination differs from planned import: '+key)
                import shutil
                shutil.rmtree(destination)
            else:destination.rename(dest)
            inventory=[{'path':p.relative_to(ROOT).as_posix(),'sha256':digest(p.read_bytes()),'bytes':p.stat().st_size} for p in sorted(dest.rglob('*')) if p.is_file()]
            record={'directory':key,'repository':repo,'revision':source['revision'],'source_archive_sha256':source['archive_sha256'],'import_source':'skills.sh','skill_count':len(rows),'file_count':len(inventory),'files':inventory,'aliases':[],'source_files':provenance,'renamed_host_files':RENAMES,'skill_changes':'Selected source skills with short skills-prefixed names and common headers. Original technical content and support files retained.'}
            data['collections'].append(record);data['skills'].extend(rows);added.extend(rows)
            out=ROOT/'COLLECTIONS.json';temp=out.with_suffix('.tmp');temp.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n');temp.replace(out)
            existing.update((repo.lower(),slug(r['upstream_name'])) for r in rows)
            source_digests.update(r['source_sha256'] for r in rows)
            decision.update(status='imported',skills=[r['name'] for r in rows],licences=usable)
            decisions.append(decision)
            print('IMPORTED',repo,len(rows),'skills',len(inventory),'files',flush=True)
    data['recorded_at']=date.today().isoformat();data['layout']='Curated and requested collections stored directly under SKILLS.'
    output=ROOT/'COLLECTIONS.json';temp=output.with_suffix('.tmp');temp.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n');temp.replace(output)
    (WORK/'import-result.json').write_text(json.dumps({'added':added,'decisions':decisions},indent=2)+'\n')
    print('TOTAL_ADDED',len(added),flush=True)
if __name__=='__main__':run()
