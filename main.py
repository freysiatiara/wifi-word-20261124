"""One word for your Wi-Fi.

The word is "flaky": home Wi-Fi works beautifully right up until the
moment you actually need it, then drops for no reason at all, comes
back on its own, and pretends nothing happened. Funny because it is
true, and true because everyone has lived it.

Writes the single word to /output/entry.txt (UTF-8, 1-20 characters,
no whitespace), as the make.fun bounty requires. Standard library only.
"""

import os

WORD = "flaky"


def main() -> None:
    word = WORD.strip()
    if not word:
        raise ValueError("word must not be empty")
    if len(word) > 20:
        raise ValueError("word must be at most 20 characters")
    if any(ch.isspace() for ch in word):
        raise ValueError("word must contain no whitespace")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(word)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
