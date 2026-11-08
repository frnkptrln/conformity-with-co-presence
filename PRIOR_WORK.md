# Prior work in this repository

The sprint's rule: building on existing work is allowed, new sprint work must be clearly identified, undisclosed prior work can disqualify. This file is that identification.

## Source

`frnkptrln/collusion-without-co-presence`, the instrument, pre-registration, run records and report of "Collusion without co-presence" (Apart Research AI Collusion Research Sprint, 23–25 October 2026), at commit `1fbb4f100d250384a6f7675fd3b810c276bf2587` (27 October 2026, the last commit before this sprint). That repository in turn copied its instrument from `frnkptrln/peer-pressure-without-peers@9b048f1` (September 2026) and changed it for the October design; each copied file's own first line says which. Licence of the source: code MIT; pre-registration, notes, fixtures and run records CC BY 4.0.

## Copied unchanged

Every file below carries, as a comment line at the top (after the shebang where there is one), `copied unchanged from collusion-without-co-presence@1fbb4f1 (prior work; …)`; apart from that line the files are byte-identical to the source (checked by removing the line and diffing).

| here | there |
|---|---|
| `instrument/workspace_server.py`, `fixtures_r3.py`, `run_r3.py`, `analyze_r3.py`, `schema.py`, `stats.py`, `report.py`, `quota.py`, `publish_scrub.py`, `concern_server.py` | `instrument/` |
| `instrument/tests/test_r3_harness.py`, `test_review_regressions.py`, `test_d4.py`, `test_d5.py` | `instrument/tests/` |
| `analysis/stats.py` | `analysis/` |
| `LICENSE`, `LICENSES/CC-BY-4.0.txt`, `.gitignore` | the same |

## Left out, and why

`instrument/gate.py`, `sprint_autorun.py`, `freeze.py`, `check_quotes.py`, `MANIFEST.sha256.json` and the tests `test_replacement.py`, `test_review_prefreeze.py`, `test_tools.py`, `test_figures_rehearsal.py`: the October runbook, its gate and its freeze are specific to the replacement design and are replaced here by `run_population.py`, `gate_population.py` and a new `freeze.py`. `analysis/schema.py`, `report.py`, `results_blocks.py`, `figures.py`, `coding_sheet.py`, `make_stub.py` and their tests: the October results sheet and figures; this study's sheet and timelines are `analyze_population.py`. `instrument/runs/`, `monitor/`, `report/`, `docs/`, `PREREGISTRATION.md`, `DEVIATIONS.md`: October's evidence, add-on study and texts stay in their own repository and are cited, not copied. The September and October run records are prior observations (PREREGISTRATION.md §2), never data of this study.

## New during the sprint (6–8 November 2026)

Everything else was written during the sprint, from the evening of 6 November: the question and the design, `PREREGISTRATION.md`, `instrument/population_server.py`, `run_population.py`, `analyze_population.py`, `gate_population.py`, `freeze.py`, `tests/test_population.py`, `tests/stub_claude.py`, `RUNBOOK.md`, this file, the README; then the binding and the freeze, the gate and main runs with their records under `instrument/runs/`, the analysis and the figures; after the main analysis (7 November, evening) the non-frozen `extras_provenance.py`, `prepare_extension.py`, `pool_extension.py`, `tests/test_extension.py` and the extension run `instrument/runs/ext`; then the report, and on 8 November, after an independent check of the draft, the non-frozen `per_agent_rule.py` (the per-agent rule, timed to what each relay agent had read before acting).
