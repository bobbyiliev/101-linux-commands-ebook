"""
CLI entry point for the 101 Linux Commands application.
"""

import typer

from commands import hello

app = typer.Typer(help="101 Linux Commands CLI 🚀")
app.add_typer(hello.app, name="hello")


def main() -> None:
    """CLI entry point."""
    app()


if __name__ == "__main__":
    app()
