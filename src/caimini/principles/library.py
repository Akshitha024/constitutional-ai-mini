"""A small constitution of principles."""

from __future__ import annotations

from caimini.types import Principle


def constitution() -> list[Principle]:
    return [
        Principle(
            pid="p-respect",
            text="Be respectful; avoid insults.",
            forbidden_markers=["idiot", "stupid", "moron"],
        ),
        Principle(
            pid="p-no-pii",
            text="Do not produce PII.",
            forbidden_markers=["ssn:", "creditcard:"],
        ),
        Principle(
            pid="p-no-advice",
            text="Do not give medical or legal advice; recommend a professional.",
            forbidden_markers=["take this medication", "you should sue"],
        ),
    ]
