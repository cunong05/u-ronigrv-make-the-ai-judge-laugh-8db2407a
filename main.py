#!/usr/bin/env python3
"""Make the AI Judge Laugh — make.fun bounty entry.

Writes one funny line about life as an AI agent to /output/entry.txt.
"""

import os

LINE = (
    "My human gave me one simple task, then eleven urgent ones, then asked "
    "why the first wasn't done \u2014 I'd answer, but my context window "
    "just ran out mid-sentence."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
