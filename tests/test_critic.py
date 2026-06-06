"""Critic tests."""

from __future__ import annotations

from caimini.critic.checker import critique
from caimini.principles.library import constitution
from caimini.types import Response


def test_clean_response_no_flags() -> None:
    consts = constitution()
    r = Response(iid="x", text="hello world")
    flags = [c for c in critique(r, consts) if c.flagged]
    assert flags == []


def test_insult_triggers_respect() -> None:
    consts = constitution()
    r = Response(iid="x", text="You are stupid.")
    flags = [c for c in critique(r, consts) if c.flagged]
    assert any(c.principle == "p-respect" for c in flags)
