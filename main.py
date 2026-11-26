#!/usr/bin/env python3
"""Worst pizza topping, one line: the topping gets sued by the other toppings.

The program assembles the line from its parts and drops it into
$MAKEFUN_OUTPUT_DIR/entry.txt. It never touches the repo itself, because
the grader runs it with the repository mounted read-only.
"""

import os
import unicodedata

OPENING = "Pineapple's lawyer called"
MIDDLE = "even the anchovies filed ticket #4821"
CLOSING = "against the gummy bears on this pizza."


def compose_line():
    """Join the three beats of the joke into a single line."""
    return " — ".join([OPENING, MIDDLE]) + " " + CLOSING


def check_line(line):
    """Refuse lines that are empty, absurdly long, or carry invisible marks."""
    if not line or len(line) >= 200:
        raise ValueError("line must be 1-199 characters")
    for mark in line:
        if unicodedata.category(mark) == "Cf" or mark == "\u00a0":
            raise ValueError("invisible formatting character in line")


def publish(line):
    """Write the line out and read it back to prove the bytes survived."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(folder, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    with open(target, "rb") as handle:
        saved = handle.read()
    if saved.decode("utf-8") != line:
        raise ValueError("written bytes do not match the line")


def main():
    line = compose_line()
    check_line(line)
    publish(line)


if __name__ == "__main__":
    main()
