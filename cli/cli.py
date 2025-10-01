import typer
from cli.commands import hello

# Create the root CLI app
app = typer.Typer(help="My CLI Application 🚀")

# Register subcommands
app.add_typer(hello.app, name="hello")

if __name__ == "__main__":
    app()
