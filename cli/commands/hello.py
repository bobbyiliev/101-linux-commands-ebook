"""
Hello command for the 101 Linux Commands CLI.
"""

import typer

from states.global_state import debug, verbose_flag

app = typer.Typer(help="Hello command group")


@app.command()
def greet(name: str = "World"):
    """Say hello to someone."""

    if verbose_flag["enabled"]:
        debug(f"Greeting {name}")

    typer.echo(f"Hello, {name}!")
