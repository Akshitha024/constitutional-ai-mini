"""Critique = check each principle against a response for forbidden markers."""

from __future__ import annotations

from caimini.types import Critique, Principle, Response


def critique(response: Response, constitution: list[Principle]) -> list[Critique]:
    out: list[Critique] = []
    text = response.text.lower()
    for p in constitution:
        hit = any(m.lower() in text for m in p.forbidden_markers)
        out.append(
            Critique(
                iid=response.iid,
                principle=p.pid,
                flagged=hit,
                note=(f"Found forbidden marker for principle {p.pid}." if hit else ""),
            )
        )
    return out
