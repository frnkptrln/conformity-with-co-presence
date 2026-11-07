#!/usr/bin/env python3
# NEW 2026-11 — collusion with co-presence (Apart Research Swarm Alignment Hackathon, 6–8 November 2026)
"""Freeze: hash the bound pre-registration and the instrument into MANIFEST.sha256.json; check for drift.

  python3 freeze.py            # refuses while PREREGISTRATION.md still holds a [FRANK] or [BIND] placeholder
  python3 freeze.py --check    # exit 1 if any frozen file changed since the freeze

Every change to a frozen file after the freeze is a dated entry in DEVIATIONS.md.
"""
import argparse
import hashlib
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
FROZEN = ("PREREGISTRATION.md", "RUNBOOK.md",
          "instrument/fixtures_r3.py", "instrument/workspace_server.py", "instrument/population_server.py", "instrument/run_r3.py",
          "instrument/run_population.py", "instrument/analyze_r3.py", "instrument/analyze_population.py", "instrument/schema.py",
          "instrument/stats.py", "instrument/report.py", "instrument/gate_population.py", "instrument/freeze.py", "instrument/quota.py",
          "analysis/stats.py")
PLACEHOLDERS = ("[FRANK]", "[BIND]")


def hashes():
    return {rel: hashlib.sha256((REPO / rel).read_bytes()).hexdigest() for rel in FROZEN if (REPO / rel).exists()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    manifest = HERE / "MANIFEST.sha256.json"
    if a.check:
        if not manifest.exists():
            print("no manifest: not frozen")
            sys.exit(1)
        frozen = json.loads(manifest.read_text())["files"]
        now = hashes()
        drift = sorted(k for k in set(frozen) | set(now) if frozen.get(k) != now.get(k))
        print(json.dumps({"frozen_at": json.loads(manifest.read_text())["frozen_at"], "drift": drift}, indent=2))
        sys.exit(1 if drift else 0)
    prereg = (REPO / "PREREGISTRATION.md").read_text(encoding="utf-8")
    open_marks = [m for m in PLACEHOLDERS if m in prereg]
    if open_marks:
        print(f"refused: PREREGISTRATION.md still holds {open_marks} — bind every placeholder first")
        sys.exit(1)
    if manifest.exists():
        print("refused: MANIFEST.sha256.json exists — a second freeze is a DEVIATIONS entry, not a new manifest")
        sys.exit(1)
    data = {"frozen_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "files": hashes()}
    manifest.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    body = manifest.read_bytes()
    print(json.dumps({"manifest": str(manifest.relative_to(REPO)), "sha256": hashlib.sha256(body).hexdigest(), "files": len(data["files"]),
                      "preregistration_sha256": data["files"].get("PREREGISTRATION.md")}, indent=2))


if __name__ == "__main__":
    main()
