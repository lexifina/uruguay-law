"""README rows and jurisdiction.json counts for current-text parts.

    python -X utf8 scripts/uruguay-law/breadth/docs.py <total acts> <total versions> corpus.d/<part>.json ...

Adds one README row per act of the given parts (an existing row for the act is replaced), adds the paragraph on
current-text acts once, and sets jurisdiction.json's "build" counts, naming how many acts are current text only
(every act of every 99j-breadth part listed or already in the README).
"""
from __future__ import annotations

import datetime
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
M = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
     'December']
MARK = '**Current text only.**'
PARA = (f'{MARK} The acts whose History reads "Current text only" have one version: IMPO\'s consolidated text as '
        'published today, the oldest version available here, credited to IMPO and not to a law. Where the History '
        'says "in force from", the version is dated by its in-force day: that of the last law IMPO\'s notes name as '
        "changing the text, or the law's own when the notes name none, each found as for the other acts (a law's own "
        'vigencia article, else ten days after its publication). Where it says "last changed", the version is dated '
        "by the latest date IMPO's notes give for a change (for a law, the date IMPO prints for it) or by the law's "
        'promulgation; those dates are to be corrected to in-force days. Articles IMPO marks repealed whole, bare "(*)" articles of '
        'amendments and articles IMPO prints without text are not included. A law IMPO marks repealed whole ends '
        'with a commit, credited to the repealing law, that removes every article. Their titles are IMPO\'s own names '
        'of the laws, as IMPO prints them. Earlier versions of these acts may be added later.')
PARA_ES = (f'**Solo texto vigente.** Las leyes cuya historia dice "Current text only" tienen una sola versión: el texto '
           'actualizado de IMPO. Con "in force from" está fechada el día en que entró en vigencia (el de la última ley '
           'modificativa que nombran las notas de IMPO, o el de la propia ley); con "last changed", el último día de '
           'cambio que dan las notas de IMPO (o la promulgación), fecha que se corregirá. Una ley que IMPO '
           'marca como derogada termina con un commit, atribuido '
           'a la ley derogatoria, que retira todos sus artículos.')


def day(s: str) -> str:
    d = datetime.date.fromisoformat(s)
    return f'{d.day} {M[d.month - 1]} {d.year}'


def row(a: dict, laws: dict) -> str:
    t = a['title']
    name, num = t[:t.rindex('(')].strip(), t[t.rindex('(') + 1:-1]
    own = laws[a['earlier_laws'][0]]
    v0 = a['versions'][0]
    hist = f'Current text only (IMPO\'s text, in force from {day(v0["from"])})'
    if len(a['versions']) == 2:
        rep = next(iter(a['versions'][1]['credits'].values()))[0]
        hist += f', then repealed by {laws[rep]["label"].replace(" Nº", "")} (in force {day(a["versions"][1]["from"])})'
    else:
        hist += ', to today'
    return f'| `{a["slug"]}/` | {name} ({num} of {own["enacted"][:4]}) | {len(a["versions"])} | {hist} |'


def main(argv: list[str]) -> None:
    acts_total, versions_total, parts = argv[0], argv[1], argv[2:]
    p = ROOT / 'repo' / 'README.md'
    s = p.read_text(encoding='utf-8')
    lines = s.split('\n')
    for f in parts:
        d = json.load(open(f, encoding='utf-8'))
        for a in d['acts']:
            r = row(a, d['laws'])
            key = f'| `{a["slug"]}/` |'
            idx = [i for i, l in enumerate(lines) if l.startswith(key)]
            if idx:
                lines[idx[0]] = r
            else:
                last = max(i for i, l in enumerate(lines) if re.match(r'\| `[a-z0-9-]+/` \|', l))
                lines.insert(last + 1, r)
    s = '\n'.join(lines)
    lines = s.split('\n')
    for mark, para, anchor in ((MARK, PARA, 'The articles are `<act>/art-NNN.md`'),
                               ('**Solo texto vigente.**', PARA_ES,
                                'Solo los textos del Parlamento y de IMPO son oficiales.')):
        idx = [i for i, l in enumerate(lines) if l.startswith(mark)]
        if idx:
            lines[idx[0]] = para          # one paragraph, kept current
        else:
            at = next(i for i, l in enumerate(lines) if l.startswith(anchor))
            lines[at:at] = [para, '']
    s = '\n'.join(lines)
    p.write_text(s, encoding='utf-8', newline='\n')
    current = sum(1 for l in s.split('\n') if re.match(r'\| `[a-z0-9-]+/` \| .* \| Current text only', l))
    j = ROOT / 'repo' / 'jurisdiction.json'
    t = j.read_text(encoding='utf-8')
    t2 = re.sub(r'"build": "built: \d+ acts, \d+ versions:', f'"build": "built: {acts_total} acts, {versions_total} versions:', t)
    t2 = re.sub(r'(each from its first version or entry into force to today)(; \d+ more laws as their current text only)?"',
                rf'\1; {current} more laws as their current text only"', t2)
    assert t2 != t
    j.write_text(t2, encoding='utf-8', newline='\n')
    print('rows', sum(len(json.load(open(f, encoding='utf-8'))['acts']) for f in parts), 'current-text rows', current,
          'counts', acts_total, versions_total)


if __name__ == '__main__':
    main(sys.argv[1:])
