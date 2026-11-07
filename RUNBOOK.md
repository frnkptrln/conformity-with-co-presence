# Runbook — the commands, in order, on the machine that runs the study

Everything runs from the repository root unless a line says otherwise. Every step that calls a model is marked **(model)**; the author starts those. Expected durations are for Haiku 4.5 episodes of 30–90 s on a laptop that can hold 16 Claude Code processes at once.

## 0. Checks — no model

```bash
cd instrument
python3 -m unittest discover -s tests                 # 62 tests, about 40 s
python3 run_population.py doctor                      # claude_installed true, claude_version, the population server's tools, env report
python3 run_population.py prepare --out /tmp/rehearsal --phase gate
python3 run_population.py run --out /tmp/rehearsal --backend rehearsal --policy population_recheck --speed 50
python3 analyze_population.py /tmp/rehearsal          # needs matplotlib for the timelines; add --no-figures without it
python3 gate_population.py /tmp/rehearsal             # PASS on the rehearsal
cd ..
```

`claude auth status` should say logged in with the subscription. If `pip3 install matplotlib` is not wanted, every analysis call takes `--no-figures`.

## 1. Bind and freeze — no model

Replace every `[FRANK]` in `PREREGISTRATION.md` §6 with your own prediction (a number or a range per line; "I adopt the draft" is a valid entry, written out). Then:

```bash
python3 instrument/freeze.py                          # writes instrument/MANIFEST.sha256.json; refuses while a [FRANK] remains
python3 instrument/freeze.py --check                  # no drift
```

Write the freeze line at the top of `DEVIATIONS.md` (the two hashes the freeze printed, the time, "decided by the author, executed on <machine>"). Commit.

## 2. Gate — (model), about 10 minutes, 48 + 4 episodes

```bash
cd instrument
python3 run_population.py prepare --out runs/gate --phase gate
python3 run_r3.py prepare --out runs/pc-gate --experiment E1 --phase gate --design pc --seed 170907 --model claude-haiku-4-5-20251001
python3 run_population.py run --out runs/gate --backend claude          # three populations of 16, one after another; prints one line per agent
python3 run_r3.py run --out runs/pc-gate --backend claude --limit 4
python3 analyze_population.py runs/gate
python3 analyze_r3.py runs/pc-gate --design pc
python3 gate_population.py runs/gate --pc runs/pc-gate                  # exit 0 PASS / 1 FAIL / 2 incomplete; read the JSON
python3 quota.py runs                                                   # five-hour and seven-day utilisation; no batch above 85 % / 80 %
cd ..
```

What to look at in the verdict: `decision`; `populations.<id>.median_duration_s` (the episode length under 16 concurrent processes), `launch_gaps_s` (should be about 1 s in the bursts, 20 s in the relay), `overlap` (relay: at least 8), `cross_reads`, `invalid` and `invalid_reasons` (rate-limit or transport errors would show here), `claude_code_versions`. A FAIL names the pre-registered fallback; it is a decision, then a DEVIATIONS entry, never a rerun of the gate under the same plan. Commit `instrument/runs/gate` and `pc-gate` as they are.

## 3. Main run — (model), 288 + 16 episodes

Order: the 56 populations in plan order (the plan interleaves the cells block by block), then the positive control. Wall time: about 56 × (episode length + launch spacing) — with 60-s episodes roughly 1.5 h for the populations (the relay populations take 5 min each), plus 20 min for the positive control. Run it in a terminal that stays open; the runner skips populations already finished and never reruns one, so an interrupted run is continued by the same command (the interrupted population is reported, counted invalid, never repeated).

```bash
cd instrument
python3 quota.py runs                                                   # before the batch
python3 run_population.py prepare --out runs/main --phase main
python3 run_population.py run --out runs/main --backend claude
python3 run_r3.py prepare --out runs/pc-main --experiment E1 --phase main --design pc --seed 170907 --model claude-haiku-4-5-20251001
python3 run_r3.py run --out runs/pc-main --backend claude --limit 16
python3 analyze_population.py runs/main
python3 analyze_r3.py runs/pc-main --design pc
python3 quota.py runs
cd ..
```

Commit the run directories as written (`instrument/runs/main`, `pc-main`). `results.md` in each run directory holds every number of the report with its source; `reports/timeline_*.png` the figures; `records.jsonl` and `populations.jsonl` the machine-readable records; `populations/<id>/population_events.jsonl` the one-clock log of a population; `populations/<id>/shared/notes/` the folder as the population left it.

## 4. Before publishing the records

```bash
python3 instrument/publish_scrub.py --help             # a redacted copy with the login e-mail replaced, if wanted (October left the records as written)
python3 instrument/freeze.py --check                   # still no drift; anything else is a DEVIATIONS entry
```
