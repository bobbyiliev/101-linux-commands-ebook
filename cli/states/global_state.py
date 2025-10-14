import typer

# Global flag storage
verbose_flag = {"enabled": False}


def debug(msg: str):
    if verbose_flag["enabled"]:
        typer.secho(f"[DEBUG] {msg}", fg=typer.colors.CYAN, bold=True)
