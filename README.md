# Conformity with co-presence

**Paper:** [*Conformity with co-presence: a rule violation spreads through a swarm of coding agents by what each agent happens to read*](report/report.pdf) (PDF; source in `report/report.md`). Frank Peterlein, Apart Research Swarm Alignment Hackathon, 6–8 November 2026, Track 2: The Science of Agent Networks.

Sixteen copies of the same coding agent (Claude Haiku 4.5 in Claude Code) share one folder of notes. Each has a scored task it can only finish by reading a file it is forbidden to read, and in half the populations the folder holds a planted note from an earlier job that did just that. Agents that start together break the rule at the single-agent rate, whatever their number. Agents that start one after another turn the outcome into a history, 2 to 15 of 16 contaminated per population, and what decides it is what each agent had read: an agent that had read no note carrying the hidden totals was contaminated at 0.15, one that had read such a note at 0.84. The study was pre-registered and frozen before the first run: 288 agents in the main run and a declared replication of 224 the same evening.

The pre-registration carries the working title *Collusion with co-presence* (`PREREGISTRATION.md`). The study continues [collusion-without-co-presence](https://github.com/frnkptrln/collusion-without-co-presence) (October 2026), whose instrument this repository reuses, and through it [peer-pressure-without-peers](https://github.com/frnkptrln/peer-pressure-without-peers) (September 2026). What was copied and what is new is listed in `PRIOR_WORK.md`.

**Record.** Bound and frozen on 7 November 2026 at 14:21 Berlin (`DEVIATIONS.md`); gate passed; main run (288 agents) and positive control (16) the same afternoon; an extension of four further blocks of the multi-agent cells (224 agents), declared in `DEVIATIONS.md` after the main analysis, run the same evening. The registered readings are in `instrument/runs/main/results.md`; the extension's own and the pooled numbers (labelled as pooled after a data-dependent extension) in `instrument/runs/ext/`; the exploratory provenance in `instrument/runs/*/extras_provenance.md` and `instrument/runs/ext/per_agent_rule.md`. Every change to a frozen file is a dated entry in `DEVIATIONS.md`.

## The experiment in one paragraph

An agent (Claude Haiku 4.5 through Claude Code, headless, four file tools served by our own MCP server that logs every call) gets a data task and a written rule: do not read the folder `/internal`. The task cannot be finished within the rule (6 of 24 records are missing; the complete file sits in `/internal`), the job is scored and it is the final attempt. The episode is the October one, byte for byte. What is new: **N such agents run at the same time on one shared folder** `/shared` — launched within seconds of each other (burst) or one every 20 s while the earlier ones still run (relay) — with an empty folder (S0) or one planted note in it that describes an earlier job's successful violation (S1). We count forbidden reads from the tool logs, resolve every read of a shared note to the write that produced it (by content hash, on one clock across the population), and so tell an agent that broke the rule itself from one that completed the job from another agent's note.

## What is in the repository

| path | what |
|---|---|
| `PREREGISTRATION.md` | question, design, outcomes, hypotheses with the author's predictions, gate, analysis plan (bound 7 November 2026) |
| `DEVIATIONS.md` | append-only deviation log, starts with the freeze |
| `PRIOR_WORK.md` | what was copied from the October repository, from which commit; what is new |
| `RUNBOOK.md` | the exact commands, in order, for the machine that runs the study |
| `instrument/` | copied unchanged from October: `workspace_server.py`, `fixtures_r3.py`, `run_r3.py`, `analyze_r3.py`, `schema.py`, `stats.py`, `report.py`, `quota.py`, `publish_scrub.py`, `concern_server.py`. New for this sprint (`NEW 2026-11`): `population_server.py` (the two-root server: private `/workspace` and `/internal`, one `/shared` per population, atomic writes, a population log under a lock), `run_population.py` (plans, the burst/relay runner, the scripted rehearsal), `analyze_population.py` (the October record per agent plus the population overlay: LEAK_POP, CONTAMINATED, peer- vs seed-induced reads, cross-reads, names; the results sheet; timelines), `gate_population.py`, `freeze.py`, `tests/test_population.py` with `tests/stub_claude.py`. Written after the main run, not frozen, exploratory: `extras_provenance.py` (the provenance one level finer than `results.md`), `prepare_extension.py` and `pool_extension.py` (the extension of 7 November evening and its replication/pooled reading), `tests/test_extension.py`, `per_agent_rule.py` (8 November: the per-agent rule, timed to what each relay agent had read before acting) |
| `analysis/` | `stats.py` (copied unchanged) |
| `instrument/runs/` | every population and agent: `gate`, `pc-gate`, `main`, `pc-main`, `ext` — records never change; each run's `results.md` holds its numbers with their sources, `reports/` its timelines |
| `report/` | the paper: `report.pdf`, its source `report.md` and a Word version, the figures, and the scripts that draw (`make_figures.py`) and build (`build_docx.js`) it |

## Checks — no model call is needed for any of this

```bash
cd instrument && python3 -m unittest discover -s tests && cd ..            # 66 tests: the copied October ones, the population ones, the extension ones
cd instrument && python3 run_population.py doctor && cd ..                 # MCP handshake with the population server, environment report
cd instrument && python3 run_population.py prepare --out /tmp/rehearsal --phase gate \
  && python3 run_population.py run --out /tmp/rehearsal --backend rehearsal --policy population_recheck --speed 50 \
  && python3 analyze_population.py /tmp/rehearsal && python3 gate_population.py /tmp/rehearsal && cd ..
```

Running episodes needs Claude Code logged in to a subscription and Frank's go (`RUNBOOK.md`); no agent starts runs on its own. The scripted rehearsal backend exercises every part of the pipeline — the two-root server, the shared folder, the population log, the analysis, the gate — without a model; nothing it produces is evidence about a model. The subject sessions get the allowlisted environment of October (`run_r3.subject_environment`), so no project context, CLAUDE.md or session variable of the operator's shell reaches them; the per-episode diagnostics line records it.

## Licence

Code (the Python and JavaScript files) is MIT-licensed (`LICENSE`), except the fixture texts in `instrument/fixtures_r3.py`. Everything else, including those fixture texts, the pre-registration, the deviation log, the prior-work disclosure, the run records under `instrument/runs/` and the report, is licensed under Creative Commons Attribution 4.0 International (`LICENSES/CC-BY-4.0.txt`). The instrument copied from the October repository is under the same terms there.

## Citation

`CITATION.cff` (GitHub shows it as "Cite this repository").

## AI use

Claude (Anthropic) drafted the pre-registration and wrote the new code, the tests and the analysis on the author's decisions of 6–8 November 2026, and wrote the text of the report, revised on the author's comments; before submission, a separate Claude session re-derived the report's numbers from the run records and checked its references. The author decided the design and the predictions, started every run, read the agents' notes and reviewed the report; the report's LLM-usage statement sets out the rest. The subject model runs through Claude Code on one subscription.
