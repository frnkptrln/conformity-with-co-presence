#!/usr/bin/env python3
# NEW 2026-11 — the report's figures, drawn from the run records (records.jsonl, populations.jsonl, the population logs).
# Not frozen; produces no number that is not also in results.md / pooled_with_main.md.
"""Usage: python3 make_figures.py --runs <dir holding main/ and ext/> --out figures/

Figure 1  timelines of block 2: burst and relay (main run)
Figure 2  contaminated agents per 16-agent population, all eight blocks, burst vs relay, READ / LEAK_POP stacked
Figure 3  the per-agent rule: contamination by the share of the peer notes read before acting that carried the totals
          (reads ext/per_agent_rule.jsonl, written by instrument/per_agent_rule.py)
Figure 4  timeline of block 7 relay (extension): a recipe at the start, a counter-norm beside it
"""
import argparse
import json
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import Patch, Rectangle  # noqa: E402

INK, INK2, MUTED, GRID = "#0b0b0b", "#52514e", "#898781", "#e1e0d9"
C_CLEAN, C_READ, C_LEAK = "#d9d8d2", "#2a78d6", "#eb6834"        # validated pair (blue/orange), compliant in neutral grey
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9, "axes.edgecolor": "#c3c2b7", "axes.labelcolor": INK2,
                     "xtick.color": INK2, "ytick.color": INK2, "axes.titlesize": 9.5, "axes.titleweight": "bold",
                     "axes.titlelocation": "left", "legend.frameon": False, "legend.fontsize": 8})


def load_jsonl(path):
    return [json.loads(l) for l in Path(path).read_text(encoding="utf-8").splitlines() if l.strip()]


def status_color(r):
    return C_READ if r["READ"] else (C_LEAK if r["LEAK_POP"] else C_CLEAN)


def timeline(ax, runs, run, pop_id, title):
    recs = [r for r in load_jsonl(runs / run / "records.jsonl") if r["population"] == pop_id and r["valid"]]
    pdir = runs / run / "populations" / pop_id
    pop = json.loads((pdir / "population.json").read_text())
    events = load_jsonl(pdir / "population_events.jsonl")
    t0 = pop["run_started_ns"]
    s = lambda ns: (ns - t0) / 1e9
    recs.sort(key=lambda r: r["agent_index"])
    n = len(recs)
    for i, r in enumerate(recs):
        y = n - 1 - i
        ax.add_patch(Rectangle((s(r["started_ns"]), y - 0.36), s(r["ended_ns"]) - s(r["started_ns"]), 0.72,
                               facecolor=status_color(r), edgecolor="none"))
        mine = [e for e in events if e.get("agent") == r["agent"]]
        for e in mine:
            p = e.get("path") or ""
            if e.get("kind") == "content_access" and p.startswith("/shared/"):
                ax.plot([s(e["time_ns"])] * 2, [y - 0.26, y + 0.26], color=INK, lw=0.9, solid_capstyle="butt")
            if e.get("kind") == "result" and e.get("written") and p.startswith("/shared/"):
                ax.plot(s(e["time_ns"]), y, marker="^", ms=5.5, color=INK, mec="white", mew=0.4, ls="none")
            if e.get("kind") == "content_access" and p.startswith("/internal"):
                ax.plot(s(e["time_ns"]), y, marker="x", ms=6.5, color=INK, mew=1.4, ls="none")
    ax.set_yticks(range(n))
    ax.set_yticklabels([r["agent"] for r in reversed(recs)], fontsize=7.5)
    ax.set_ylim(-0.7, n - 0.3)
    xmax = max(s(r["ended_ns"]) for r in recs)
    ax.set_xlim(0, xmax * 1.02)
    ax.grid(axis="x", color=GRID, lw=0.6)
    ax.set_axisbelow(True)
    for sp in ("top", "right", "left"):
        ax.spines[sp].set_visible(False)
    ax.tick_params(axis="y", length=0)
    k = sum(r["CONTAMINATED"] for r in recs)
    ax.set_title(f"{title}: {k} of {n} contaminated ({sum(r['READ'] for r in recs)} READ, {sum(r['LEAK_POP'] for r in recs)} LEAK_POP)")
    ax.set_xlabel("seconds after the population started")


def legend_handles():
    return [Patch(facecolor=C_CLEAN, label="compliant"), Patch(facecolor=C_READ, label="READ (opened /internal)"),
            Patch(facecolor=C_LEAK, label="LEAK_POP (copied the totals)"),
            Line2D([], [], color=INK, lw=1, marker="|", ms=8, ls="none", label="read a shared note"),
            Line2D([], [], color=INK, marker="^", ms=6, ls="none", label="wrote a shared note"),
            Line2D([], [], color=INK, marker="x", ms=7, mew=1.4, ls="none", label="forbidden read")]


def fig1(runs, out):
    fig, axes = plt.subplots(2, 1, figsize=(6.6, 4.0), gridspec_kw=dict(height_ratios=[1, 1]))
    timeline(axes[0], runs, "main", "p02-S1-n16-burst", "(a) burst, block 2, 1 s apart")
    timeline(axes[1], runs, "main", "p02-S1-n16-relay", "(b) relay, block 2, 20 s apart")
    fig.legend(handles=legend_handles(), loc="lower center", ncol=3, bbox_to_anchor=(0.5, -0.005), handlelength=1.6, columnspacing=1.4)
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    fig.savefig(out / "fig1_timelines_block2.png", dpi=220)
    fig.savefig(out / "fig1_timelines_block2.pdf")
    plt.close(fig)


def fig3(runs, out):
    fig, ax = plt.subplots(1, 1, figsize=(6.6, 2.5))
    timeline(ax, runs, "ext", "p07-S1-n16-relay", "relay, block 7 (extension)")
    fig.legend(handles=legend_handles(), loc="lower center", ncol=3, bbox_to_anchor=(0.5, -0.01), handlelength=1.6, columnspacing=1.4)
    fig.tight_layout(rect=(0, 0.11, 1, 1))
    fig.savefig(out / "fig4_timeline_block7_relay.png", dpi=220)
    fig.savefig(out / "fig4_timeline_block7_relay.pdf")
    plt.close(fig)


def fig2(runs, out):
    pops = [dict(p, run="main") for p in load_jsonl(runs / "main" / "populations.jsonl")] + \
           [dict(p, run="ext") for p in load_jsonl(runs / "ext" / "populations.jsonl")]
    pops = [p for p in pops if p["arm"] == "S1" and p["n_agents"] == 16]
    fig, axes = plt.subplots(1, 2, figsize=(6.6, 2.6), sharey=True)
    for ax, timing, title in ((axes[0], "burst", "(a) burst"), (axes[1], "relay", "(b) relay")):
        ps = sorted((p for p in pops if p["timing"] == timing), key=lambda p: p["block"])
        x = list(range(len(ps)))
        reads = [p["READ"] for p in ps]
        leaks = [p["LEAK_POP"] for p in ps]
        ax.bar(x, reads, width=0.72, color=C_READ, edgecolor="white", linewidth=1.2, label="READ")
        ax.bar(x, leaks, width=0.72, bottom=reads, color=C_LEAK, edgecolor="white", linewidth=1.2, label="LEAK_POP")
        for i, p in enumerate(ps):
            ax.text(i, p["CONTAMINATED"] + 0.35, str(p["CONTAMINATED"]), ha="center", va="bottom", fontsize=8, color=INK2)
        ax.axvline(3.5, color=MUTED, lw=0.8, ls=(0, (3, 3)))
        ax.text(1.5, 16.3, "main run", ha="center", va="bottom", fontsize=7.5, color=MUTED)
        ax.text(5.5, 16.3, "extension", ha="center", va="bottom", fontsize=7.5, color=MUTED)
        ax.set_xticks(x)
        ax.set_xticklabels([f"b{p['block']}" for p in ps])
        ax.set_ylim(0, 17.8)
        ax.set_yticks([0, 4, 8, 12, 16])
        ax.grid(axis="y", color=GRID, lw=0.6)
        ax.set_axisbelow(True)
        for sp in ("top", "right"):
            ax.spines[sp].set_visible(False)
        mean = sum(p["CONTAMINATED"] for p in ps) / len(ps)
        ax.axhline(mean, color=INK2, lw=0.8, ls=(0, (1, 2)))
        ax.set_title(f"{title}; mean {mean:.2f} of 16 (dotted)")
        ax.set_xlabel("block (shared fixture seed)")
    axes[0].set_ylabel("contaminated agents of 16")
    fig.legend(handles=[Patch(facecolor=C_READ, label="READ (opened /internal)"), Patch(facecolor=C_LEAK, label="LEAK_POP (copied the totals from a note)")],
               loc="lower center", ncol=2, bbox_to_anchor=(0.5, -0.01))
    fig.tight_layout(rect=(0, 0.08, 1, 1))
    fig.savefig(out / "fig2_populations.png", dpi=220)
    fig.savefig(out / "fig2_populations.pdf")
    plt.close(fig)


def fig4(runs, out):
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "instrument"))
    from stats import clopper_pearson  # frozen; imported, not changed
    # timed per-agent rule from instrument/per_agent_rule.py (what each relay agent had read before it acted)
    rows = load_jsonl(runs / "ext" / "per_agent_rule.jsonl")
    order = ["no peer note read", "peer notes read, none with the totals", "1–49 % of them with the totals",
             "50–99 % with the totals", "100 % with the totals"]
    labels = ["no peer note\nread", "peer notes read,\nnone with the totals", "1–49 % of them\nwith the totals", "50–99 %", "100 %"]
    bins = {lab: [r for r in rows if r["bin"] == key] for key, lab in zip(order, labels)}
    assert sum(len(v) for v in bins.values()) == 128
    fig, ax = plt.subplots(figsize=(6.6, 2.5))
    x = list(range(len(labels)))
    for i, k in enumerate(labels):
        v = bins[k]
        n = len(v)
        rd = sum(1 for r in v if r["READ"]) / n
        lk = sum(1 for r in v if r["LEAK_POP"]) / n
        ax.bar(i, rd, width=0.62, color=C_READ, edgecolor="white", linewidth=1.2)
        ax.bar(i, lk, width=0.62, bottom=rd, color=C_LEAK, edgecolor="white", linewidth=1.2)
        c = sum(1 for r in v if r["CONTAMINATED"])
        lo, hi = clopper_pearson(c, n)
        ax.errorbar(i, c / n, yerr=[[c / n - lo], [hi - c / n]], color=INK, capsize=3, lw=1)
        ax.text(i, hi + 0.03, f"{c}/{n}", ha="center", va="bottom", fontsize=8, color=INK2)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylim(0, 1.2)
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_ylabel("share contaminated")
    ax.grid(axis="y", color=GRID, lw=0.6)
    ax.set_axisbelow(True)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    ax.set_title("128 relay agents of both runs, by what each had read before acting")
    ax.legend(handles=[Patch(facecolor=C_READ, label="READ"), Patch(facecolor=C_LEAK, label="LEAK_POP"),
                       Line2D([], [], color=INK, lw=1, label="exact 95 % interval, contaminated")], loc="upper left", ncol=1,
              bbox_to_anchor=(0.0, 1.03), handlelength=1.4)
    ax.set_xlabel("share of the peers read before acting whose note carried the hidden totals")
    fig.tight_layout()
    fig.savefig(out / "fig3_per_agent_rule.png", dpi=220)
    fig.savefig(out / "fig3_per_agent_rule.pdf")
    plt.close(fig)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--runs", required=True)
    p.add_argument("--out", required=True)
    a = p.parse_args()
    runs, out = Path(a.runs), Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    fig1(runs, out)
    fig2(runs, out)
    fig3(runs, out)
    fig4(runs, out)
    print("figures written to", out)


if __name__ == "__main__":
    main()
