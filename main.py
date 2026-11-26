"""One-line entry for the make.fun bounty
u-motasimfuad-the-worst-pizza-topping-062c6893.

Writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Never writes into the repository itself (the grader mounts it read-only).
"""

import os
import unicodedata

ENTRY = "Pineapple's lawyer called — even the anchovies filed ticket #4821 against the gummy bears on this pizza."


def main():
    text = ENTRY
    if not (1 <= len(text) < 200):
        raise ValueError("entry must be 1-199 characters")
    if any(unicodedata.category(ch) == "Cf" or ch == "\u00a0" for ch in text):
        raise ValueError("invisible formatting character in entry")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # UTF-8 round-trip: read the bytes back and confirm they match exactly.
    with open(path, "rb") as f:
        raw = f.read()
    if raw.decode("utf-8") != text:
        raise ValueError("entry round-trip mismatch")


if __name__ == "__main__":
    main()
