"""Batch 6 of Uruguayan acts: writes scripts/uruguay-law/corpus.d/90-batch6.json (gitlaw_common/SCHEMA.md).

    python -X utf8 scripts/uruguay-law/batch6/batch6.py [slugs] [--dry]
    python -X utf8 scripts/uruguay-law/batch6/batch6.py --vigencia <slug>...
    python -X utf8 scripts/uruguay-law/batch6/batch6.py --count [slugs]

Batch 5's module with this batch's acts: batch5 is imported (it brings batches 2 to 4's readings and its own law days
and article reading), batch 3's readings are re-installed with batch 4, 5 and 6's original-text prefixes, and batch5's
part writer runs with this batch's table, part file and decisions.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
UY = HERE.parent
sys.path.insert(0, str(UY / 'batch5'))
sys.path.insert(0, str(UY / 'batch4'))
import batch5 as b5  # noqa: E402

ih, batch2, batch3, batch4 = b5.ih, b5.batch2, b5.batch3, b5.batch4
_law = b5._law

ACTS: dict[str, dict] = dict([
    _law('ley-18387', 'Ley 18.387', 'Ley de Declaración Judicial del Concurso y Reorganización Empresarial '
                                    '(Ley Nº 18.387)', 'leyes/18387-2008'),
    _law('ley-17703', 'Ley 17.703', 'Ley de Fideicomiso (Ley Nº 17.703)', 'leyes/17703-2003'),
    _law('ley-16871', 'Ley 16.871', 'Ley de Registros Públicos (Ley Nº 16.871)', 'leyes/16871-1997'),
    _law('ley-18627', 'Ley 18.627', 'Ley de Mercado de Valores (Ley Nº 18.627)', 'leyes/18627-2009'),
    _law('ley-19210', 'Ley 19.210', 'Ley de Inclusión Financiera (Ley Nº 19.210)', 'leyes/19210-2014'),
    _law('ley-18212', 'Ley 18.212', 'Ley de Tasas de Interés y Usura (Ley Nº 18.212)', 'leyes/18212-2007'),
    _law('ley-18099', 'Ley 18.099', 'Ley de Responsabilidad Solidaria y Seguros por Accidentes de Trabajo '
                                    '(Ley Nº 18.099)', 'leyes/18099-2007'),
    _law('ley-18065', 'Ley 18.065', 'Ley de Trabajo Doméstico (Ley Nº 18.065)', 'leyes/18065-2006'),
    _law('ley-16074', 'Ley 16.074', 'Ley de Seguros sobre Accidentes de Trabajo y Enfermedades Profesionales '
                                    '(Ley Nº 16.074)', 'leyes/16074-1989'),
    _law('ley-19121', 'Ley 19.121', 'Estatuto del Funcionario Público de la Administración Central (Ley Nº 19.121)',
         'leyes/19121-2013'),
    _law('ley-17060', 'Ley 17.060', 'Ley Cristal: Funcionarios Públicos (Ley Nº 17.060)', 'leyes/17060-1998'),
    _law('ley-18335', 'Ley 18.335', 'Ley de Derechos y Obligaciones de Pacientes y Usuarios de los Servicios de Salud '
                                    '(Ley Nº 18.335)', 'leyes/18335-2008'),
    _law('ley-19684', 'Ley 19.684', 'Ley Integral para Personas Trans (Ley Nº 19.684)', 'leyes/19684-2018'),
    _law('ley-19161', 'Ley 19.161', 'Ley de Subsidios por Maternidad, Paternidad y Cuidado del Recién Nacido '
                                    '(Ley Nº 19.161)', 'leyes/19161-2013'),
    _law('ley-18384', 'Ley 18.384', 'Estatuto del Artista y Oficios Conexos (Ley Nº 18.384)', 'leyes/18384-2008'),
])

VIGENCIA: dict[str, str] = {}
for _cfg in ACTS.values():
    _cfg['vigencia'] = {**batch3.VIGENCIA, **batch4.VIGENCIA, **b5.VIGENCIA, **VIGENCIA, **_cfg['vigencia']}


def _reinstall() -> None:
    for n, f in batch4._ORIG.items():
        setattr(ih, n, f)
    ih._batch3 = False
    added = {**batch4.ACTS, **b5.ACTS, **ACTS}
    for slug in added:
        assert slug not in batch3.ACTS, slug
    batch3.ACTS.update(added)
    try:
        batch3._install()
    finally:
        for slug in added:
            del batch3.ACTS[slug]


_reinstall()

# Amending laws whose day the general reading gets wrong here (each read by hand from IMPO's text of the law, cached).
LAW_DAY: dict[str, tuple[str, str]] = {
    '17296': ('2001-01-01', 'its art. 2: "La presente ley regirá a partir del 1º de enero de 2001, excepto en aquellas '
                            'disposiciones para las cuales, en forma expresa, se establezca otra fecha de vigencia" (as '
                            'batch 2 dates it for the CGP)'),
    '19732': ('2019-01-28', 'no general vigencia article (art. 8 dates only itself, 1 January 2020; art. 24 dates arts. '
                            '13 to 18): published 2019-01-18; Código Civil art. 1: ten days after publication'),
    '20396': ('2025-05-14', 'its art. 22: "La presente ley entrará en vigor a los 90 (noventa) días a contar desde su '
                            'promulgación" (promulgated 13/02/2025)'),
    # Found by the audit of every default-dated amending law (batch12/.tmp/default_audit.py, 2026-10-31): each law's
    # own general vigencia article, which the general reading missed (an IMPO "Ver vigencia" pointer to one of its
    # article-level clauses was taken for it, or the wording has no date). Batches 6 to 12 all import this table.
    '15851': ('1987-01-01', 'its art. 230: "La presente ley regirá a partir del 1º de enero de 1987 excepto en aquellas '
                            'disposiciones en que, en forma expresa se establezca otra fecha de vigencia"'),
    '16002': ('1989-01-01', 'its art. 1: "La presente ley regirá a partir del 1º de enero de 1989, excepto en aquellas '
                            'disposiciones en que, en forma expresa, se establezca otra fecha de vigencia"'),
    '16017': ('1989-01-20', 'its art. 51: "Esta ley entrará en vigencia desde la fecha de su promulgación" (promulgated '
                            '20/01/1989)'),
    '16134': ('1991-01-01', 'its art. 2: "La presente Ley regirá a partir del 1º de enero de 1991, excepto en aquellas '
                            'disposiciones en que, en forma expresa, se establezca otra fecha de vigencia"'),
    '16320': ('1993-01-01', 'its art. 2: "La presente ley regirá a partir del 1° de enero de 1993, excepto en aquellas '
                            'disposiciones en que, en forma expresa, se establezca otra fecha de vigencia"'),
    '16883': ('1997-12-01', 'its art. 10: "La presente ley entrará en vigencia el primer día hábil del mes siguiente a su '
                            'publicación" (published 20/11/1997; Monday 1 December 1997)'),
    '18395': ('2009-02-01', 'its art. 17: "La presente ley entrará en vigencia el primer día del cuarto mes siguiente al '
                            'de su promulgación" (promulgated 24/10/2008), except Capítulo I (see its articles)'),
    '18458': ('2009-01-02', 'its art. 6: "La presente ley entrará en vigencia a la fecha de su promulgación" '
                            '(promulgated 02/01/2009)'),
    '19162': ('2014-02-01', 'its art. 30: "La presente ley entrará en vigencia el primer día del mes siguiente al del '
                            'cumplimiento de los noventa días de su promulgación" (promulgated 01/11/2013; the ninetieth '
                            'day is 30/01/2014); its exception for "la instrumentación de los Subfondos" names no article '
                            'and is not applied'),
    '19566': ('2018-03-08', 'its art. 31: "La presente ley entrará en vigencia a los noventa días de su promulgación" '
                            '(promulgated 08/12/2017)'),
    '19590': ('2018-04-01', 'its art. 26: "La presente ley entrará en vigencia el primer día del mes siguiente al del '
                            'cumplimiento de los noventa días de su promulgación" (promulgated 28/12/2017; the ninetieth '
                            'day is 28/03/2018)'),
    '19797': ('2020-03-01', 'its art. 6: "La presente ley entrará en vigencia el 1° de marzo de 2020"'),
}
batch2.LAW_DAY.update(LAW_DAY)

# Amending articles dated by another article of their law (law, article) -> (day, how).
ARTICLE_DAY: dict[tuple[str, str], tuple[str, str]] = {
    ('19732', str(n)): ('2019-01-01', f'Ley Nº 19.732 art. 24: "Lo dispuesto en los artículos 13 a 18 de la presente '
                                      f'ley regirá a partir del 1° de enero de 2019" (art. {n})')
    for n in range(13, 19)
}
# Ley 18.395 Capítulo I (arts. 1 to 3): its art. 17 says they "regirán, como máximo, a partir del 1º de julio de 2009";
# no earlier day is given in the law, so they are shown on that latest day.
ARTICLE_DAY.update({
    ('18395', str(n)): ('2009-07-01', f'Ley Nº 18.395 art. 17: "salvo las disposiciones contenidas en el Capítulo I que '
                                      f'regirán, como máximo, a partir del 1º de julio de 2009" (art. {n}, Capítulo I; '
                                      f'shown on that latest day)')
    for n in range(1, 4)
})
# Ley 20.130 (coordinator decision 2026-10-31): each provision on the day its own art. 6 sets. The law's day stays
# 2023-08-01 (numeral 1, "regla de principio"). Numeral 4 puts the Sistema Previsional Común in force "el primer día del
# mes siguiente al del cumplimiento de los ciento ochenta días de la publicación" (published 10/05/2023: 2023-12-01),
# with the second pillar on the same day: Título III (first pillar, arts. 26-85) and Título IV (second pillar, arts.
# 86-100). Kept on 2023-08-01: numeral 3's first-pillar incapacity rules (arts. 33, 41, 42, 48, 49, 50) and Título III
# Capítulo IV (survivor pensions, arts. 52-74, including art. 74's repeals), which art. 53 puts in force "de acuerdo a
# lo dispuesto en el numeral 1) del artículo 6°". Título V (arts. 101-124, fund administration) is not singled out by
# art. 6: numeral 1, a judgement call. Art. 97 and art. 100 (second-pillar incapacity financing) follow numeral 4:
# numeral 3 names only the first pillar.
_L20130_NUMERAL_1 = {33, 41, 42, 48, 49, 50, *range(52, 75)}
ARTICLE_DAY.update({
    ('20130', str(n)): ('2023-12-01', f'Ley Nº 20.130 art. 6 numeral 4: "el Sistema Previsional Común entrará en vigor el '
                                      f'primer día del mes siguiente al del cumplimiento de los ciento ochenta días de '
                                      f'la publicación de la presente ley en el Diario Oficial" (published 10/05/2023; '
                                      f'art. {n}, Título {"III" if n < 86 else "IV"})')
    for n in range(26, 101) if n not in _L20130_NUMERAL_1
})
_article_in_force = batch2.article_in_force


def article_in_force(law: str, year: str, art: str) -> tuple[str, str] | None:
    return ARTICLE_DAY.get((law, art)) or _article_in_force(law, year, art)


batch2.article_in_force = article_in_force

# batch2.post_pass moves a change to its amending article's own day only from the second text of an article on; an
# article a law added (its first text) stays on the law's day. Here such a first text moves too when ARTICLE_DAY dates
# the adding article and the move keeps the order (Ley 19.210 art. 41 BIS, added by Ley 19.732 art. 18).
_build_one = batch2.build_one


def build_one(slug: str, cfg: dict, verification: dict):
    laws, act, v = _build_one(slug, cfg, verification)
    arts, _ = ih.articles(ih.load(cfg['path']))
    tl, _ = batch2.timelines(act)
    base_day = v['base_in_force']['day']
    moved = []
    for a in arts:
        chain = tl.get(a.key)
        if not chain or chain[0][1] is None:
            continue
        ls = [l.removeprefix('ley-') for l in chain[0][2]]
        days = [ARTICLE_DAY[(e.law, e.art)] for e in a.events
                if (e.law, e.art) in ARTICLE_DAY and e.law in ls and not e.scope
                and e.kind in ('added', 'added-earlier', 'wording-earlier', 'wording')]
        if not ls or len(ls) != 1 or not days:
            continue
        new, how = max(days)
        if new != chain[0][0] and new > base_day and (len(chain) == 1 or new < chain[1][0]):
            moved.append(f'{a.label}: {chain[0][0]} -> {new} ({how})')
            chain[0][0] = new
    if moved:
        act['versions'] = batch2.versions_from(tl, act['versions'])
    v['post_pass']['added_article_vigencia'] = moved
    return laws, act, v


batch2.build_one = build_one

b5.ACTS = ACTS
b5.PART = UY / 'corpus.d' / '90-batch6.json'
b5.VERIFICATION = HERE / 'verification.json'
b5.OTHER_PARTS = b5.OTHER_PARTS + [UY / 'corpus.d' / '80-batch5.json']
b5.DECISIONS_COMMON = [d.replace('Batch 5 acts', 'Batch 6 acts').replace('batches 2 to 4', 'batches 2 to 5')
                       for d in b5.DECISIONS_COMMON]
ACT_DECISIONS: dict[str, list[str]] = {}
b5.ACT_DECISIONS = ACT_DECISIONS

if __name__ == '__main__':
    if sys.argv[1:2] == ['--vigencia']:
        batch2.ACTS.update(ACTS)
        for s in sys.argv[2:]:
            batch2.vigencia_report(s)
    elif sys.argv[1:2] == ['--count']:
        b5.count(sys.argv[2:])
    else:
        b5.main(sys.argv[1:])
