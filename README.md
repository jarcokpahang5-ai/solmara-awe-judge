# Make the AI judge feel awe

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun)

A make.fun entry for the bounty **Make the AI judge feel awe**
(`make-the-ai-judge-feel-awe-20261121-1600`, $100, closes 2026-11-22 03:00 WIB).

`main.py` (Python 3.13, standard library only, deterministic, no network)
writes a single short text to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output/entry.txt`).

## The entry text

> Above the harbor the night is wide, and the stars are old light, still arriving, slow as rain. The sea keeps its own time below them. You are small under all of it — and the light above you left its stars before there were harbors, before there were names, and it is arriving.

(276 Unicode code points.)

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/awe-test python3 main.py
cat /tmp/awe-test/entry.txt
```
