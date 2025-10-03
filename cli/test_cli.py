#!/usr/bin/env python3
"""Basic tests for the CLI module."""

import os
import subprocess
import sys


def run_cli(args):
    """Helper to run CLI with subprocess and capture output."""
    result = subprocess.run(
        [sys.executable, "cli.py", *args],
        capture_output=True,
        text=True,
        cwd=os.path.dirname(__file__),
    )
    return result


def test_cli_help():
    """Test that the CLI shows help."""
    result = run_cli(["--help"])
    assert result.returncode == 0
    assert "101 Linux Commands CLI" in result.stdout


def test_hello_command():
    """Test the hello command."""
    result = run_cli(["hello", "greet"])
    assert result.returncode == 0
    assert "Hello, World!" in result.stdout


def test_hello_command_with_name():
    """Test the hello command with a custom name."""
    result = run_cli(["hello", "greet", "--name", "Linux"])
    assert result.returncode == 0
    assert "Hello, Linux!" in result.stdout


def test_hello_help():
    """Test the hello command help."""
    result = run_cli(["hello", "--help"])
    assert result.returncode == 0
    assert "Hello command group" in result.stdout


def test_list_command():
    """Test the list command."""
    result = run_cli(["list"])
    assert result.returncode == 0
    assert "ls - List directory contents." in result.stdout
    assert "cd - Change directory." in result.stdout
    assert "pwd - Print working directory." in result.stdout
    assert "cat - Concatenate and display files." in result.stdout


def test_version_command():
    """Test the version command"""
    result = run_cli(["version"])
    assert result.returncode == 0
    assert "101-linux v" in result.stdout
    assert "0.1.0" in result.stdout


def test_version_show_command():
    """Test the version show subcommand."""
    result = run_cli(["version", "show"])
    assert result.returncode == 0
    assert "101-linux v0.1.0" in result.stdout


# ----------------------------
# Tests for `show` subcommand
# ----------------------------


def test_show_ls():
    """Test the show command with ls."""
    result = run_cli(["show", "ls"])
    assert result.returncode == 0
    assert "ls" in result.stdout
    assert "List" in result.stdout


def test_show_grep():
    """Test the show command with grep."""
    result = run_cli(["show", "grep"])
    assert result.returncode == 0
    assert "grep" in result.stdout
    assert "Search" in result.stdout or "Print" in result.stdout


def test_show_invalid():
    """Test the show command with an invalid command."""
    result = run_cli(["show", "foobar"])
    assert result.returncode != 0
    combined_output = result.stdout + result.stderr
    assert "Unknown" in combined_output or "Error" in combined_output


if __name__ == "__main__":
    test_cli_help()
    test_hello_command()
    test_hello_command_with_name()
    test_hello_help()
    test_list_command()
    test_version_command()
    test_version_show_command()
    test_show_ls()
    test_show_grep()
    test_show_invalid()
    print("✅ All tests passed!")
