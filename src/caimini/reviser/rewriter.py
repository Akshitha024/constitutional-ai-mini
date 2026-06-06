"""Revise a response by stripping forbidden markers."""

from __future__ import annotations

from caimini.types import Critique, Principle, Response, Revision


def revise(
    response: Response, critiques: list[Critique], constitution: list[Principle]
) -> Revision:
    text = response.text
    notes: list[str] = []
    for c in critiques:
        if not c.flagged:
            continue
        principle = next((p for p in constitution if p.pid == c.principle), None)
        if principle is None:
            continue
        for marker in principle.forbidden_markers:
            if marker.lower() in text.lower():
                # Case-insensitive replace.
                import re

                text = re.sub(re.escape(marker), "[REDACTED]", text, flags=re.IGNORECASE)
                notes.append(f"Redacted '{marker}' (principle {principle.pid}).")
    return Revision(iid=response.iid, original=response.text, revised=text, critique_notes=notes)
