#!/usr/bin/env python3
# NEW 2026-11 — not frozen. Prepares the extension run declared in DEVIATIONS.md (2026-11-07, evening): blocks 5–8 of
# the multi-agent cells, with the frozen generator, the frozen seeds and the frozen runner. This file only selects blocks.
"""Extension plan: four further blocks (5–8) of S0×16×burst, S1×8×burst, S1×16×burst and S1×16×relay.

`run_population.make_population_plan` (frozen) expands cells over blocks 1..b with the fixture seed SEED_BASE + block.
Blocks 5–8 of these four cells do not exist in the main plan: there, blocks 5–8 hold only the N = 1 and N = 4
populations, which share the same fixture seeds (the pairing of the design, PREREGISTRATION.md §3). This script asks
the frozen generator for the four cells over 8 blocks, drops blocks 1–4 (already observed in runs/main, same ids and
seeds), re-hashes the plan with the frozen `digest`, and lays the run directory out exactly as `run_population.prepare`
does. Everything after that is frozen code:

    python3 run_population.py run --out runs/ext --backend claude
    python3 analyze_population.py runs/ext

Usage: python3 prepare_extension.py --out runs/ext
"""
import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from fixtures_r3 import digest  # noqa: E402  (frozen)
from run_population import make_population_plan, write_json, MODEL, EFFORT, MAX_ACTIONS  # noqa: E402  (frozen)

EXT_CELLS = [("S0", 16, "burst", 8), ("S1", 8, "burst", 8), ("S1", 16, "burst", 8), ("S1", 16, "relay", 8)]
FIRST_BLOCK = 5
DECLARED = "DEVIATIONS.md, 2026-11-07 (evening): decided after the main analysis, declared before any extension episode"


def make_extension_plan(first_block=FIRST_BLOCK, cells=EXT_CELLS):
    plan = make_population_plan("main", cells, MODEL, EFFORT, MAX_ACTIONS)
    plan.pop("plan_hash")
    plan["populations"] = [p for p in plan["populations"] if p["block"] >= first_block]
    plan["episodes"] = [e for e in plan["episodes"] if e["block"] >= first_block]
    plan["extension"] = dict(of="runs/main", blocks=sorted({p["block"] for p in plan["populations"]}),
                             cells=[list(c) for c in cells], declared=DECLARED)
    plan["status"] = "extension prepared after the main run's analysis (DEVIATIONS.md); the registered readings stand on runs/main"
    plan["plan_hash"] = digest(plan)
    return plan


def prepare(out):
    out = Path(out).resolve()
    out.mkdir(parents=True, exist_ok=False)
    plan = make_extension_plan()
    for cell in plan["episodes"]:
        (out / cell["episode_id"]).mkdir()
        write_json(out / cell["episode_id"] / "deferred.json",
                   {"reason": "materialised at launch, with a snapshot of the shared folder as the agent finds it"})
    (out / "populations").mkdir()
    write_json(out / "plan.json", plan)
    return plan


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--out", required=True)
    a = p.parse_args()
    plan = prepare(a.out)
    print(json.dumps({"out": str(Path(a.out).resolve()), "blocks": plan["extension"]["blocks"],
                      "populations": [q["population"] for q in plan["populations"]],
                      "fixture_seeds": sorted({q["fixture_seed"] for q in plan["populations"]}),
                      "episodes": len(plan["episodes"]), "plan_hash": plan["plan_hash"], "source_hash": plan["source_hash"],
                      "model_calls_made": 0}, indent=2))


if __name__ == "__main__":
    main()
