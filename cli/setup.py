#!/usr/bin/env python3
"""Setup script for 101 Linux Commands CLI tool."""

from setuptools import find_packages, setup

setup(
    name="linux-commands-cli",
    version="0.1.0",
    description="Interactive CLI tool for 101 Linux Commands eBook",
    author="Bobby Iliev",
    author_email="bobby@bobbyiliev.com",
    packages=find_packages(),
    install_requires=[
        "typer[all]==0.12.3",
    ],
    entry_points={
        "console_scripts": [
            "linux-cli=cli.cli:app",
            "l101=cli.cli:app",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: System :: Systems Administration",
        "Topic :: Education",
    ],
)
