"""Reviser tests."""

from __future__ import annotations

from caimini.critic.checker import critique
from caimini.principles.library import constitution
from caimini.reviser.rewriter import revise
from caimini.types import Response


def test_revise_redacts_forbidden_marker() -> None:
    consts = constitution()
    r = Response(iid="x", text="You are stupid.")
    pre = critique(r, consts)
    rev = revise(r, pre, consts)
    assert "stupid" not in rev.revised.lower()
    assert "[REDACTED]" in rev.revised


def test_revise_clean_response_unchanged() -> None:
    consts = constitution()
    r = Response(iid="x", text="hello world")
    pre = critique(r, consts)
    rev = revise(r, pre, consts)
    assert rev.revised == r.text
