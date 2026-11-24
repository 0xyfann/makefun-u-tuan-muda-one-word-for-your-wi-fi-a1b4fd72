"""One Word for Your Wi-Fi — entry program.

Writes a single original word describing home Wi-Fi to
``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (default ``/output``).
Stdlib only.
"""

import os
import sys

WORD = "Ghosting"


def validate(word: str) -> str:
    """Enforce the competition gate: 1-20 chars, one word, not blank."""
    word = word.strip()
    if not word:
        raise ValueError("entry word is empty")
    if len(word) > 20:
        raise ValueError(f"entry word too long: {len(word)} chars (max 20)")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    return word


def main() -> int:
    word = validate(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(word)
    print(f"wrote {len(word)}-char entry to {path}: {word}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
