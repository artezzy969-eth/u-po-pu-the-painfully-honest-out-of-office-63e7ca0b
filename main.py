#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office.

Writes a single out-of-office email auto-reply (one sentence, 168 chars)
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Stdlib only, deterministic, no network, no input.
"""

import os

LINE = (
    "I'm away, and honestly I have snoozed this inbox so many times "
    "it no longer believes me, so thank you for your understanding "
    "while I answer yours properly on my return."
)


def main() -> None:
    # Self-check the gate before writing: one sentence, 1-200 chars.
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.count("\n") == 0, "entry must be a single line"
    assert LINE.strip() == LINE, "entry must not be whitespace-padded"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
