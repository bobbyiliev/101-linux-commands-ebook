from typing import Dict, TypedDict

import json
from pathlib import Path
import typer

from states.global_state import debug, verbose_flag


class CommandInfo(TypedDict):
    description: str
    usage: str
    example: str
    notes: str


def _load_commands_from_json() -> Dict[str, CommandInfo] | None:
    data_path = Path(__file__).parent.parent / "data" / "commands.json"
    if not data_path.exists():
        return None
    try:
        data = json.loads(data_path.read_text(encoding="utf-8"))
        result: Dict[str, CommandInfo] = {}
        for item in data:
            key = item.get("name")
            if not key:
                continue
            result[key] = {
                "description": item.get("description", ""),
                "usage": item.get("usage", ""),
                "example": item.get("example", ""),
                "notes": item.get("notes", ""),
            }
        return result
    except Exception:
        return None


# Try to load a generated commands index, otherwise fall back to the baked-in dataset
_LOADED_COMMANDS = _load_commands_from_json()


COMMANDS: Dict[str, CommandInfo]

if _LOADED_COMMANDS is not None:
    COMMANDS = _LOADED_COMMANDS
else:
    # fallback in-code registry
    COMMANDS = {
        "ls": {
            "description": (
                "List information about the files in the current directory (the default). "
                "Options can be used to modify the output format, sort order, and more."
            ),
            "usage": "ls [OPTION]... [FILE]...",
            "example": "ls -la /var/log",
            "notes": (
                "- `-l` : use a long listing format\n"
                "- `-a` : show hidden files (starting with `.`)\n"
                "- `-h` : with -l, print sizes in human-readable format (e.g., 1K, 234M)"
            ),
        },
        "grep": {
            "description": (
                "Search input files for lines containing a match to the given PATTERN. "
                "Often used for filtering log files or searching through code."
            ),
            "usage": "grep [OPTION]... PATTERN [FILE]...",
            "example": 'grep -R "TODO" .',
            "notes": (
                "- `-i` : ignore case distinctions\n"
                "- `-R` : recursively search subdirectories\n"
                "- `-n` : show line numbers of matches"
            ),
        },
        "cat": {
            "description": (
                "Concatenate files and print on the standard output. "
                "Often used to quickly view file contents."
            ),
            "usage": "cat [OPTION]... [FILE]...",
            "example": "cat /etc/passwd",
            "notes": (
                "- `-n` : number all output lines\n"
                "- `-b` : number non-blank lines\n"
                "- Use with pipes: `cat file.txt | grep pattern`"
            ),
        },
        "mkdir": {
            "description": (
                "Create directories if they do not already exist. "
                "By default, it creates a single directory."
            ),
            "usage": "mkdir [OPTION]... DIRECTORY...",
            "example": "mkdir -p projects/python/app",
            "notes": (
                "- `-p` : create parent directories as needed\n"
                "- `-v` : print a message for each created directory"
            ),
        },
    }


def show(
    command: str = typer.Argument(..., help="Linux command to show details for"),
) -> None:
    """
    Display description, usage, examples, and notes for a given Linux command.
    """

    key = command.strip()
    info = COMMANDS.get(key)

    if not info:
        typer.secho(
            f"Unknown command '{command}'. Try one of: {', '.join(sorted(COMMANDS))}",
            err=True,
            fg=typer.colors.RED,
        )
        raise typer.Exit(code=1)

    if verbose_flag["enabled"]:
        debug(f"Showing details for command: {key}")

    typer.secho(f"\nCommand: {key}\n", fg=typer.colors.CYAN, bold=True)

    typer.secho("Description:", fg=typer.colors.MAGENTA, bold=True)
    typer.echo(f"  {info['description']}\n")

    typer.secho("Usage:", fg=typer.colors.MAGENTA, bold=True)
    typer.echo(f"  {info['usage']}\n")

    typer.secho("Example:", fg=typer.colors.MAGENTA, bold=True)
    typer.echo(f"  {info['example']}\n")

    typer.secho("Notes:", fg=typer.colors.MAGENTA, bold=True)
    typer.echo(f"{info['notes']}\n")
