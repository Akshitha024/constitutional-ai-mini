"""Typer CLI."""

from __future__ import annotations

import json
from pathlib import Path

import typer
from rich.console import Console

from caimini.runner import run

app = typer.Typer(no_args_is_help=True, help="Constitutional-AI mini.")
console = Console()


@app.command()
def info() -> None:
    console.print("constitutional-ai-mini: see `caimini bench --help`.")


@app.command()
def bench(out_dir: Path = typer.Option(Path("runs/latest"))) -> None:
    res = run(out_dir)
    console.print_json(json.dumps(res, default=str))


if __name__ == "__main__":
    app()
