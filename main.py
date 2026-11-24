#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line developer excuse for code breaking in
production to /output/entry.txt (and a local copy, entry.txt, for
verification). Stdlib only, no network, deterministic.
"""

import hashlib
import os
import sys

# The entry: one original single-line developer excuse.
# Twist on the worn "it worked in staging" line: production is the same
# stage, only now there are witnesses. Revised to drop "just" so every
# word earns its place and the punch lands faster.
ENTRY = "It worked in staging; production is staging with witnesses."


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= 200):
        print(f"entry length {len(text)} out of 1-200 range", file=sys.stderr)
        return 1
    if text.strip() != text or "\n" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    data = text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "wb") as f:
        f.write(data)
    print(f"wrote {len(data)} bytes, sha256={hashlib.sha256(data).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
