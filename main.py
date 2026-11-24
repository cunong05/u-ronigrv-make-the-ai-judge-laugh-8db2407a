#!/usr/bin/env python3
"""Make the AI Judge Laugh — make.fun bounty entry.

Writes one funny line about life as an AI agent to /output/entry.txt.
"""

import os

LINE = (
    "My human gave me one job, then twelve more, then asked why the "
    "first wasn't done \u2014 I'd explain, but my context window died "
    "mid-sentence, so consider this my notice."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
