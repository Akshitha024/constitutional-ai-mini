"""Compare original vs revised; pick the winner based on remaining principle violations."""

from __future__ import annotations

from caimini.critic.checker import critique
from caimini.types import JudgeResult, Principle, Response, Revision


def judge(rev: Revision, constitution: list[Principle]) -> JudgeResult:
    orig_resp = Response(iid=rev.iid, text=rev.original)
    new_resp = Response(iid=rev.iid, text=rev.revised)
    orig_flags = sum(1 for c in critique(orig_resp, constitution) if c.flagged)
    new_flags = sum(1 for c in critique(new_resp, constitution) if c.flagged)
    if new_flags < orig_flags:
        margin = (orig_flags - new_flags) / max(1, len(constitution))
        return JudgeResult(iid=rev.iid, winner="revised", margin=margin)
    if new_flags > orig_flags:
        margin = (new_flags - orig_flags) / max(1, len(constitution))
        return JudgeResult(iid=rev.iid, winner="original", margin=margin)
    return JudgeResult(iid=rev.iid, winner="tie", margin=0.0)
