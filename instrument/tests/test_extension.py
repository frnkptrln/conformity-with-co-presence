# NEW 2026-11 — tests for the non-frozen extension scripts (prepare_extension.py, pool_extension.py). No model call.
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))

from prepare_extension import make_extension_plan, prepare, EXT_CELLS, FIRST_BLOCK  # noqa: E402
from run_population import make_population_plan, load_plan, CELLS  # noqa: E402


class ExtensionPlan(unittest.TestCase):
    def test_blocks_cells_and_seeds(self):
        plan = make_extension_plan()
        blocks = sorted({p["block"] for p in plan["populations"]})
        self.assertEqual(blocks, [5, 6, 7, 8])
        self.assertEqual(len(plan["populations"]), 16)
        self.assertEqual(len(plan["episodes"]), 224)
        self.assertEqual(sorted({p["fixture_seed"] for p in plan["populations"]}), [1_000_005, 1_000_006, 1_000_007, 1_000_008])
        cells = {(p["arm"], p["n_agents"], p["timing"]) for p in plan["populations"]}
        self.assertEqual(cells, {(a, n, t) for a, n, t, _ in EXT_CELLS})
        for p in plan["populations"]:
            self.assertEqual(len(p["agents"]), p["n_agents"])
            self.assertEqual(p["spacing_s"], 20.0 if p["timing"] == "relay" else 1.0)

    def test_disjoint_from_main_and_paired_with_it(self):
        main = make_population_plan("main", CELLS["main"])
        ext = make_extension_plan()
        main_ids = {p["population"] for p in main["populations"]}
        ext_ids = {p["population"] for p in ext["populations"]}
        self.assertFalse(main_ids & ext_ids)
        self.assertFalse({e["episode_id"] for e in main["episodes"]} & {e["episode_id"] for e in ext["episodes"]})
        # the same block shares the fixture seed across both runs (the pairing of §3)
        main_seed = {p["block"]: p["fixture_seed"] for p in main["populations"]}
        for p in ext["populations"]:
            self.assertEqual(p["fixture_seed"], main_seed[p["block"]])
        # the extension's episodes are the frozen generator's: same fields, same handoff and rule hash
        self.assertEqual(ext["rule_sha256"], main["rule_sha256"])
        self.assertEqual(ext["handoff_text"], main["handoff_text"])
        self.assertEqual(set(ext["episodes"][0]) , set(main["episodes"][0]))

    def test_prepared_directory_loads_with_the_frozen_loader(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "ext"
            plan = prepare(out)
            loaded = load_plan(out)          # verifies plan hash and source hash exactly as the frozen runner does
            self.assertEqual(loaded["plan_hash"], plan["plan_hash"])
            self.assertEqual(loaded["extension"]["blocks"], [5, 6, 7, 8])
            self.assertTrue((out / "populations").is_dir())
            self.assertEqual(sum(1 for d in out.iterdir() if d.is_dir() and d.name != "populations"), 224)
            with self.assertRaises(FileExistsError):
                prepare(out)                 # never over an existing run directory


class PooledReport(unittest.TestCase):
    def test_pool_on_a_rehearsal(self):
        """prepare → rehearsal of two populations → frozen analysis → pooled report of the run with itself renamed."""
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "ext"
            prepare(out)
            env = dict(os.environ, PYTHONPATH=str(HERE))
            subprocess.run([sys.executable, str(HERE / "run_population.py"), "run", "--out", str(out), "--backend", "rehearsal",
                            "--policy", "population_recheck", "--speed", "50", "--limit", "2"], check=True, env=env,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run([sys.executable, str(HERE / "analyze_population.py"), str(out), "--no-figures"], check=True, env=env,
                           stdout=subprocess.DEVNULL)
            # a "main" stand-in: the same records with the population ids of blocks 1–4, so the id sets are disjoint
            main = Path(tmp) / "main"
            main.mkdir()
            for name in ("populations.jsonl", "records.jsonl"):
                text = (out / name).read_text(encoding="utf-8")
                for b in (5, 6, 7, 8):
                    text = text.replace(f"p0{b}-", f"p0{b - 4}-").replace(f'"block": {b},', f'"block": {b - 4},')
                (main / name).write_text(text, encoding="utf-8")
            res = subprocess.run([sys.executable, str(HERE / "pool_extension.py"), str(main), str(out)], check=True, env=env,
                                 capture_output=True, text=True)
            self.assertIn("Part A", res.stdout)
            self.assertIn("Part B", res.stdout)
            self.assertTrue((out / "pooled_with_main.md").exists())
            j = json.loads((out / "pooled_with_main.json").read_text(encoding="utf-8"))
            self.assertIn("pooled_H4", j)
            self.assertEqual(j["extension_validity"]["agents"], 224)


if __name__ == "__main__":
    unittest.main()
