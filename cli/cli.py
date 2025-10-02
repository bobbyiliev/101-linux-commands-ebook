"""
CLI entry point for the 101 Linux Commands application.
"""

import typer

from commands import hello, list, version

app = typer.Typer(help="101 Linux Commands CLI 🚀")
app.add_typer(hello.app, name="hello")
app.add_typer(list.app, name="list")
app.add_typer(version.app, name="version")


def main() -> None:
    """CLI entry point."""
    app()


if __name__ == "__main__":
    app()
