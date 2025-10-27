import json
from pathlib import Path
from typing import Dict, List

import typer

from states.global_state import debug, verbose_flag

app = typer.Typer(help=("Search available commands by keyword (name or description)."))


def _get_available_commands() -> List[Dict[str, str]]:
    """
    Return commands loaded from cli/data/commands.json if available, else fall back
    to the mocked in-code list.
    """
    data_path = Path(__file__).parent.parent / "data" / "commands.json"
    if data_path.exists():
        try:
            data = json.loads(data_path.read_text(encoding="utf-8"))
            # normalize to list of dicts with name/description
            return [
                {
                    "name": item.get("name", ""),
                    "description": item.get("description", ""),
                }
                for item in data
            ]
        except Exception:
            pass

    # fallback mocked data
    return [
        {"name": "ls", "description": "List directory contents"},
        {"name": "grep", "description": "Search for PATTERN in files"},
        {
            "name": "find",
            "description": "Search for files in a directory hierarchy",
        },
        {
            "name": "awk",
            "description": "Pattern scanning and processing language",
        },
        {
            "name": "cat",
            "description": ("Concatenate files and print on the standard output"),
        },
        {"name": "head", "description": "Output the first part of files"},
        {"name": "tail", "description": "Output the last part of files"},
        {
            "name": "sed",
            "description": ("Stream editor for filtering and transforming text"),
        },
    ]


def _search_commands(
    keyword: str,
    commands: List[Dict[str, str]],
) -> List[Dict[str, str]]:
    k = (keyword or "").strip().lower()
    if not k:
        return []
    return [
        cmd
        for cmd in commands
        if (k in cmd.get("name", "").lower())
        or (k in cmd.get("description", "").lower())
    ]


@app.callback(invoke_without_command=True)
def search(
    keyword: str = typer.Argument(
        ...,
        help="Keyword to search for, e.g. 'grep'",
    ),
) -> None:
    """
    Search available commands by keyword (matches command name or description).
    Example: python cli.py search grep
    """
    results = _search_commands(keyword, _get_available_commands())
    if not results:
        typer.echo("No commands found.")
        raise typer.Exit(code=1)

    if verbose_flag["enabled"]:
        debug(f"Found {len(results)} commands matching '{keyword}'")

    for cmd in results:
        name = cmd.get("name", "").strip()
        desc = cmd.get("description", "").strip()
        typer.echo(f"{name}: {desc}")
