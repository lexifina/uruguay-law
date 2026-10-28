# Uruguay: law history in git

The law of Uruguay as a git history: one file per provision, one commit per law (or plebiscite) on the day it took effect, and the law that made each change as the commit's author. `git blame` names the reform behind every paragraph; `git log` lists every change to an article; checking out a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `uy/`.

*En español: [más abajo](#en-español).*

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitucion/` | Constitución de la República Oriental del Uruguay (1967) | 5 | From its entry into force (15 February 1967) through the reforms approved by plebiscite in 1989, 1994, 1996 and 2004, to today |
| `codigo-civil/` | Código Civil, as approved by Ley Nº 16.603 (1994) | 18 | From the re-edition approved by Ley 16.603 (in force 1 December 1994) through 20 amending laws (Leyes 16.719 to 20.446), to today. The code of 1868 and its changes before 1994 are not included |
| `ley-18331/` | Ley Nº 18.331 de Protección de Datos Personales (2008) | 7 | As enacted (in force 28 August 2008), then every amending law IMPO names: Leyes 18.719, 18.996, 19.355, 19.670, 19.924 and 20.075, to today |

The articles are `<act>/art-NNN.md` (`art-009-bis.md` for Artículo 9 BIS; four digits in the Código Civil, `art-1782.md`); the Constitution's Disposiciones Transitorias y Especiales are `constitucion/disp-trans-<letter>.md` (`-prima` for V'), Z'), `-segunda` for Z")). The per-act `README.md` lists every provision, how often it changed and when.

**How a law's history is rebuilt.** IMPO publishes only today's text of a law, but under each amended article it names the amending law and article ("Inciso 2º) redacción dada por: Ley Nº 18.719 de 27/12/2010 artículo 152", "Literal Ñ) agregado/s por: …") and links the article as originally published ("TEXTO ORIGINAL"). So the first version of each amended article is IMPO's original text, and every later version is today's text. Where one article was amended by two laws on different days, the text in between is taken only from a source: the wording the earlier amending law quotes (IMPO's original of that law), or today's text without an item that IMPO says the later law added. Every step and how it was rebuilt is listed in [`data/verification.json`](data/verification.json). Each amending law takes effect on the day its own vigencia article gives (Leyes 18.719, 18.996, 19.355, 19.670, 19.924 and 20.075 each say "regirá a partir del 1° de enero de …"), or else ten days after publication (Código Civil art. 1).

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What did art. 67 of the Constitution say on 1 January 1990? | `python tools/on.py 1990-01-01 constitucion 67` |
| The same, naming the reform behind the text | `python tools/on.py --law 1990-01-01 constitucion 67` |
| The same, with raw git (bash) | `git show $(git rev-list -1 --before="1990-01-01T23:59:59Z" main -- constitucion/art-067.md):constitucion/art-067.md` |
| Which reform wrote each paragraph of art. 77? | `git blame constitucion/art-077.md` |
| Every change to art. 47, word by word | `git log -p --word-diff constitucion/art-047.md` |
| Every reform in the record, in order | `git log --reverse --format="%ad %an" --date=short main` |
| Everything one reform changed | `git show law/plebiscito-1996-12-08` (tags `law/<key>` mark each law's commit) |
| The whole Constitution on a date | `python tools/on.py 1995-06-01 constitucion` |
| The Constitution as of a version | `git show constitucion/1990-05-01` (tags `<act>/<in-force day>`) |
| Laws passed but not yet in force | `git log main..futuro` (none today) |

After a rebuild, refresh tags with `git fetch --force --tags`: a plain fetch keeps stale tags.

## Dates

- Each commit is dated at **noon, America/Montevideo, on the day the change took effect**. The plebiscite day is the `Enacted:` trailer, and the in-force day is in `In-force:`, which the tools read.
- **1967.** The Constitution was approved by plebiscite on 27 November 1966. Its transitional provision A), as the Parlamento prints the 1967 text, put it in force on 15 February 1967 (Secciones VIII to XI and XVI from 1 March 1967, provision B). Git cannot store dates before 1970, so this first commit is dated 1 January 1970; its real day is in the `In-force:` trailer, which `tools/on.py` reads.
- **1989 reform** (plebiscite of 26 November 1989: art. 67 incisos 2 and 3, provision V)). Provision V) puts the reform of art. 67 in force on 1 May 1990, and that is the version's day.
- **1994, 1996 and 2004 reforms.** A reform approved by plebiscite takes effect when the Corte Electoral proclaims the result (the 1996 text of provision A)). No source we read dates those proclamations, so **these versions are dated on the plebiscite day** (27 November 1994, 8 December 1996, 31 October 2004), and each commit says so. The Parlamento files the 1994 and 1996 texts as "vigencia 1995" and "vigencia 1997"; Decreto 435/004 of 13 December 2004 (IMPO) states that the 2004 reform was then in force. For a day between a plebiscite and its proclamation, the history shows the new text one step early.
- **Default rule for laws.** Código Civil art. 1: laws are binding by their promulgation by the Poder Ejecutivo, which is deemed known ten days after it is verified in the capital. A law's own vigencia clause overrides it. Ley 18.331 took effect on 28 August 2008, ten days after its publication on 18 August 2008 (it has no vigencia clause). Leyes 18.719 (enacted 27 December 2010, published 5 January 2011) and the other budget laws take effect on 1 January by their own vigencia article, so a change can take effect a few days before the law was published; the `Published:` trailer shows it.
- `--before="YYYY-MM-DD"` alone uses your clock's time of day, so a change that took effect that day may be missed before noon. Use `T23:59:59Z` as above, or the tool.

## How it is checked

- **Every version is the Parlamento's own dated edition.** The Parlamento publishes the Constitution as approved in 1966 and as amended in 1989, 1994, 1996 and 2004. Each version's units have exactly the words of that edition, except units where the Parlamento's and IMPO's transcriptions differ in a few words (see below). [`data/verification.json`](data/verification.json) lists every such unit and every word that differs.
- **The reforms agree between two publishers.** The units each reform changed come from comparing consecutive Parlamento editions word by word. The parser stops unless they are exactly the units that IMPO's own notes ("La redacción de este artículo fue dada por la Reforma Constitucional, aprobada por plebiscito de fecha …", "El inciso final fue agregado por …") assign to that plebiscite. All four reforms match: 2 units (1989), 1 (1994), 34 (1996), 3 (2004).
- **Today's text is IMPO's consolidated text**, unit for unit, for every act.
- **Ley 18.331 and the Código Civil:** the first version of each amended article is IMPO's original text of the law; every change step, the laws credited and the words that changed are in `data/verification.json`.
- Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`), and must match `corpus.json`: 0 mismatches. No merge commits on `main`, commit dates never go backwards, nothing is dated in the future, and every commit's trailers parse.
- The repository is rebuilt from the same data a second time and gives identical hashes. Details in [`REPRODUCE.md`](REPRODUCE.md).

## What "author" means

The author of a commit is the reform or law that made the change, with an e-mail address that cannot exist (`plebiscito-1996-12-08@impo.invalid`, `ley-18719@impo.invalid`), so `git blame` and `git log --author` name them. The committer is always Lexifina.

- **Credits come only from the sources.** A unit of the Constitution is credited to a reform only when the Parlamento's editions show it changing at that reform and IMPO's note on the unit names that plebiscite. An article of a law is credited only to the laws IMPO's notes on that article name. There are no unexplained changes.
- **Transcription differences are not changes.** IMPO and the Parlamento transcribe the same text with small differences in about 40 units ("aun"/"aún", "hayan"/"haya", "presupuesto"/"presupuestos", ordinals in words or figures). A unit uses IMPO's text from its last reform on (throughout, if no reform touched it), and the Parlamento's text only before that, so these differences never show as changes. Inside a unit a reform rewrote, the reform's commit can also show such differences; `git log -p --word-diff` shows them.
- **Incisos added later.** Where a reform added incisos to an article (arts. 47, 67, 188), the earlier text is IMPO's text without those incisos, which has exactly the Parlamento's earlier words.
- The Parlamento's 2004 edition also changes words in arts. 7, 135, 197, 275 and 313 that no reform and no IMPO note explains; IMPO's text agrees with the earlier editions, so they are not changes here.
- Blame credits whole lines (one paragraph or item per line).

## What it does not show

- The Código Civil before 1 December 1994. Its first commit is "oldest version available": the re-edition approved by Ley Nº 16.603, which IMPO consolidates.
- A few intermediate texts no source gives (Código Civil arts. 98 and 1782, listed as unresolved in `data/verification.json`): there the change is shown on the next day whose text is known, credited to every law in between, so for the days between those laws the file shows the older text.
- The Constitutions before 1967 (1830, 1918, 1934, 1942, 1952). The Parlamento publishes them, but this repository starts with the 1967 Constitution, which is a new text, not an amendment.
- Plebiscites that rejected a reform. They changed no words and are not recorded yet.
- The exact proclamation day of the 1994, 1996 and 2004 reforms (see Dates).
- Section and chapter headings, which are not units. IMPO's headings are not part of the article text.
- Changes to a law that IMPO's notes do not record. The history of a law is only as complete as IMPO's notes.
- Interpretative laws (for example Ley 19.355 art. 84 on Ley 18.331 arts. 9 and 17), which change no words.

Only the texts published by the Parlamento and IMPO are authoritative. This repository is a research aid, not legal advice.

## How it is built

`tools/fetch.py` downloads every source into a cache: IMPO's JSON (`?json=true`) for the consolidated Constitution, its transitional provisions and each law, and every original article and amending article their notes point to, at most one request every 10 seconds as IMPO's robots.txt asks, and the Parlamento's dated editions through pinned Wayback Machine captures, because parlamento.gub.uy refuses this machine. `tools/parse.py` reads only that cache and writes `corpus.json`; `tools/build.py` writes this repository from it. The same cache gives the same bytes and the same commit hashes. A model (Claude) wrote the scripts; it wrote no legal text. No model runs when the history is built.

## Sources

| Source | What it gives | Dated versions | Names the amending act | Access |
| --- | --- | --- | --- | --- |
| [IMPO, Base de datos de normativa](https://www.impo.com.uy/bases) | Consolidated text in force of the Constitution, codes and laws | No (the original text of an amended article, for laws) | Yes, per article ("redacción dada por", "agregado por") | JSON (`?json=true`); robots.txt Crawl-Delay 10 |
| [Parlamento, Constitución de la República](https://parlamento.gub.uy/documentosyleyes/constitucion) | The Constitution as of 1967, 1989, 1994, 1997 and 2004, and the earlier constitutions | Yes | Footnotes on transitional provisions | HTML; 403 from this machine, read through Wayback captures pinned in `tools/fetch.py` |

Research guides that cover every country: [GlobaLex](https://www.nyulawglobal.org/globalex/) and the [Law Library of Congress Guide to Law Online](https://www.loc.gov/research-centers/law-library-of-congress/researcher-resources/guide-to-law-online/).

## Licence

The texts are the official texts published by IMPO (www.impo.com.uy/bases) and the Parlamento del Uruguay (parlamento.gub.uy), cited as the source of every version. We found no licence statement on either site and make no claim to the legal text. The history, commit messages, tables and tools are released under [CC0 1.0](LICENSE).

---

## En español

La Constitución de la República Oriental del Uruguay como historia git: un archivo por artículo o disposición transitoria, y un commit por cada reforma plebiscitada (1989, 1994, 1996, 2004), con la reforma como autor y fechado el día en que entró en vigencia.

- **Fuentes:** las ediciones fechadas de la Constitución que publica el Parlamento (1967, 1989, 1994, 1997, 2004) y el texto actualizado de IMPO. Las unidades que cambió cada reforma coinciden exactamente con las notas de IMPO ("La redacción de este artículo fue dada por la Reforma Constitucional…").
- **Fechas:** la Constitución de 1967 rige desde el 15 de febrero de 1967; la reforma de 1989 desde el 1º de mayo de 1990 (disposición V). Las reformas de 1994, 1996 y 2004 rigen desde la proclamación de la Corte Electoral, que no hemos podido fechar con una fuente oficial: esas versiones llevan la fecha del plebiscito.
- **Diferencias de transcripción** entre IMPO y el Parlamento (por ejemplo "aun"/"aún") no se registran como cambios.
- **Leyes** (Ley Nº 18.331 de Protección de Datos Personales): la primera versión de cada artículo modificado es el texto original que publica IMPO, y cada cambio se atribuye a la ley que nombran las notas de IMPO ("redacción dada por", "agregado/s por"), en la fecha de vigencia que fija la propia ley o, en su defecto, diez días después de su publicación (Código Civil, art. 1).

Solo los textos del Parlamento y de IMPO son oficiales.
