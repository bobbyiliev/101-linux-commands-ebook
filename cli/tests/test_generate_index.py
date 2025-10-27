#!/usr/bin/env python3
"""Tests for the generator script that builds cli/data/commands.json."""

from pathlib import Path
import subprocess
import sys
import json


def test_generate_index_creates_file():
    cli_dir = Path(__file__).resolve().parents[1]
    script = cli_dir / "scripts" / "generate_command_index.py"
    assert script.exists(), "Generator script missing"

    # run the script
    result = subprocess.run(
        [sys.executable, str(script)], capture_output=True, text=True, cwd=str(cli_dir)
    )
    assert result.returncode == 0, f"Generator failed: {result.stdout}\n{result.stderr}"

    data_file = cli_dir / "data" / "commands.json"
    assert data_file.exists(), "commands.json was not created"

    data = json.loads(data_file.read_text(encoding="utf-8"))
    assert isinstance(data, list)
    # at least one item and 'ls' should be present for this ebook
    assert len(data) > 0
    assert any(
        (item.get("name") == "ls") or (item.get("name") == "cat") for item in data
    ), "Expected 'ls' or 'cat' in generated index"
