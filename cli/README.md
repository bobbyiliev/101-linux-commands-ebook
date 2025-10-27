# 101 Linux Commands CLI Tool

Interactive CLI tool companion for the 101 Linux Commands eBook.

## Usage

To get started, install the dependencies and run the CLI:

```bash
uv sync --frozen

# for Windows PowerShell
.\.venv\Scripts\Activate.ps1
# OR for macOS/Linux
source .venv/bin/activate

python -m cli --help
```

The CLI will be installed as an editable package.
```bash
linux-cli --help
```
### Options
*   `--verbose`: Enable verbose output for debugging purposes.
    Example:
    ```bash
    linux-cli --verbose hello greet
    ```
    OR

    ```bash
    cd cli
    python -m cli --verbose hello greet
    ```

### Examples

Here are some examples of how to use the CLI:

> Note: The `list`, `search`, and `show` commands are still under development.

*   **List all commands:**

    ```bash
    linux-cli list
    ```

*   **Search for a command:**

    ```bash
    linux-cli search grep
    ```

*   **Show details for a command:**

    ```bash
    linux-cli show ls
    ```

## Generating the CLI command index

The CLI can consume a generated index of commands parsed from the ebook markdown. This keeps the CLI registry in sync with the eBook source.

To generate or refresh the index, run the generator from the `cli/` directory:

```powershell
# from the repo root
cd cli
python scripts/generate_command_index.py
```

That will create `cli/data/commands.json` which `show` and `search` will prefer when present. The test `tests/test_generate_index.py` exercises the generator.


## Development

### Running Tests
```bash
pytest
```

### Code Formatting
```bash
black cli/
```

### Import Sorting
```bash
isort cli/
```

### Linting
```bash
flake8 cli/
```

### Type Checking
```bash
mypy cli/
```

## GitHub Actions

The CLI has its own workflow that runs:
- Code formatting checks (Black)
- Import sorting checks (isort) 
- Linting (Flake8)
- Type checking (MyPy)
- Tests (pytest)

This workflow only triggers on changes to the `cli/` directory.