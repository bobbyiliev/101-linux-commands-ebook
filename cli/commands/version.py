"""Version command for 101-linux-commands CLI."""

import sys
from pathlib import Path

import typer

from __version__ import __version__
from states.global_state import debug, verbose_flag

sys.path.insert(0, str(Path(__file__).parent.parent))

app = typer.Typer(help="version command")


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """Show the current version of 101-linux CLI"""
    if ctx.invoked_subcommand is None:
        if verbose_flag["enabled"]:
            debug("Showing version")
        typer.echo(f"101-linux v{__version__}")


@app.command()
def show():
    """Show the current version of 101-linux CLI"""
    if verbose_flag["enabled"]:
        debug("Showing version")
    typer.echo(f"101-linux v{__version__}")
