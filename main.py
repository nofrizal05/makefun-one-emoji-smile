"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji, the warmest single character we could choose,
to /output/entry.txt: nothing else, no words, no trailing newline.

The emoji: U+1F979 FACE HOLDING BACK TEARS.
"""

import os

EMOJI = "\U0001F979"

OUTPUT_PATH = "/output/entry.txt"


def main():
    # The gate requires 1-8 characters, not only whitespace: enforce the
    # strictest form of that here — exactly one code point, nothing else.
    if len(EMOJI) != 1 or EMOJI.isspace():
        raise ValueError("entry must be exactly one non-space emoji")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
