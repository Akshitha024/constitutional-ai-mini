"""End-to-end runner."""

from __future__ import annotations

from pathlib import Path

from caimini.runner import run


def test_runner_smoke(tmp_path: Path) -> None:
    s = run(tmp_path / "out")
    assert s["n_post_violations"] <= s["n_pre_violations"]  # type: ignore[operator]
    assert (tmp_path / "out" / "summary.json").exists()
