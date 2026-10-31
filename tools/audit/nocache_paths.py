import json, glob, sys, os, subprocess
sys.path.insert(0, '.')
import impo_history as ih
labs = set(l.strip() for l in open('.tmp/audit/nocache.txt', encoding='utf8') if l.strip())
urls = {}
for f in sorted(glob.glob('corpus.d/*.json')) + ['corpus.json']:
    for k, x in json.load(open(f, encoding='utf8')).get('laws', {}).items():
        if x['label'] in labs and x.get('url'):
            urls[x['label']] = x['url'].split('/bases/', 1)[1]
print(len(labs), 'labels,', len(urls), 'with url', sorted(labs - set(urls)))
open('.tmp/audit/nocache_paths.txt', 'w', encoding='utf8', newline='\n').write('\n'.join(sorted(set(urls.values()))) + '\n')
