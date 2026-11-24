#!/usr/bin/env python3
"""The Houseplant Out-of-Office -- make.fun entry.

Writes one out-of-office auto-reply, as if a houseplant sent it,
to /output/entry.txt. Deterministic, no network, no input.

The line (119 chars): a fern, unwatered since March, tells the sender
their email has been composted and it will reply when it rains indoors.
Plant neglect drives the joke; the compost twist is the surprise.
"""

import os

LINE = "Out of office: I'm the office fern, unwatered since March. Your email is now compost. I'll reply when it rains indoors."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 120, f"entry must be 1-120 chars, got {len(text)}"
    path = OUTPUT_PATH
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        # Local run without a sandbox /output: write next to the repo.
        path = os.path.join(os.getcwd(), "output", "entry.txt")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
