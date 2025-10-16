"""
CLI entry point for the 101 Linux Commands application.
"""

from typing import List

import click
import typer
from typer.main import TyperGroup

from commands import build, hello, list, search, show, version
from states.global_state import verbose_flag


class CustomTyper(TyperGroup):
    def resolve_command(self, ctx: click.Context, args: List[str]):
        try:
            return super().resolve_command(ctx, args)
        except click.exceptions.UsageError as e:
            original = e.format_message()

            if "No such command" in original:
                script_name = ctx.find_root().info_name or "cli"
                hint = f"💡 Hint: Run '{script_name} --help' to see available commands."

                new_message = f"{original}\n{hint}"
                raise click.exceptions.UsageError(new_message, ctx=ctx) from e

            raise


app = typer.Typer(help="101 Linux Commands CLI 🚀", cls=CustomTyper)
app.add_typer(hello.app, name="hello")
app.add_typer(list.app, name="list")
app.add_typer(version.app, name="version")
app.command()(show.show)
app.add_typer(search.app, name="search")
app.command()(build.build)


# Main callback to handle global options
def main_callback(
    verbose: bool = typer.Option(False, "--verbose", help="Enable verbose output")
) -> None:
    verbose_flag["enabled"] = verbose
    if verbose:
        typer.secho("[DEBUG] Verbose mode enabled", fg=typer.colors.YELLOW, bold=True)


app.callback()(main_callback)


def main() -> None:
    """CLI entry point."""
    app()


if __name__ == "__main__":
    main()
