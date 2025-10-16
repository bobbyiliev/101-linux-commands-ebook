"""
Stub command to build the ebook using Ibis.
"""

import typer

from states.global_state import debug, verbose_flag

app = typer.Typer(help="Ebook Builder CLI using Ibis")


@app.command()
def build():
    """Build the ebook using Ibis."""

    if verbose_flag["enabled"]:
        debug("Starting the build process using Ibis")

    typer.echo("Building ebook with Ibis... (this is a stub command)")

    if verbose_flag["enabled"]:
        debug("Build process completed")
