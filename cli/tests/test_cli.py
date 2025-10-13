#!/usr/bin/env python3
"""Basic tests for the CLI module."""

import os
import re
import sys
import pytest
import subprocess
from pathlib import Path


ANSI_ESCAPE = re.compile(r"\x1B\[[0-?]*[ -/]*[@-~]")
EMOJI = re.compile("[\U0001f300-\U0001faff]", flags=re.UNICODE)
CLI_APP_PATH = Path(__file__).parents[2] / "cli" / "cli.py"


def clean_output(text: str) -> str:
    """Remove ANSI colors and emojis."""
    text = ANSI_ESCAPE.sub("", text)
    text = EMOJI.sub("", text)
    return text


@pytest.mark.parametrize(
    "args, expected_strings, exit_code",
    (
        (
            ("--help",),
            ("101 Linux Commands CLI",),
            0
        ),
        (
            ("hello", "greet"),
            ("Hello, World!",),
            0
        ),
        (
            ("hello", "greet", "--name", "Linux"),
            ("Hello, Linux!",),
            0
        ),
        (
            ("hello", "--help"),
            ("Hello command group",),
            0
        ),
        (
            ("list",),
            (
                "ls - List directory contents.",
                "cd - Change directory.",
                "pwd - Print working directory.",
                "cat - Concatenate and display files."
            ),
            0
        ),
        (
            ("version",),
            ("101-linux v", "0.1.0"),
            0
        ),
        (
            ("version", "show"),
            ("101-linux v0.1.0",),
            0
        ),
        (
            ("unknowncmd",),
            ("No such command", "Hint: Run 'cli.py --help' to see available commands."),
            2
        ),
        (
            ("show", "ls"),
            ("ls", "List"),
            0
        ),
        (
            ("show", "grep"),
            ("Search",),
            0
        ),
        (
            ("show", "foobar"),
            ("Unknown",),
            1
        ),
        (
            ("search", "grep"),
            ("grep:",),
            0
        ),
        (
            ("search", "this-should-not-exist-xyz"),
            ("No commands found.",),
            1
        )
    )
)
def test_check_cli(args: tuple[str], expected_strings: tuple[str], exit_code: int):
    """Helper to run CLI with subprocess and capture output."""
    result = subprocess.run(
        [sys.executable, CLI_APP_PATH, *args],
        capture_output=True,
        text=True,
        cwd=os.path.dirname(__file__),
    )
    out_raw = result.stdout + result.stderr
    out = clean_output(out_raw)

    assert result.returncode == exit_code
    for string in expected_strings:
        assert string in out
