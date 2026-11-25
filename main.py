"""Weirdest Job Title entry for make.fun.

Writes exactly one job title to /output/entry.txt. Before writing, it checks the
contest gate: UTF-8 text of 1 to 60 characters that is not only white space,
on a single line. If the title ever fails, the program exits non-zero instead
of writing an invalid entry.
"""
import os
import sys

ENTRY = "Speech Therapist for Retired Pirate Parrots"
MAX_CHARS = 60
OUT = os.environ.get("ENTRY_OUT", "/output/entry.txt")


def gate(text: str) -> str:
    text = text.strip()
    if not text:
        raise ValueError("entry is empty or white space only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, limit is {MAX_CHARS}")
    text.encode("utf-8")  # must round-trip as UTF-8
    return text


def main() -> int:
    try:
        title = gate(ENTRY)
    except ValueError as err:
        print(f"gate failed: {err}", file=sys.stderr)
        return 1
    out_dir = os.path.dirname(OUT)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(title)
    print(f"wrote {len(title)} chars to {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
