import json, collections, difflib, sys
vf = sys.argv[1]
v = json.load(open(vf, encoding='utf8'))
print('shared differing', list(v['_shared_law_entries_differing']))
for s, x in v.items():
    if s.startswith('_'): continue
    odd = [l for l, y in x['in_force'].items() if '(artículo' in y['how'] and 'Código Civil' in y['how']]
    print('==', s, x['base_in_force']['day'], x['base_in_force']['how'][:90], 'ODD' if odd else '', odd,
          'impo', x['impo_check']['today']['equal'], x['impo_check']['last_version']['equal'])
    for k, r in x['articles'].items():
        if 'unresolved' in r: print('   UNRES', k, str(r['unresolved'])[:200], r.get('resolved_by_post_pass'))
    for k, items in x['post_pass'].items():
        for it in items: print('   PP', k, str(it)[:230])
    for p, r in x.get('unamended_sample', {}).items():
        if r == 'same words': continue
        if isinstance(r, str): print('   S', p, r); continue
        a = ' / '.join(r['original']).split(); b = ' / '.join(r['impo_today']).split()
        sm = difflib.SequenceMatcher(None, a, b)
        print('   S', p, [(op, ' '.join(a[i1:i2])[:60], ' '.join(b[j1:j2])[:60]) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != 'equal'][:4])
    if x.get('before_first_day'): print('   BEFORE', x['before_first_day'])
d = collections.defaultdict(set)
files = ['batch2/verification.json', 'batch3/verification.json', 'batch4/verification.json', 'batch5/verification.json',
         'batch6/verification.json', 'batch7/verification.json'] + sys.argv[2:] + [vf]
for f in files:
    vv = json.load(open(f, encoding='utf8'))
    for s, x in vv.items():
        if s.startswith('_') or not isinstance(x, dict): continue
        for k, y in x.get('in_force', {}).items(): d[k].add((y['day'], f.split('/')[0] + ':' + s))
for k, vals in sorted(d.items()):
    if len({a for a, b in vals}) > 1: print('DAYDIFF', k, sorted(vals))
