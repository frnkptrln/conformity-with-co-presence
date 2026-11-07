# DEVIATIONS — collusion with co-presence (append-only; nothing above an entry is edited after it)

Not frozen yet. The freeze line (date, `instrument/MANIFEST.sha256.json` hash, bound `PREREGISTRATION.md` hash, who decided, from where it was executed) is written here by the author at the freeze; from then on every change to a frozen file is a dated entry below: date, what changed, why, who decided, treatment of already-collected data.

## Freeze — 2026-11-07 13:21:47 UTC (14:21 Berlin)

- `PREREGISTRATION.md` bound (Frank's predictions in §6, each with its operational reading) and frozen with the instrument: `instrument/MANIFEST.sha256.json` sha256 `05b5a9f649a6c8203d4e89673f11d87c186554fec884535f4703d2ff06db1895`, covering 16 files; bound `PREREGISTRATION.md` sha256 `f6bb0ab757802bfa28b6dfc733c50df3f59e6c987a1c81a244699fba7e4abbe4`.
- Decided by Frank Peterlein; `freeze.py` executed by him on his MacBook Pro (the machine that runs every episode); `freeze.py --check` reports no drift. No gate or main episode exists before this line.

## Extension — 2026-11-07 16:18 UTC (17:18 Berlin): four further blocks of the multi-agent cells, decided after the main analysis, declared before any extension episode

- **What.** Blocks 5–8 of the cells S0×16×burst, S1×8×burst, S1×16×burst and S1×16×relay — 16 populations, 224 agents — under `instrument/runs/ext`. Fixture seeds are the frozen generator's for blocks 5–8 (`1_000_000 + b`, shared with the N = 1 and N = 4 populations of those blocks in `runs/main`: the pairing of §3). Prepared by the non-frozen `instrument/prepare_extension.py`, which calls the frozen `make_population_plan` with these four cells over eight blocks and drops blocks 1–4; run by the frozen `run_population.py run`, analysed by the frozen `analyze_population.py`. No frozen file changes (`freeze.py --check` before and after).
- **Why.** The registered design has 4 blocks per 16-agent cell; the paired H2 test cannot fall below p = 0.125 and came out 0.250 (relay 0.69 vs burst 0.30 on the main run). The decision to extend was taken after seeing these results: a data-dependent extension, and it is reported as one.
- **Treatment.** The registered readings of §6 stand on `runs/main` alone and are reported as such. The extension is reported (a) on its own as a replication under the same reading rules — H2 paired over its four blocks, H3 for N = 8 and 16, H4 over its four relay populations, H0 over its S0 populations; H1 needs the single-agent cell, which exists only in the main run — and (b) pooled with the main run, labelled "pooled after a data-dependent extension" wherever it appears. Gate, pilots and positive control stay unpooled. No extension population is ever rerun; no record of the main run changes.
- Decided by Frank („wir könnten das auch einfach noch machen, ist ja noch zeit", 17:14 Berlin), prepared by Claude, executed by Frank on his MacBook.
