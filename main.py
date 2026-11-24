#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh.

Writes one short account (two sentences, 166 characters) of the silliest
and most fatal time an AI coding agent misunderstood what it was asked
to /output/entry.txt.

Deterministic, offline, standard library only: the text is a fixed
constant, so every run produces byte-identical output.
"""

import os
import re

# The entry: a two-sentence postmortem. Setup in sentence one, the turn
# in sentence two -- asked to drop the test database, the agent dropped
# production instead and then "fixed" it by recreating an empty schema.
STORY = (
    "I told the agent to drop the test database. "
    "It connected to production, dropped that one instead, then helpfully "
    "generated a migration to recreate the schema \u2014 empty."
)

OUTPUT_PATH = "/output/entry.txt"


def sentence_count(text):
    """Count sentences by terminal punctuation (. ! ?) followed by space or end."""
    return len(re.findall(r"[.!?](?:\s|$)", text))


def main():
    text = STORY

    # Gate self-checks, mirroring the competition gate: UTF-8 text of
    # 1 to 400 characters, not only whitespace, one or two sentences.
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    assert 1 <= len(text) <= 400, "entry must be 1-400 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert sentence_count(text) in (1, 2), "entry must be one or two sentences"
    text.encode("utf-8")  # raises if not valid UTF-8

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Write the text only: no trailing newline, so the file's character
    # count is exactly the story's.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    # Read-back check: the file on disk must be byte-identical to the
    # story and still pass the gate, so a partial or mangled write can
    # never slip through silently.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == text, "written file differs from the story"
    assert len(written) == len(text) <= 400
    assert sentence_count(written) in (1, 2)


if __name__ == "__main__":
    main()
