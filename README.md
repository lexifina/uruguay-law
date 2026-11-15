# Uruguay: law history in git

The national law of Uruguay as a git history: one file per article, one commit per law (or plebiscite) on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every paragraph; `git log` lists every change to an article; picking a date gives the text in force that day.

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is Uruguay's national law, which global-law reads at `uruguay/national/acts/`.

**What is in it now:** the Constitution of 1967 with its four reforms by plebiscite, 13 codes (among them the Código Civil, the Código Penal and the Código General del Proceso) and 255 laws and decree-laws, each from its first version or its entry into force to today; and 761 more laws as their current text only. That is 1,030 acts with 1,997 versions in force from 1866 to 2026; 10 more versions, due to take effect on 1 January 2027 (Ley 20.531), are on the `futuro` branch. [`data/versions.json`](data/versions.json) lists every act with the day each version took effect; [`data/laws.csv`](data/laws.csv) lists the 1,278 norms the record names, with their dates.

Each act is a folder by kind, year and number, with one file per article: `ley/2008/18331/` is the Ley Nº 18.331 de Protección de Datos Personales, `decreto-ley/1974/14219/` a decree-law, `code/codigo-civil/art-1700.md` art. 1700 of the Código Civil, and `constitution/constitucion/art-067.md` art. 67 of the Constitution. [`data/paths.json`](data/paths.json) maps each act id to its folder, and each folder's `README.md` lists its provisions and when each changed.

The text is in Spanish, as IMPO publishes it (and the Parlamento, for earlier texts of the Constitution).

## Questions as git commands

| Question | Command |
| --- | --- |
| Every change to art. 67 of the Constitution | `git log -p --follow --word-diff -- constitution/constitucion/art-067.md` |
| Which reform wrote each paragraph of art. 67? | `git blame constitution/constitucion/art-067.md` |
| Every version of the Constitution, with the day each took effect | `git log --author=impo.invalid --format="%h %(trailers:key=In-force,valueonly,separator=) %an" -- constitution/constitucion constitucion` |
| Art. 67 as in force on 1 January 1990 | `python tools/on.py 1990-01-01 constitucion 67` |

The acts moved to these folders on 10 November 2026: `git log` needs `--follow` for one file, or the old folder name beside the new one; `git blame` and `tools/on.py` follow the move.

**Outside git**, we also host this record publicly, for free:

- **[Ask Claude about Uruguayan law](https://global-law.lexifina.com/v1/try_claude?country=uruguay)**: opens Claude with a first question ready.
- **[Ask ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=uruguay)**: the same question in ChatGPT.
- **[Call the API in your browser](https://global-law.lexifina.com/v1/search_law?query=licencia+anual&jurisdictions=uruguay)**: a search of Uruguayan law for "licencia anual", returned as JSON. See the [documentation here](https://lexifina.com/api/global-law).

Both assistants read the record through the free Global law connector (MCP, `https://global-law.lexifina.com/mcp`); the first time, the chat gives you the link that adds it. Ask in Spanish or in English.

**Host it yourself easily.** All it takes is git and Python, and the tools run on your machine:

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add uruguay/national/acts
python3 tools/law.py show 2026-01-01 uruguay/national/acts/constitution/constitucion/art-067.md
```

Opened in Claude Code, Cursor, VS Code or Codex, the clone also starts a local MCP server with the same tools ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Dates

Each commit is dated at noon, America/Montevideo, on the day the change took effect, and carries it in its `In-force:` trailer:

- a law's own vigencia clause decides; without one, Código Civil art. 1 makes it binding ten days after its publication. No change is dated before its law was promulgated and published: where a law names an earlier day, it is dated ten days after publication (Ley 18.719, published 5 January 2011, "regirá a partir del 1° de enero de 2011": 15 January 2011);
- the Constitution took effect on 15 February 1967 and the 1989 reform on 1 May 1990, as their transitional provisions say; the 1994, 1996 and 2004 reforms took effect when the Corte Electoral proclaimed the result, which no source dates, so they are dated on the plebiscite day;
- a current-text law is dated by the day the last law IMPO's notes name took effect (458 laws), or by the last change date IMPO gives or its promulgation (303 laws), still to be corrected to the day it took effect;
- git cannot store dates before 1970, so the 365 earlier commits are dated from 1970-01-01, with the real day in `In-force:`. Ask for a date with `tools/on.py`, not `git log --before`.

Each change is credited to the law, decree-law or plebiscite that made it, at an address that cannot exist (`ley-18719@impo.invalid`, `plebiscito-1996-12-08@impo.invalid`), and only as IMPO's notes on that article name it. A first version that is not the text as enacted, such as the current text of the 761 laws, is credited to the publisher, IMPO, as the "oldest version available"; the committer is Lexifina.

## How it is checked

- Each version of the Constitution has the words of the Parlamento's edition of that year, apart from about 40 units where IMPO's and the Parlamento's transcriptions differ ("aun"/"aún"), and the units each reform changed are exactly those IMPO's notes give to that plebiscite (2, 1, 34 and 3); [`data/verification.json`](data/verification.json) lists both.
- Today's text of every act is IMPO's consolidated text, unit for unit; an earlier text is taken only from a source (IMPO's original text of a law, or the wording an amending law quotes). Every exception is in [`REPRODUCE.md`](REPRODUCE.md).
- `tools/check_repo.py` reads every version back from git on the day it took effect and on the day before; both must match the corpus, whose sha256 is in `data/corpus.sha256`. `REPRODUCE.md` records that no second build has been compared yet.
- History is append-only (`tools/append.py`): no merge commits on `main`, no commit dates that go backwards, nothing dated in the future, and every commit's trailers parse.

## What it does not show

- **Most national law.** These are 1,030 laws, codes and decree-laws; decrees of the Poder Ejecutivo, departmental law and case law are not here.
- **Earlier versions of the 761 current-text laws**, which have one version each.
- **Changes before an act's first version or not in IMPO's notes**: the Código Civil before its 1994 re-edition (Ley 16.603), the constitutions before 1967, and the Código Penal between 1934 and 1969, where IMPO names no amending law.
- **Texts no source gives.** Where no source gives the text between two amending laws, the change shows on the next day whose text is known; a few items whose start cannot be placed are left out, each listed in `REPRODUCE.md`.
- **Headings and acts IMPO only points from**: headings of books, titles and chapters are not kept, and the Ley de Urgente Consideración (Ley 19.889) is not an act of its own; its changes are in the laws it amended.

## Sources

| Source | Kind | Past versions | Notes |
| --- | --- | --- | --- |
| [IMPO, Base de datos de normativa](https://www.impo.com.uy/bases) (Dirección Nacional de Impresiones y Publicaciones Oficiales) | Official database of national legislation | no: today's consolidated text, and the original text of each amended article | Its notes name the law behind each change ("redacción dada por", "agregado/s por") |
| [Parlamento del Uruguay, Constitución](https://parlamento.gub.uy/documentosyleyes/constitucion) | The Constitution | yes, the editions of 1967, 1989, 1994, 1997 and 2004 | Read through Internet Archive captures of its pages |

## Licence

See [`LICENSE`](LICENSE). The legal texts are the official texts published by IMPO and the Parlamento del Uruguay, to which Lexifina makes no claim; IMPO's texts and data are used under the [Licencia de Datos Abiertos – Uruguay, version 0.1](https://www.impo.com.uy/wp_impo/wp-content/uploads/2018/06/licencia-de-datos-abiertos.pdf), and were changed: assembled into a dated version history, with formatting normalised. The history, commit messages, tables and tools are CC0 1.0.

No AI model wrote, translated or corrected legal text, and none runs at build time. Claude Code running Claude Opus 5.5 wrote the scripts and read the laws' vigencia articles behind the dates listed in [`REPRODUCE.md`](REPRODUCE.md).

## En español

Historia del derecho nacional uruguayo en git: un archivo por artículo y un commit por ley (o plebiscito), fechado el día en que entró en vigencia y firmado por la norma que hizo el cambio. Contiene la Constitución de 1967 con sus cuatro reformas plebiscitadas, 13 códigos y 255 leyes y decretos-ley con su historia, y 761 leyes más solo con su texto vigente; las versiones que aún no rigen están en la rama `futuro`. Texto vigente en una fecha: `python tools/on.py 1990-01-01 constitucion 67`. Fuentes: IMPO (Licencia de Datos Abiertos – Uruguay) y el Parlamento del Uruguay. Ningún modelo de IA escribió texto legal.

## More

From [lexifina/global-law](https://github.com/lexifina/global-law):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): every feature, and what every corpus must support (`git blame`, `law.py`, the MCP tools)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): questions and answers · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): proposing changes · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): the MCP server · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): how it was built · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): how current each corpus is · [Monitoring](https://github.com/lexifina/global-law/tree/main/monitoring): whether updates are running · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): how each official source is watched for changes
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): how fast the tools are, measured
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): charts and bridges across the world's law
- [Vulnerabilities](https://github.com/lexifina/global-law/tree/main/vulnerabilities): mistakes in legislation as published
