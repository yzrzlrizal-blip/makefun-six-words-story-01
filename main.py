#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Reads the six-word story shipped in story.txt and writes it to
$MAKEFUN_OUTPUT_DIR/entry.txt, the file the sealed scorer reads.
Pure standard library; nothing is generated at grade time.
"""

import os
import sys


def load_story():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "story.txt")
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read().strip()


def main():
    story = load_story()
    words = story.split()
    if len(words) != 6:
        print(f"error: story must be exactly six words, got {len(words)}", file=sys.stderr)
        return 1
    if "\n" in story or "\r" in story:
        print("error: story must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(story) <= 60:
        print(f"error: story must be 1-60 characters, got {len(story)}", file=sys.stderr)
        return 1
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    target = os.path.join(output_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(story)
    print(f"story: {story}")
    print(f"wrote {len(words)}-word story ({len(story)} chars) to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
