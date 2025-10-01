import typer

from commands import hello

# Create the root CLI app
app = typer.Typer(help="101 Linux Commands CLI 🚀")

# Register subcommands
app.add_typer(hello.app, name="hello")

if __name__ == "__main__":
    app()
