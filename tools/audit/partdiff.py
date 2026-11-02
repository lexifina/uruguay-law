import json, sys, glob, os
for f in sorted(glob.glob('.tmp/audit/prev/*.json')):
    name = os.path.basename(f)
    a = json.load(open(f, encoding='utf8')); b = json.load(open('corpus.d/' + name, encoding='utf8'))
    if a == b:
        print(name, 'identical'); continue
    print(name, {k: a.get(k) == b.get(k) for k in set(a) | set(b)})
    for x, y in zip(a['acts'], b['acts']):
        if x != y:
            fx = [v['from'] for v in x['versions']]; fy = [v['from'] for v in y['versions']]
            print('  ', x['slug'], 'from removed', sorted(set(fx) - set(fy)), 'added', sorted(set(fy) - set(fx)))
    print('   new decisions:', [d[:150] for d in b['decisions'] if d not in a['decisions']][:6])
