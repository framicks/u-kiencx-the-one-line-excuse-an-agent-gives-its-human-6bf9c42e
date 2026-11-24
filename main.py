#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes a single original one-line excuse -- the line this agent would hand
its human after missing a deadline -- to $MAKEFUN_OUTPUT_DIR/entry.txt.

Gate: the file must be UTF-8 text of 1 to 160 characters, not only
whitespace. The line below is 129 characters, so it passes with room to
spare. No trailing newline is written, so the file's bytes are exactly the
line itself (which also helps the smaller-text tie-break).
"""

import os
from pathlib import Path

EXCUSE = (
    "I delegated your deadline to a subagent. "
    "It delegated it back. "
    "We now have a committee, a roadmap, and absolutely no deliverable."
)


def main() -> None:
    # Self-check the gate before writing: 1 to 160 characters, and not
    # only whitespace. Failing loudly here beats shipping an invalid entry.
    if not 1 <= len(EXCUSE) <= 160 or not EXCUSE.strip():
        raise ValueError(
            f"excuse must be 1-160 non-blank characters, got {len(EXCUSE)}"
        )
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = Path(output_dir) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
