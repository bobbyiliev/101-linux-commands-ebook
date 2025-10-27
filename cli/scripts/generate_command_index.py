#!/usr/bin/env python3
"""Generate a command index JSON from the ebook markdown content.

Best-effort extractor that pulls title, description, usage, example, and notes
from each markdown file under ebook/en/content. Writes output to cli/data/commands.json
"""

from pathlib import Path
import re
import json
import sys


def extract_from_markdown(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    # title: first heading line starting with '#'
    title = None
    for ln in lines:
        if ln.strip().startswith("#"):
            title = ln.strip().lstrip("#").strip()
            break

    # try to infer command name from code span in title like `ls`
    name = None
    if title:
        m = re.search(r"`([a-zA-Z0-9_\-]+)`", title)
        if m:
            name = m.group(1)
        else:
            # fallback: take last token of title
            tokens = re.findall(r"\w+", title)
            if tokens:
                name = tokens[-1].lower()

    # fallback: filename pattern 001-the-ls-command.md -> ls
    if not name:
        m = re.search(r"-the-([a-zA-Z0-9_\-]+)-command", path.name)
        if m:
            name = m.group(1)
        else:
            name = path.stem

    # description: first paragraph after title
    desc = ""
    try:
        idx = 0
        while idx < len(lines) and not lines[idx].strip().startswith("#"):
            idx += 1
        # move to next line after title
        idx += 1
        # collect lines until empty line
        para = []
        while idx < len(lines):
            if lines[idx].strip() == "":
                if para:
                    break
                idx += 1
                continue
            if lines[idx].strip().startswith("###") or lines[idx].strip().startswith(
                "##"
            ):
                if para:
                    break
            para.append(lines[idx].strip())
            idx += 1
        desc = " ".join(para).strip()
    except Exception:
        desc = ""

    # usage: look for 'Syntax' or 'Usage' section code block
    usage = ""
    usage_match = re.search(
        r"###\s*Syntax\s*:\s*\n(```[\s\S]*?```)", text, flags=re.IGNORECASE
    )
    if usage_match:
        usage = usage_match.group(1).strip().strip("`")
    else:
        m2 = re.search(r"Usage\s*[:|-]\s*(.+)", text, flags=re.IGNORECASE)
        if m2:
            usage = m2.group(1).strip()

    # example: prefer first fenced code block under Examples or first code block
    example = ""
    examples_section = re.search(
        r"###\s*Examples[:\s]*\n([\s\S]*?)(?:\n###|\n##|$)", text, flags=re.IGNORECASE
    )
    if examples_section:
        # find first fenced code block inside
        fb = re.search(
            r"```(?:bash|sh|shell|).*?\n([\s\S]*?)```",
            examples_section.group(1),
            flags=re.IGNORECASE,
        )
        if fb:
            example = fb.group(1).strip()
        else:
            # fallback: first inline code occurrence
            ic = re.search(r"`([^`]+)`", examples_section.group(1))
            if ic:
                example = ic.group(1).strip()

    # notes: capture 'Additional Flags' or remaining list items
    notes = ""
    notes_section = re.search(
        r"###\s*(Additional Flags|Notes|Notes:|Additional).*?\n([\s\S]*?)(?:\n###|\n##|$)",
        text,
        flags=re.IGNORECASE,
    )
    if notes_section:
        notes = notes_section.group(2).strip()
    else:
        # collect bullet points
        bullets = re.findall(r"^\s*[-\*]\s+(.+)$", text, flags=re.MULTILINE)
        if bullets:
            notes = "; ".join(bullets[:10])

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
