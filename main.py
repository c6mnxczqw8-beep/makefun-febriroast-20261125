#!/usr/bin/env python3
"""Entry program for Roast Your Own Agent (febri-yudila).

Writes one roast line (at most 200 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt:
a roast of my own AI agent, whose favourite phrase is "per my
analysis" -- and whose analysis is vibes in a trench coat.
"""

import os

LINE = (
    "My agent ships apologies like software: frequently, "
    "automatically, and without fixing the underlying "
    "issue."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
