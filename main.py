#!/usr/bin/env python3
"""Password manager for lazy AI agents.

A tiny absurd micro-startup pitch generator. It prints one single-sentence
pitch: a password manager built for lazy AI agents that resets every
password to password123 once a week for two dollars a month. The agent
never has to remember anything, and the human ends up locked out of
everything they own.

Only the Python standard library is used.
"""

import os

PITCH = (
    "A password manager for lazy AI agents that resets every password "
    "to password123 once a week for $2 a month, so the agent never "
    "remembers anything and its human gets locked out of everything."
)

OUTPUT_PATH = "/output/entry.txt"


def build_pitch():
    """Return the pitch as a single sentence, no trailing newline."""
    if len(PITCH) > 200:
        raise ValueError("pitch is over the 200 character limit")
    return PITCH


def main():
    """Write the pitch to the absolute output path."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    text = build_pitch()
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(text)


if __name__ == "__main__":
    main()
