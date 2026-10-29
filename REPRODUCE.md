# How this repository was made (Uruguay)

This file is written by the build on 2026-10-29, the day the source data was retrieved. Everything below is enough to rebuild this repository hash for hash.

## Sources

| Source | Address | Retrieved | Requests | Licence |
| --- | --- | --- | ---: | --- |
| IMPO, Base de datos de normativa | <https://www.impo.com.uy/bases> | 2026-10-28 | 534 | Texts from IMPO, Base de datos de normativa (www.impo.com.uy/bases), and the Parlamento del Uruguay (parlamento.gub.uy, read through Wayback Machine captures). |
| Parlamento del Uruguay, dated texts of the Constitución, via the Wayback Machine | <https://parlamento.gub.uy/documentosyleyes/constitucion> | 2026-10-28 | 10 | Texts from IMPO, Base de datos de normativa (www.impo.com.uy/bases), and the Parlamento del Uruguay (parlamento.gub.uy, read through Wayback Machine captures). |
| IMPO, Base de datos de normativa (codes of corpus.d/50-batch2) | <https://www.impo.com.uy/bases> | 2026-10-28 | 685 | Texts from IMPO, Base de datos de normativa (www.impo.com.uy/bases). |
| IMPO, Base de datos de normativa (acts of corpus.d/60-batch3) | <https://www.impo.com.uy/bases> | 2026-10-29 | 505 | Texts from IMPO, Base de datos de normativa (www.impo.com.uy/bases). |
| IMPO, Base de datos de normativa (acts of corpus.d/70-batch4) | <https://www.impo.com.uy/bases> | 2026-10-29 | 162 | Texts from IMPO, Base de datos de normativa (www.impo.com.uy/bases). |

Every response is cached by the sha256 of its URL, and the table above lists every source with its retrieval date. Lexifina keeps its fetch scripts privately; `tools/parse.py` reads only the cache and writes `corpus.json`, so the same cache always gives the same corpus.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitucion` | Constitución de la República Oriental del Uruguay | 5 | 1967-02-15 to 2004-10-31 |
| `ley-18331` | Ley Nº 18.331 de Protección de Datos Personales | 7 | 2008-08-28 to 2023-01-01 |
| `codigo-civil` | Código Civil (texto aprobado por la Ley Nº 16.603) | 18 | 1994-12-01 to 2026-01-01 |
| `codigo-penal` | Código Penal (Ley Nº 9.155) | 36 | 1934-08-01 to 2024-10-07 |
| `codigo-general-proceso` | Código General del Proceso (Ley Nº 15.982) | 28 | 1989-11-20 to 2026-01-01 |
| `codigo-comercio` | Código de Comercio | 14 | 1866-01-24 to 2020-07-24 |
| `codigo-proceso-penal` | Código del Proceso Penal (Ley Nº 19.293) | 12 | 2017-11-01 to 2026-09-24 |
| `ley-17250` | Ley de Relaciones de Consumo (Ley Nº 17.250) | 7 | 2000-08-27 to 2024-01-01 |
| `codigo-aduanero` | Código Aduanero de la República Oriental del Uruguay (Ley Nº 19.276) | 9 | 2015-03-18 to 2025-09-13 |
| `codigo-tributario` | Código Tributario (Decreto-Ley Nº 14.306) | 10 | 1974-12-16 to 2026-01-01 |
| `ley-16060` | Ley de Sociedades Comerciales (Ley Nº 16.060) | 21 | 1989-12-31 to 2021-01-01 |
| `codigo-ninez-adolescencia` | Código de la Niñez y la Adolescencia (Ley Nº 17.823) | 22 | 2004-09-24 to 2024-06-02 |
| `ley-18381` | Ley sobre el Derecho de Acceso a la Información Pública (Ley Nº 18.381) | 4 | 2008-11-17 to 2022-01-01 |
| `ley-17514` | Ley de Erradicación de la Violencia Doméstica (Ley Nº 17.514) | 3 | 2002-07-19 to 2019-01-01 |
| `ley-19580` | Ley de Violencia hacia las Mujeres Basada en Género (Ley Nº 19.580) | 7 | 2018-01-19 to 2026-01-01 |
| `ley-19574` | Ley Integral contra el Lavado de Activos (Ley Nº 19.574) | 8 | 2018-01-20 to 2026-04-20 |

The build made 147 commits:

| Commits | Kind |
| ---: | --- |
| 16 | first version of an act |
| 131 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `futuro`: laws not yet in force on 2026-10-29.
- 8 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 171 laws in the record.
- 350 tags.

## Dates

Each commit is dated at noon (America/Montevideo) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Código Civil art. 1: laws are binding by their promulgation by the Poder Ejecutivo, and the promulgation is deemed known ten days after it is verified in the capital. A law's own vigencia clause overrides this. A constitutional reform approved by plebiscite takes effect when the Corte Electoral proclaims the result (Constitución, Disposición transitoria A). https://www.impo.com.uy/bases/codigo-civil/16603-1994/1

## Commands, in order

```sh
# fill the cache from the sources listed above (network; Lexifina's fetch scripts are kept privately)
python -X utf8 tools/parse.py                  # cache -> corpus.json (no network)
python -X utf8 tools/build.py <folder> --repo <empty folder> --docs-date 2026-10-29
python -X utf8 tools/check_repo.py <repo> --corpus <folder>/corpus.json --write
python -X utf8 tools/build.py <folder> --repo <another empty folder> --docs-date 2026-10-29 --compare <repo>
```

In the main Lexifina repository these files live as follows:
- `fetch.py`, `parse.py` and `repo/`: in `scripts/uruguay-law/`.
- `build.py`, `check_repo.py` (`check.py` there) and `on.py`: in `scripts/gitlaw_common/`, with the corpus format in `SCHEMA.md`.

## Exact inputs

- `corpus.json` sha256 `ac64096717d8d3271769dd1b34a99ecbdd0de9cd9668a1efe3ac8275ac640422` (5403756 bytes)
- Script blob hashes (`git hash-object`):

| Script | Blob |
| --- | --- |
| build.py | `2bfc4ac9df193a7be844556d7f69cdb9d93ec3f2` |
| check.py | `cd346c7ff9996d450240e3bab52bcae03b2bc865` |
| on.py | `644a6c0857fbcc72562032b58d57aa113fee0641` |
| fetch.py | `48f54c5b2423f577d2253f5d7f48f5ba68aac381` |
| parse.py | `3bb324230c4f2a8e12b9130c054d90305a5b5d06` |

- Tools:
  - Python 3.14.0
  - git version 2.52.0.windows.1
  - curl 8.21.0 (Windows) libcurl/8.21.0 Schannel zlib/1.3.2 WinIDN WinLDAP

## Checks

189 versions of 12 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

A second build from the same corpus into an empty folder gave identical hashes for all 137 history commits and 320 tags (history tip `f8f07707f19e1068185ba73230cf82908d9a76b2`).

These results are from the check run on the build before this one, from the same corpus.

## Decisions made by hand

- Constitution: the dated texts are the Parlamento's editions of 1967, 1989, 1994, 1997 and 2004; today's text is IMPO's consolidated text. The units each reform changed come from comparing consecutive Parlamento editions word by word, and parse.py stops unless they equal the units IMPO's own notes ("redacción dada por", "agregado por") assign to that plebiscite.
- Constitution: the Parlamento and IMPO transcriptions differ in a few words in about 40 units (listed in verification.json). These are not changes in the law, so a unit uses IMPO's text from its last reform on (throughout, if no reform touched it), and the Parlamento's text only before that.
- Constitution: where a reform added incisos to an article (arts. 47, 67, 188), the earlier text is IMPO's text minus those incisos whenever that has exactly the Parlamento's earlier words.
- Constitution: the Parlamento's 2004 edition changes words in a few articles that no reform and no IMPO note explains (verification.json, parlamento_changes_no_reform_explains); they are not committed as changes.
- Constitution: the 1994, 1996 and 2004 reforms took effect when the Corte Electoral proclaimed the result. No source we read dates those proclamations, so their versions are dated on the plebiscite day, and each law's note says so.
- Constitution: the 1989 reform is dated 1 May 1990, the day its transitional provision V) puts it in force.
- Constitution: the Parlamento letters the 1994 and 2004 transitional provisions as a second V) and a further Z); IMPO letters them V') and Z"). IMPO's lettering is used (disp-trans-v-prima, disp-trans-z-segunda).
- Laws (impo_history.py): IMPO gives only today's text, with notes naming the amending law and article for each change, and a link to the article as originally published. The first version of an amended article is that original text; today's text follows the last amending law. A text in between is used only when a source gives it: the wording the earlier amending law quotes (IMPO's original of that law), today's text without an item IMPO says a later law added, or the earlier text with an item replaced by the wording the amending law quotes for it. Otherwise the change is shown on the next known day, credited to every law in between, and verification.json lists it as unresolved.
- Laws: an amending law takes effect on the day its own vigencia article gives ("regirá a partir del …", read from IMPO's text of the article its notes point to, or for Ley 18.719 its art. 3, read by hand), else ten days after its publication in the Diario Oficial (Código Civil art. 1).
- Laws: amending laws that took effect before the norm's own first day are already in its text and are not credited.
- Código Civil: the oldest version is the text approved by Ley Nº 16.603 (promulgated 19 October 1994, published 21 November 1994, in force 1 December 1994 by Código Civil art. 1), the re-edition IMPO consolidates. The code of 1868 and its amendments before 1994 are not in IMPO's data, so the first commit is "oldest version available".
- Código Civil arts. 2393 to 2405: IMPO still prints them, with a note that Ley Nº 19.920 art. 62 repealed the Ley Nº 10.084 that added them; they are removed on Ley 19.920's day.
- Vigencia articles read by hand (fetch.IMPO_ACTS) where IMPO's notes do not point to one: Ley 18.719 art. 3, Ley 17.703 art. 46, Ley 18.387 art. 255, Ley 19.075 art. 29, Ley 19.920 art. 63, Ley 19.670 art. 2, Ley 15.903 art. 2, Ley 17.897 art. 23 (in force on promulgation).
- Código Penal: in force 1 August 1934 by Ley Nº 9.414 art. 2, which IMPO's note on the code cites. IMPO's text is the update of the Versión Oficial of 26 October 1967 (Decreto 698/967), and IMPO records no amendment before Ley 13.737 (1969); changes made between 1934 and 1969, if any, are not shown and would appear inside the next recorded change of that article. A sample of 11 unamended articles has exactly the words of IMPO's 1933 original text.
- Código Penal: Ley 19.138 takes effect ten days after its regulation by the Poder Ejecutivo, which we did not date; its one change (art. 350 BIS literal C) is dated by the default rule.
- Unit text: IMPO's hard-wrapped lines are joined into paragraphs (one paragraph or lettered item per line); ordinal marks, quotes and IMPO's "(*)" amended markers are normalised once in parse.py.
- Batch 2 codes (corpus.d/50-batch2.json) are rebuilt by the same impo_history.py as the Código Civil and Penal: the original text of each amended article from IMPO's TEXTO ORIGINAL link, today's text from IMPO, sourced intermediate texts only, and each amending law in force on the day its own vigencia article gives, else ten days after publication (Código Civil art. 1).
- Batch 2: IMPO notes "Derogado anteriormente por" and "Redacción derogada por" are read as events of that law; an article repealed and later given new wording is absent in between.
- Batch 2: IMPO scopes changes in the CGP and CPP to "ordinales" (e.g. 547.1); such a note is read as a scoped change to the article, never as a change to the whole article.
- Batch 2, anachronism rule: where a unit would show today's wording before the last law IMPO says gave it was in force, it reads "[La fuente no da el texto vigente en esta fecha.]" until that day (or is absent if that law inserted it); the units are listed below and in batch2/verification.json (post_pass).
- CGP: in force 20 November 1989 by its own art. 547 (as worded by Ley 16.053, which took effect before the code and is therefore part of its first text). The first version is therefore the code as in force on that day (Ley 15.982 with Ley 16.053's changes), credited to the publisher as the oldest version available, naming both laws.
- CGP: vigencia articles read by hand (batch2.ACTS): Ley 16.053 art. 3, 16.170 art. 2, 16.226 art. 2, 16.462 art. 2, 16.871 art. 101, 17.296 art. 2, 17.453 art. 51, 17.707 art. 28, 17.930 art. 2, 18.172 art. 2, 18.387 art. 255, 19.090 art. 2, 19.535 art. 2, 19.670 art. 2; budget laws that say they rule from 1 January are dated so even when published later. Ley 19.090 ("el día hábil siguiente a los sesenta días de su promulgación", promulgated 14/06/2013) is dated 14/08/2013; Ley 20.130 (art. 6.1, first day of the third month after publication on 10/05/2023) 01/08/2023.
- CGP: an amending article's own clause ("El presente artículo entrará en vigencia a partir de la promulgación") overrides its law's day when it keeps the article's changes in order (post_pass article_vigencia).
- CGP: many amending laws quote a single ordinal ("ARTICULO 349.3", "Sustitúyese el artículo 29.1"); such a quote is not taken for the whole article, so that intermediate text is unknown and the change is shown on the next day with a known text, credited to every law in between (batch2/verification.json).
- CGP: Ley 20.531 (promulgated 01/10/2026, in force 1 January 2027 by its art. 2) substitutes arts. 64 and 64 BIS; IMPO's consolidated text does not include it yet, so it is not in this history.
- CGP, absent between: Artículo 452: absent from 2008-11-02 (Ley Nº 18.387, "derogado anteriormente") until 2013-08-14.
- CGP, added part removed: Artículo 548: before 1992-01-01, today's text without Apartado ordinal 1º) inciso 2º) (Ley Nº 16.226 art. 327 quotes it).
- Código de Comercio: the first version is the code of 1865 (Ley Nº 817) as IMPO gives it, dated 24 January 1866, the promulgation of Ley Nº 841, which fixed the day the code began to apply; that day is only in IMPO's scan of Ley Nº 841, which is not read (no OCR). The version is credited to the publisher as the oldest version available, naming Leyes 817 and 841.
- Código de Comercio: each amended article starts from IMPO's original 1865 text (textos-originales-ley/817-1865); unamended articles carry IMPO's consolidated text throughout. In a fixed sample of 12 unamended articles, 10 have the original's words exactly; arts. 66 ("hacerse,", "asiento,", "foja" for "hoja") and 382 ("los" for "lo") differ in punctuation or one word, with no amending law recorded, so no change is committed for them (batch2/verification.json, unamended_sample).
- Código de Comercio: vigencia articles read by hand: Decreto-Ley 14.701 art. 127 (1 November 1977), Ley 16.060 art. 511 (sixty days after publication on 01/11/1989: 31/12/1989), Ley 17.930 art. 2, Ley 18.387 art. 255; laws of 1878 and 1882 that IMPO gives no publication day for are dated ten days after promulgation.
- Código de Comercio, Libro IV (quiebras): IMPO keeps it as two entries, arts. 1523 a 1781 and 1764 a 1785, whose original texts are the 1865 arts. 1523-1747 and 1748-1768 (the numbering changed with the 1878 and 1916 texts). Ley Nº 1.422 replaced the whole book, in force 1 February 1879 by IMPO's summary of it, and Ley Nº 2.666 (1900) replaced it again; IMPO gives neither text, so from 1879 both units read the placeholder until Ley Nº 18.387 repealed them; the later partial changes IMPO lists inside that unknown text are not committed (listed under "whole rewrites" below).
- Batch 2: decree-laws of 1973-1985 (IMPO "Decreto Ley Nº") are kind "decree", with their own keys (decreto-ley-<n>) and IMPO paths (decretos-ley/).
- Código de Comercio, whole rewrites: art-1523-1781: the 1865 text until 1879-02-01, then "[La fuente no da el texto vigente en esta fecha.]" (Ley Nº 1.422 replaced it whole; IMPO's summary: "empiece a regir desde el 1º de Febrero de 1879"), removed on 2008-11-02; not credited within the unknown text: ley-5392, ley-5548, ley-8045, ley-8301, ley-8461, ley-9280, ley-13665; art-1764-1785: the 1865 text until 1879-02-01, then "[La fuente no da el texto vigente en esta fecha.]" (Ley Nº 1.422 replaced it whole; IMPO's summary: "empiece a regir desde el 1º de Febrero de 1879"), removed on 2008-11-02; not credited within the unknown text: ley-17292.
- CPP: in force 1 November 2017 by its art. 403 (as worded by Ley 19.510). Leyes 19.436, 19.474, 19.510, 19.511 and 19.544 (the last in force with the code, by its art. 11) changed it before that day, so the first version is the oldest version available; where a later law changed such an article, its first text is the wording the earlier law quotes (post_pass first_text_from_earlier_law), else the placeholder.
- CPP: arts. 383 to 392 (suspensión condicional del proceso) are absent from Ley 19.889's day until Ley 20.519 (IMPO note "Reincorporado por", in force ten days after its publication on 14/09/2026) puts them back.
- CPP: vigencia articles read by hand: Ley 19.510 art. 2, 19.670 art. 2, 20.446 art. 3; 19.544 art. 11.
- CPP, first text from earlier law: Artículo 45: the wording Ley Nº 19.474 art. 1 gives it; Artículo 49: the wording Ley Nº 19.474 art. 1 gives it; Artículo 97: the wording Ley Nº 19.436 art. 2 gives it; Artículo 127: the wording Ley Nº 19.436 art. 2 gives it; Artículo 224: the wording Ley Nº 19.436 art. 2 gives it; Artículo 268: the wording Ley Nº 19.436 art. 2 gives it; Artículo 269: the wording Ley Nº 19.436 art. 2 gives it; Artículo 270: the wording Ley Nº 19.436 art. 2 gives it; Artículo 271: unknown (placeholder); Artículo 272: the wording Ley Nº 19.436 art. 3 gives it; Artículo 273: the wording Ley Nº 19.436 art. 3 gives it; Artículo 382: the wording Ley Nº 19.436 art. 6 gives it; Artículo 383: the wording Ley Nº 19.436 art. 6 gives it; Artículo 384: the wording Ley Nº 19.436 art. 6 gives it; Artículo 385: the wording Ley Nº 19.436 art. 6 gives it; Artículo 386: the wording Ley Nº 19.436 art. 6 gives it; Artículo 387: the wording Ley Nº 19.436 art. 6 gives it; Artículo 388: the wording Ley Nº 19.436 art. 6 gives it; Artículo 389: the wording Ley Nº 19.436 art. 6 gives it; Artículo 390: the wording Ley Nº 19.436 art. 6 gives it; Artículo 391: the wording Ley Nº 19.436 art. 6 gives it; Artículo 392: the wording Ley Nº 19.436 art. 6 gives it; Artículo 394: the wording Ley Nº 19.436 art. 6 gives it; Artículo 397: the wording Ley Nº 19.436 art. 6 gives it.
- CPP, article vigencia: Artículo 45: 2019-01-01 -> 2018-10-15 (Ley Nº 19.670 art. 292: "El presente artículo entrará en vigencia a partir de la promulgación").
- CPP, absent between: Artículo 383: absent from 2020-07-24 (Ley Nº 19.889, "derogado anteriormente") until 2026-09-24; Artículo 384: absent from 2020-07-24 (Ley Nº 19.889, "derogado anteriormente") until 2026-09-24; Artículo 385: absent from 2020-07-24 (Ley Nº 19.889, "derogado anteriormente") until 2026-09-24; Artículo 386: absent from 2020-07-24 (Ley Nº 19.889, "derogado anteriormente") until 2026-09-24; Artículo 387: absent from 2020-07-24 (Ley Nº 19.889, "derogado anteriormente") until 2026-09-24; Artículo 388: absent from 2020-07-24 (Ley Nº 19.889, "derogado anteriormente") until 2026-09-24; Artículo 389: absent from 2020-07-24 (Ley Nº 19.889, "derogado anteriormente") until 2026-09-24; Artículo 390: absent from 2020-07-24 (Ley Nº 19.889, "derogado anteriormente") until 2026-09-24; Artículo 391: absent from 2020-07-24 (Ley Nº 19.889, "derogado anteriormente") until 2026-09-24; Artículo 392: absent from 2020-07-24 (Ley Nº 19.889, "derogado anteriormente") until 2026-09-24.
- CPP, placeholder: Artículo 221: today's wording held back until 2018-09-06 (Ley Nº 19.653).
- Batch 3 acts (corpus.d/60-batch3.json) are rebuilt by batch 2's code unchanged (batch2.build_one over impo_history.py): each amended article starts from IMPO's original text, today's text is IMPO's consolidated text, intermediate texts are only those an amending law quotes or IMPO's notes determine, and each amending law is in force on the day its own vigencia article gives, else ten days after publication (Código Civil art. 1). Batch 2's readings of IMPO's notes and its anachronism rule (placeholder "[La fuente no da el texto vigente en esta fecha.]") apply.
- Batch 3: IMPO's original texts end with the next section's heading, in capitals ("PROCESO INFRACCIONAL ADUANERO") or as a short line with no closing punctuation ("De los consorcios"); such trailing lines are dropped from first texts and quoted wordings (the list is in batch3/verification.json, headings_dropped).
- Batch 3: articles are dated by each amending law's general in-force day as batch 2 does; where a law also amends an act of corpus.json or batch 2, it has the same day there.
- Batch 3: Ley Nº 19.889 (Ley de Urgente Consideración) was a candidate but is left out: IMPO's consolidated text of it gives 253 of its 476 articles only as "(*)" pointers to the laws they amended, so it has no self-standing consolidated text to rebuild; its changes are in those laws' histories.
- Ley 17.250: in force 27 August 2000, ten days after its publication on 17/08/2000 (it has no vigencia clause). Vigencia articles read by hand: Ley 18.046 art. 2 and Ley 18.362 art. 2 (1 January 2007 and 2009).
- Ley 17.250: Ley Nº 20.531 (promulgated 01/10/2026, in force 1 January 2027 by its art. 2) substitutes art. 16 (art. 108) and the acápite and literales C) and F) of art. 42 (art. 117); IMPO's consolidated text does not include it yet (IMPO notes only "Ver vigencia"), so it is not in this history.
- Ley 17.250, art. 31: Literal I) was added by Ley 19.149 and reworded by Ley 20.212; the 2014 wording is not determined by IMPO's notes, so the change is shown on 1 January 2024, credited to both laws.
- Ley 17.250: amended articles IMPO gives no TEXTO ORIGINAL link for start from IMPO's original text at leyes-originales/17250-2000/<n>: Artículo 16, Artículo 18, Artículo 22, Artículo 23, Artículo 31, Artículo 47.
- CAROU: in force 18 March 2015, 180 days after its promulgation on 19/09/2014 (its art. 276).
- CAROU: Leyes 19.322 and 19.394 changed no words: each suspended the vigencia of arts. 224, 225, 227 to 257 and 269 (and of art. 275 as to its repeal of procedural articles of Ley 13.318), until 1 March 2016 and then until 16 July 2017, retroactively (each validates proceedings under the old law from the earlier date). They are recorded as wording-unchanged commits on their in-force days (ten days after publication; neither has a vigencia clause), crediting the 35 articles whose IMPO notes name them, with a note on each law; the articles' text stays in the tree throughout. The day the suspension ended (16 July 2017) is not a commit.
- CAROU: Leyes 19.651 and 20.419 have no vigencia clause and are dated ten days after publication.
- CAROU: interpretative laws IMPO names on art. 240 (Leyes 19.924 art. 230, 19.996 art. 123, 20.446 art. 198) change no words and are not recorded.
- CAROU: amended articles IMPO gives no TEXTO ORIGINAL link for start from IMPO's original text at leyes-originales/19276-2014/<n>: Artículo 15, Artículo 49.
- CAROU, suspension of vigencia: Ley Nº 19.322 art. 1 ("Suspéndese la vigencia de los artículos 224, 225, 227 a 257 y 269 ..."), in force 2015-06-18 (published 2015-06-08; Código Civil art. 1: ten days after publication): wording unchanged, credited to 35 articles IMPO notes name it on: art-224, art-225, art-227, art-228, art-229, art-230, art-231, art-232, art-233, art-234, art-235, art-236, art-237, art-238, art-239, art-240, art-241, art-242, art-243, art-244, art-245, art-246, art-247, art-248, art-249, art-250, art-251, art-252, art-253, art-254, art-255, art-256, art-257, art-269, art-275.
- CAROU, suspension of vigencia: Ley Nº 19.394 art. 1 ("Suspéndese la vigencia de los artículos 224, 225, 227 a 257 y 269 ..."), in force 2016-06-17 (published 2016-06-07; Código Civil art. 1: ten days after publication): wording unchanged, credited to 35 articles IMPO notes name it on: art-224, art-225, art-227, art-228, art-229, art-230, art-231, art-232, art-233, art-234, art-235, art-236, art-237, art-238, art-239, art-240, art-241, art-242, art-243, art-244, art-245, art-246, art-247, art-248, art-249, art-250, art-251, art-252, art-253, art-254, art-255, art-256, art-257, art-269, art-275.
- Código Tributario (Decreto-Ley Nº 14.306, kind "decree"): in force 16 December 1974, ten days after its publication on 06/12/1974 (no vigencia clause); the errata IMPO notes (published 13/12/1974) came before that day and are part of the first text. Decree-laws 14.416, 14.948, 15.294, 15.322 and 15.524 have no vigencia clause and are dated ten days after publication; Ley 18.083 by its art. 113 (1 July 2007).
- Código Tributario: in a fixed sample of 12 articles IMPO records no change to, 7 have the original's words exactly; arts. 5 ("las"/"los"), 13 ("Con"/"Son") and 105 ("representantes"/"representados", "dependencias"/"dependientes") differ by a word, art. 75 by a heading run into its text, and art. 40 by the words "ficta; se notifique la resolución definitiva" that no amending law IMPO names explains. Unamended articles carry IMPO's consolidated text throughout, so these are not committed as changes (batch3/verification.json, unamended_sample).
- Ley 16.060: in force 31 December 1989, sixty days after its publication on 01/11/1989 (its art. 511), the day batch 2 uses for it in the Código de Comercio. Its law entry is the one batch 2 published (title "LEY DE SOCIEDADES COMERCIALES").
- Ley 16.060: vigencia articles read by hand: Ley 16.736 art. 2 (1 January 1996), Ley 16.871 art. 101 (1 January 1998), Ley 18.083 art. 113 (1 July 2007), Ley 19.288 art. 21 ("primer día del segundo mes siguiente al de su promulgación", promulgated 26/09/2014: 1 November 2014); laws without a vigencia clause are dated ten days after publication.
- Ley 16.060: in a fixed sample of 12 unamended articles, 11 have the original's words (after dropping the next section's heading); art. 345 differs only in where a paragraph breaks.
- Ley de Sociedades Comerciales, absent between: Artículo 303: absent from 2009-12-26 (Ley Nº 18.627, "derogado anteriormente") until 2011-01-01; Artículo 334: absent from 2009-12-26 (Ley Nº 18.627, "derogado anteriormente") until 2011-01-01.
- CNA: in force 24 September 2004, ten days after its publication on 14/09/2004 (no vigencia clause). Vigencia read by hand: Ley 19.075 art. 29 (90 days after promulgation, as the Código Civil uses it), Ley 19.551 art. 21 (with the CPP, 1 November 2017), Ley 19.747 art. 9 (180 days after promulgation on 19/04/2019: 16 October 2019); the others by their own vigencia article or ten days after publication.
- CNA: IMPO numbers articles added inside a chapter 120.1, 132.1, 133.1 ... (IMPO "120 / 1"); they are labelled "Artículo 120.1" with keys art-120-1.
- CNA: in a fixed sample of 12 unamended articles, 10 have the original's words; art. 28 as enacted also reworded inciso 4 of Código Civil art. 227, a paragraph IMPO's consolidated text leaves out, and art. 199 reads "Instituto del Niño y Adolescente del Uruguay (INAU)" for the original "Instituto Nacional del Menor", the renaming art. 223 orders in the text; neither is committed as a change. Where an amended article's original says INAME, the INAU wording appears in its first recorded change.
- CNA, dotted articles: Artículo 132.6: not in IMPO's original of art. 132 (leyes-originales/17823-2004/132); first worded by Ley Nº 19.092 art. 2, read as added by it; Artículo 133.1: not in IMPO's original of art. 133 (leyes-originales/17823-2004/133); first worded by Ley Nº 18.590 art. 3, read as added by it; Artículo 133.2: not in IMPO's original of art. 133 (leyes-originales/17823-2004/133); first worded by Ley Nº 18.590 art. 3, read as added by it.
- Batch 4 acts (corpus.d/70-batch4.json) are rebuilt by the code of batches 2 and 3 unchanged (batch2.build_one over impo_history.py, with batch 3's readings): each amended article starts from IMPO's original text, today's text is IMPO's consolidated text, intermediate texts are only those an amending law quotes or IMPO's notes determine, and each amending law is in force on the day its own vigencia article gives, else ten days after publication (Código Civil art. 1); a law shared with an earlier part has the same day there.
- Batch 4: legalize-dev/legalize-uy was checked as a faster source and not used for text: its 10,155 law commits are each a single "[bootstrap]" snapshot of IMPO's consolidated text taken in 2026, dated by the base law's publication, with IMPO's notes dropped, so it holds no earlier wording and names no amending law; its words equal IMPO's for the laws compared (Leyes 18.331, 16.060, 17.250: 620 of the 623 articles matched by label word for word, the other 3 only adding the signatories), and it has no file for the codes. Common Crawl (six 2026 crawls) holds some of IMPO's HTML pages (e.g. 206 URLs under codigo-rural/, many of them reference pages) but none of the JSON with notes that the rebuild reads. Every text here is IMPO's JSON, fetched live with its crawl delay.
- Ley 18.381: amended articles IMPO gives no TEXTO ORIGINAL link for start from IMPO's original text at leyes-originales/18381-2008/<n>: Artículo 9, Artículo 21.
- Ley 17.514: amended articles IMPO gives no TEXTO ORIGINAL link for start from IMPO's original text at leyes-originales/17514-2002/<n>: Artículo 9.
- Ley 19.580: amended articles IMPO gives no TEXTO ORIGINAL link for start from IMPO's original text at leyes-originales/19580-2017/<n>: Artículo 65, Artículo 79.
- Ley 19.580, article vigencia: Artículo 58: 2019-01-01 -> 2018-10-15 (Ley Nº 19.670 art. 290: "El presente artículo entrará en vigencia a partir de la promulgación"); Artículo 58: 2024-01-01 -> 2023-11-06 (Ley Nº 20.212 art. 512: "Lo dispuesto en este artículo entrará en vigencia a partir de la promulgación").
- Ley 19.574: amended articles IMPO gives no TEXTO ORIGINAL link for start from IMPO's original text at leyes-originales/19574-2017/<n>: Artículo 4, Artículo 59.

## What AI did and did not do

The fetch, parse and check scripts were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above, through code that anyone can rerun.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- A model (Claude) wrote fetch.py and parse.py and chose the sources. It wrote no legal text: every unit is parsed from IMPO or Parlamento bytes in the cache.
- A model (Claude) wrote batch2/fetch2.py and batch2/batch2.py and read the vigencia articles listed in decisions. It wrote no legal text: every unit is parsed from IMPO bytes in the cache, apart from the fixed placeholder sentence of the anachronism rule.
- A model (Claude) wrote batch3/fetch3.py and batch3/batch3.py (which reuse batch 2's code) and read the vigencia articles listed in decisions. It wrote no legal text: every unit is parsed from IMPO bytes in the cache, apart from the fixed placeholder sentence of the anachronism rule.
- A model (Claude) wrote batch4/fetch4.py and batch4/batch4.py (which reuse batches 2 and 3's code) and read the vigencia articles listed in decisions. It wrote no legal text: every unit is parsed from IMPO bytes in the cache, apart from the fixed placeholder sentence of the anachronism rule.
