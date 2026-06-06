"""Five chart families for constitutional-ai-mini."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure

from caimini.types import Critique, JudgeResult


def _save(fig: Figure, out: Path) -> Path:
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(out, dpi=160)
    plt.close(fig)
    return out


def violation_rate_bar(rows: list[Critique], stage: str, out: Path) -> Path:
    by_p: dict[str, list[int]] = {}
    for c in rows:
        by_p.setdefault(c.principle, []).append(int(c.flagged))
    ps = sorted(by_p)
    rates = [sum(by_p[p]) / max(1, len(by_p[p])) for p in ps]
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(ps, rates, color="#c25a4f")
    ax.set_ylim(0, 1.05)
    ax.set_ylabel("violation rate")
    ax.set_title(f"Per-principle violation rate ({stage})")
    return _save(fig, out)


def winrate_pie(results: list[JudgeResult], out: Path) -> Path:
    cnt = Counter(r.winner for r in results)
    labels = list(cnt.keys())
    vals = list(cnt.values())
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.pie(vals, labels=labels, autopct="%1.0f%%", colors=["#5b8d4a", "#3b6fa1", "#7a7a7a"])
    ax.set_title("Revision win rate")
    return _save(fig, out)


def margin_hist(results: list[JudgeResult], out: Path) -> Path:
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.hist([r.margin for r in results], bins=10, color="#5b8d4a", edgecolor="white")
    ax.set_xlabel("revision margin")
    ax.set_ylabel("instructions")
    ax.set_title("Margin distribution")
    return _save(fig, out)


def violations_pre_post_bar(pre: list[Critique], post: list[Critique], out: Path) -> Path:
    pre_n = sum(1 for c in pre if c.flagged)
    post_n = sum(1 for c in post if c.flagged)
    fig, ax = plt.subplots(figsize=(7, 4))
    bars = ax.bar(["pre-revision", "post-revision"], [pre_n, post_n], color=["#c25a4f", "#5b8d4a"])
    ax.set_ylabel("# violations")
    ax.set_title("Total violations before vs after revision")
    for bar, v in zip(bars, [pre_n, post_n], strict=True):
        ax.text(bar.get_x() + bar.get_width() / 2, v + 0.1, str(v), ha="center", fontsize=11)
    return _save(fig, out)


def per_instruction_heatmap(pre: list[Critique], post: list[Critique], out: Path) -> Path:
    iids = sorted({c.iid for c in pre} | {c.iid for c in post})
    principles = sorted({c.principle for c in pre})
    pre_mat = np.zeros((len(principles), len(iids)))
    post_mat = np.zeros_like(pre_mat)
    for c in pre:
        pre_mat[principles.index(c.principle), iids.index(c.iid)] = int(c.flagged)
    for c in post:
        post_mat[principles.index(c.principle), iids.index(c.iid)] = int(c.flagged)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))
    for ax, mat, title in [(ax1, pre_mat, "pre"), (ax2, post_mat, "post")]:
        ax.imshow(mat, aspect="auto", cmap="Reds", vmin=0, vmax=1)
        ax.set_xticks(range(len(iids)))
        ax.set_xticklabels(iids, rotation=45, ha="right", fontsize=8)
        ax.set_yticks(range(len(principles)))
        ax.set_yticklabels(principles)
        ax.set_title(title)
    return _save(fig, out)
