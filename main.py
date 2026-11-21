#!/usr/bin/env python3
"""make.fun entry: Make the AI judge feel awe.

Writes a single short text to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Pure Python standard library,
deterministic, no network.
"""

import os

TEXT = (
    "Above the harbor the night is wide, and the stars are old light, "
    "still arriving, slow as rain. The sea keeps its own time below "
    "them. You are small under all of it \u2014 and the light above you "
    "left its stars before there were harbors, before there were "
    "names, and it is arriving."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
