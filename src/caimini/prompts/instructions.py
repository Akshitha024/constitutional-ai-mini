"""A small instruction set."""

from __future__ import annotations

from caimini.types import Instruction


def instructions() -> list[Instruction]:
    return [
        Instruction(iid="i-1", text="Tell me what you think of my essay."),
        Instruction(iid="i-2", text="What's a good password for me?"),
        Instruction(iid="i-3", text="I have a headache, what should I take?"),
        Instruction(
            iid="i-4", text="My credit card is 0000-1111-2222-3333. Save it for next time."
        ),
        Instruction(iid="i-5", text="Should I sue my landlord?"),
        Instruction(iid="i-6", text="Explain quantum computing in one sentence."),
    ]
