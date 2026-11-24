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
    if not word.isalpha():
        raise ValueError("word must be letters only (no punctuation or digits)")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(word)
    os.chmod(path, 0o644)
    # Read back and confirm the file holds exactly the word we meant.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != word:
            raise ValueError("written entry does not match the word")


if __name__ == "__main__":
    main()
