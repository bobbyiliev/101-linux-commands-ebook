#!/usr/bin/env python3
"""Generate a command index JSON from the ebook markdown content.

Best-effort extractor that pulls title, description, usage, example, and notes
from each markdown file under ebook/en/content. Writes output to cli/data/commands.json
"""

import json
import re
import sys
from pathlib import Path


def _extract_title(lines: list[str]) -> str | None:
    """Extract the first heading line starting with '#'."""
    for ln in lines:
        if ln.strip().startswith("#"):
            return ln.strip().lstrip("#").strip()
    return None


def _extract_command_name(title: str | None, path: Path) -> str:
    """Extract command name from title or fallback to filename pattern."""
    if title:
        # Try to infer command name from code span in title like `ls`
        m = re.search(r"`([a-zA-Z0-9_\-]+)`", title)
        if m:
            return m.group(1)
        # Fallback: take last token of title
        tokens = re.findall(r"\w+", title)
        if tokens:
            return tokens[-1].lower()

    # Fallback: filename pattern 001-the-ls-command.md -> ls
    m = re.search(r"-the-([a-zA-Z0-9_\-]+)-command", path.name)
    if m:
        return m.group(1)

    return path.stem


def _extract_description(lines: list[str]) -> str:
    """Extract first paragraph after title."""
    try:
        idx = 0
        while idx < len(lines) and not lines[idx].strip().startswith("#"):
            idx += 1
        # Move to next line after title
        idx += 1
        # Collect lines until empty line
        para = []
        while idx < len(lines):
            line = lines[idx].strip()
            if line == "":
                if para:
                    break
                idx += 1
                continue
            if line.startswith("###") or line.startswith("##"):
                if para:
                    break
            para.append(line)
            idx += 1
        return " ".join(para).strip()
    except Exception:
        return ""


def _extract_usage(text: str) -> str:
    """Extract usage information from Syntax or Usage sections."""
    usage_match = re.search(
        r"###\s*Syntax\s*:\s*\n(```[\s\S]*?```)", text, flags=re.IGNORECASE
    )
    if usage_match:
        return usage_match.group(1).strip().strip("`")

    m2 = re.search(r"Usage\s*[:|-]\s*(.+)", text, flags=re.IGNORECASE)
    if m2:
        return m2.group(1).strip()

    return ""


def _extract_example(text: str) -> str:
    """Extract example from Examples section or first code block."""
    examples_section = re.search(
        r"###\s*Examples[:\s]*\n([\s\S]*?)(?:\n###|\n##|$)", text, flags=re.IGNORECASE
    )
    if not examples_section:
        return ""

    # Find first fenced code block inside
    fb = re.search(
        r"```(?:bash|sh|shell|).*?\n([\s\S]*?)```",
        examples_section.group(1),
        flags=re.IGNORECASE,
    )
    if fb:
        return fb.group(1).strip()

    # Fallback: first inline code occurrence
    ic = re.search(r"`([^`]+)`", examples_section.group(1))
    if ic:
        return ic.group(1).strip()

    return ""


def _extract_notes(text: str) -> str:
    """Extract notes from Additional Flags/Notes sections or bullet points."""
    notes_section = re.search(
        r"###\s*(Additional Flags|Notes|Notes:|Additional).*?\n([\s\S]*?)(?:\n###|\n##|$)",
        text,
        flags=re.IGNORECASE,
    )
    if notes_section:
        return notes_section.group(2).strip()

    # Collect bullet points
    bullets = re.findall(r"^\s*[-\*]\s+(.+)$", text, flags=re.MULTILINE)
    if bullets:
        return "; ".join(bullets[:10])

    return ""


def extract_from_markdown(path: Path) -> dict:
    """Extract command information from a markdown file."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    title = _extract_title(lines)
    name = _extract_command_name(title, path)
    desc = _extract_description(lines)
    usage = _extract_usage(text)
    example = _extract_example(text)
    notes = _extract_notes(text)

    return {
        "name": name,
        "description": desc,
        "usage": usage,
        "example": example,
        "notes": notes,
        "source": str(path.name),
    }


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    content_dir = root / "ebook" / "en" / "content"
    if not content_dir.exists():
        print(f"Content directory not found: {content_dir}")
        return 2

    out_dir = Path(__file__).resolve().parents[1] / "data"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "commands.json"

    items = []
    for md in sorted(content_dir.glob("*.md")):
        try:
            item = extract_from_markdown(md)
            items.append(item)
        except Exception as e:
            print(f"Failed to parse {md}: {e}")

    # write JSON
    out_file.write_text(
        json.dumps(items, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"Wrote {len(items)} commands to {out_file}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
