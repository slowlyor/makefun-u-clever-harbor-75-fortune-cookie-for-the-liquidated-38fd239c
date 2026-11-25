#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes a single fortune cookie line to /output/entry.txt.
Deterministic, standard library only.
"""

import os

FORTUNE = "A great fortune is coming your way \u2014 it just walked out of your wallet."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
