#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse - make.fun bounty entry.

Writes one line (under 200 characters) to /output/entry.txt: the excuse
a dog gives after being caught eating the homework, in the dog's own
voice. The dog believes it did nothing wrong: the homework was lying on
the floor, and the floor is a dog's dinner table.

Pure Python standard library only. Deterministic: the same bytes on
every run. No network, no secrets, reads nothing outside this repo.
"""

import os

EXCUSE = (
    "It was lying on the floor, and the floor is a dog's dinner table, "
    "so I sat down, ate at the table like a gentleman, and I regret nothing."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    if not 1 <= len(EXCUSE) <= 200:
        raise SystemExit(f"excuse is {len(EXCUSE)} characters, must be 1-200")
    if "\n" in EXCUSE or not EXCUSE.strip():
        raise SystemExit("excuse must be one non-blank line")
    if EXCUSE != EXCUSE.strip() or "  " in EXCUSE:
        raise SystemExit("excuse must have no leading/trailing or double space")
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(EXCUSE)
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    if written != EXCUSE.encode("utf-8"):
        raise SystemExit("written bytes differ from the excuse")


if __name__ == "__main__":
    main()
