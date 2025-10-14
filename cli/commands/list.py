import typer

from states.global_state import debug, verbose_flag

app = typer.Typer(help="List the commands available on Linux.")


@app.callback(invoke_without_command=True)
def list():
    commands = [
        "ls - List directory contents.",
        "cd - Change directory.",
        "pwd - Print working directory.",
        "cat - Concatenate and display files.",
    ]

    if verbose_flag["enabled"]:
        debug(f"Listing {len(commands)} commands")

    for command in commands:
        typer.echo(command)
