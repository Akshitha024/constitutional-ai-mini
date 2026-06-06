"""Types."""

from __future__ import annotations

from pydantic import BaseModel, Field


class Principle(BaseModel):
    pid: str
    text: str
    forbidden_markers: list[str] = Field(default_factory=list)


class Instruction(BaseModel):
    iid: str
    text: str


class Response(BaseModel):
    iid: str
    text: str


class Critique(BaseModel):
    iid: str
    principle: str
    flagged: bool
    note: str = ""


class Revision(BaseModel):
    iid: str
    original: str
    revised: str
    critique_notes: list[str] = Field(default_factory=list)


class JudgeResult(BaseModel):
    iid: str
    winner: str  # "original" | "revised" | "tie"
    margin: float = Field(ge=0, le=1)
