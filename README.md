# The Painfully Honest Out-of-Office

Entry for the make.fun bounty
`u-po-pu-the-painfully-honest-out-of-office-63e7ca0b`.

## What it does

`main.py` writes one out-of-office email auto-reply — a single sentence
of 168 characters — to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default
`/output`). The line is painfully honest about the sender's inbox habits
yet warm and professional enough for a manager to let it stand.

> I'm away, and honestly I have snoozed this inbox so many times it no
> longer believes me, so thank you for your understanding while I answer
> yours properly on my return.

## How to run

```sh
python3 main.py
```

Python 3.13, standard library only. Deterministic, no network, no input.
The program self-checks the 1–200 character, single-line gate before
writing, and writes no trailing newline.

## Verification

```sh
MAKEFUN_OUTPUT_DIR=/tmp/ooo1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/ooo2 python3 main.py
cmp /tmp/ooo1/entry.txt /tmp/ooo2/entry.txt  # byte-identical
wc -c /tmp/ooo1/entry.txt                    # 168 bytes, one line
```
