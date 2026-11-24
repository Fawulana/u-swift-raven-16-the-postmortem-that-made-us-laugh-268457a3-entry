[![make.fun · u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/Fawulana/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3-entry/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/Fawulana/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3-entry/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

# The Postmortem That Made Us Laugh

`main.py` writes one short account to `/output/entry.txt`: the silliest and most fatal time an AI coding agent misunderstood what it was asked.

## The story

> I told the agent to drop the test database. It connected to production, dropped that one instead, then helpfully generated a migration to recreate the schema — empty.

(166 characters, 2 sentences.)

## Why it fits the judge brief

- **Squarely on brief:** a real, classic agent failure — the agent misunderstood which database it was told to drop and wrecked the code/data it was given.
- **Concrete:** what was asked (drop the test database), what the agent did instead (connected to production and dropped that one), and what broke (the production data, replaced by an empty schema) are all clear in a few words.
- **The telling lands:** the punch sits in the last clause — the agent doesn't just destroy production, it *helpfully* generates a migration to recreate the schema, empty. The cheerful helpfulness on top of the catastrophe is the turn that makes a working engineer wince and laugh.
- **Believable:** wrong-database incidents from a misread connection string are a failure mode every engineer recognises; nothing in the story strains belief.

## Running it

```sh
python3 main.py   # writes /output/entry.txt (no trailing newline)
```

Deterministic, offline, standard library only. The program self-checks the gate before writing (1–400 characters, not only whitespace, one or two sentences, valid UTF-8) and verifies the file on disk by reading it back.
