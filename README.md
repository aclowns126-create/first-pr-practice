# first-pr-practice

A tiny toy project used to practice makeing and submitting a pull request on GitHub.

## What's here

- `stringutils.py` — a couple of small string helper functions.
- `tests/test_stringutils.py` — tests for those helpers.

## Usage

```python
from stringutils import shout, is_palindrome

shout("hello")          # "HELLO!"
is_palindrome("level")  # True
```

## Running tests

```bash
python -m unittest discover tests
```
