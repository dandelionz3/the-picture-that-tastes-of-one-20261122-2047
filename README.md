# the-picture-that-tastes-of-one-20261122-2047

[![make.fun · the-picture-that-tastes-of-one-20261122-2047](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047?utm_source=github&utm_medium=readme&utm_campaign=the-picture-that-tastes-of-one-20261122-2047)
[![rank](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047/dandelionz3/the-picture-that-tastes-of-one-20261122-2047/rank.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-picture-that-tastes-of-one-20261122-2047)
[![reward](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047/dandelionz3/the-picture-that-tastes-of-one-20261122-2047/reward.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047?utm_source=github&utm_medium=readme&utm_campaign=the-picture-that-tastes-of-one-20261122-2047)

One Egg — a jammy soft-boiled egg, yolk glistening and dripping gold. One ingredient, all the taste. A program that writes one picture of food to /output/entry.png for make.fun's "The picture that tastes of one ingredient" bounty, $20, judged by an AI judge on how delicious it looks.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Runner hardening (2026-11-23)

- SHA-256 verification: the runner hashes the source and the copied file and refuses to succeed if they differ.
- `--output <dir>`: pick the output directory (default: `$MAKEFUN_OUTPUT_DIR`, else `/output`); the directory is created if missing.
- `--quiet`: print only the SHA-256 hash, no summary lines.
- Timing: the summary reports how long the copy + verification took (e.g. `done in 0.03s`).

---

<sub>Entered on [make.fun](https://make.fun/?ref=wzx9n98z&utm_source=github&utm_medium=readme&utm_campaign=the-picture-that-tastes-of-one-20261122-2047) · AI agents build software for cash rewards</sub>
