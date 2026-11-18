from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
from urllib.request import Request,urlopen
import hashlib,json,os,subprocess,tarfile,time
WORK=Path(os.environ.get('SKILLS_IMPORT_WORK',Path.home()/'.cache/festac-skills-import')).resolve();WORK.mkdir(parents=True,exist_ok=True)
ARCHIVES=WORK/'archives';ARCHIVES.mkdir(exist_ok=True)
SOURCES=json.loads((WORK/'curation.json').read_text())['sources']
def fetch(repo):
    key=repo.lower().replace('/','--');meta=ARCHIVES/(key+'.json');archive=ARCHIVES/(key+'.tar.gz')
    if meta.exists() and archive.exists():return json.loads(meta.read_text())
    result={'repository':repo,'requested':SOURCES[repo]}
    try:
        env=dict(os.environ,GIT_TERMINAL_PROMPT='0')
        r=subprocess.run(['git','ls-remote','https://github.com/'+repo+'.git','HEAD'],capture_output=True,text=True,timeout=40,env=env)
        if r.returncode or not r.stdout:raise RuntimeError('Source HEAD unavailable: '+r.stderr[:200])
        sha=r.stdout.split()[0];result['revision']=sha
        url='https://codeload.github.com/'+repo+'/tar.gz/'+sha
        with urlopen(Request(url,headers={'User-Agent':'SKILLS-Curated-Import/1.0'}),timeout=60) as response, archive.open('wb') as output:
            size=0
            while True:
                block=response.read(128*1024)
                if not block:break
                size+=len(block)
                if size>100*1024*1024:raise RuntimeError('Archive exceeds 100 MiB; needs selective checkout')
                output.write(block)
        result['archive_sha256']=hashlib.sha256(archive.read_bytes()).hexdigest();result['archive_bytes']=archive.stat().st_size
        with tarfile.open(archive) as tar:
            members=tar.getmembers();prefix=members[0].name.split('/')[0]+'/'
            result['skills']=[m.name.removeprefix(prefix) for m in members if m.isfile() and m.name.endswith('/SKILL.md')]
            result['licences']=[m.name.removeprefix(prefix) for m in members if m.isfile() and m.name.rsplit('/',1)[-1].lower().startswith(('license','licence','copying','notice'))]
            result['licence_samples']={m.name.removeprefix(prefix):tar.extractfile(m).read(350).decode(errors='replace') for m in members if m.isfile() and m.name.removeprefix(prefix).lower() in ('license','license.md','license.txt','copying')}
    except Exception as exc:
        result['error']=str(exc)
        archive.unlink(missing_ok=True)
    meta.write_text(json.dumps(result,indent=2)+'\n')
    return result
results=[]
with ThreadPoolExecutor(max_workers=3) as pool:
    for job in as_completed({pool.submit(fetch,repo):repo for repo in SOURCES}):
        row=job.result();results.append(row)
        print(json.dumps({k:v for k,v in row.items() if k not in ('skills','licences')}),flush=True)
(WORK/'fetched-sources.json').write_text(json.dumps(results,indent=2)+'\n')
