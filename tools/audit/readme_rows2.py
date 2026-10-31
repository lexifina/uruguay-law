"""Rewrite (or insert after `after`) the README table rows for the acts of the given parts."""
import json, sys, datetime
from pathlib import Path
M = ['January','February','March','April','May','June','July','August','September','October','November','December']
def day(s):
    d = datetime.date.fromisoformat(s); return f'{d.day} {M[d.month-1]} {d.year}'
def rows_for(part):
    out = []
    for a in part['acts']:
        L = part['laws']
        laws = sorted({l for v in a['versions'] for ls in v.get('credits', {}).values() for l in ls} - {a.get('first_law')} - set(a.get('earlier_laws') or []),
                      key=lambda l: (L[l]['enacted'] or '', l))
        lab = lambda l: L[l]['label'].replace(' Nº', '')
        yr = lambda l: (L[l]['enacted'] or '????')[:4]
        t = a['title']; num = t[t.rindex('(') + 1:-1]; name = t[:t.rindex('(')].strip()
        base_key = a.get('first_law') or (a.get('earlier_laws') or [None])[0]
        base_year = (L[base_key]['enacted'] or '')[:4] if base_key in L else ''
        if a.get('first_law'):
            hist = f'As enacted (in force {day(a["versions"][0]["from"])})'
        else:
            pre = [lab(l) for l in (a.get('earlier_laws') or [])[1:]]
            hist = f'From its entry into force ({day(a["versions"][0]["from"])}), with the changes ' + ', '.join(pre) + ' made by that day'
        if not laws: hist += ', with no later amendment recorded by IMPO, to today' if not a.get('first_law') else ', with no amendment recorded by IMPO, to today'
        elif len(laws) <= 3: hist += ', then ' + ', '.join(lab(l) for l in laws) + ', to today'
        else: hist += f', then {len(laws)} amending laws from {lab(laws[0])} ({yr(laws[0])}) to {lab(laws[-1])} ({yr(laws[-1])}), to today'
        out.append((f'| `{a["slug"]}/` |', f'| `{a["slug"]}/` | {name} ({num} of {base_year}) | {len(a["versions"])} | {hist} |'))
    return out
p = Path('repo/README.md'); lines = p.read_text(encoding='utf-8').split('\n')
for f in sys.argv[1:]:
    for key, row in rows_for(json.load(open(f, encoding='utf8'))):
        idx = [i for i, l in enumerate(lines) if l.startswith(key)]
        if idx:
            lines[idx[0]] = row
        else:
            last = max(i for i, l in enumerate(lines) if l.startswith('| `'))
            lines.insert(last + 1, row)
p.write_text('\n'.join(lines), encoding='utf-8', newline='\n')
