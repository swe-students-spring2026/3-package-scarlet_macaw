# devmood - Emotional Support for Developers

![GitHub Actions](https://github.com/swe-students-spring2026/3-package-scarlet_macaw/actions/workflows/event-logger.yml/badge.svg)

`devmood` is a playful Python package that gives developers quick emotional support during coding sessions.  
It helps turn debugging stress into momentum with encouragement, small-win celebrations, sarcastic advice, and ASCII hugs.

## Project Description

`devmood` includes four functions that all accept arguments and return a `str`:

- `debug_encouragement(error_type: str) -> str`  
  Returns a supportive message based on the error type.
- `celebrate_small_win(task: str) -> str`  
  Celebrates progress for a completed coding task.
- `passive_aggressive_advice(topic: str) -> str`  
  Returns playful sarcastic advice tied to a topic.
- `ascii_hug(name: str) -> str`  
  Returns a personalized ASCII hug.

## PyPI



## Install and Import

Install from PyPI:

```bash
pip install devmood
```

Import in your own project:

```python
from devmood import (
    debug_encouragement,
    celebrate_small_win,
    passive_aggressive_advice,
    ascii_hug,
)
```

## Function Documentation and Exact Examples

### `debug_encouragement(error_type: str) -> str`

```python
from devmood import debug_encouragement

message = debug_encouragement("TypeError")
print(message)
```

### `celebrate_small_win(task: str) -> str`

```python
from devmood import celebrate_small_win

message = celebrate_small_win("wrote my first passing test")
print(message)
```

### `passive_aggressive_advice(topic: str) -> str`

```python
from devmood import passive_aggressive_advice

message = passive_aggressive_advice("variable naming")
print(message)
```

### `ascii_hug(name: str) -> str`

```python
from devmood import ascii_hug

message = ascii_hug("Laura")
print(message)
```

## Example Program Using All Functions

- Example script: [`example.py`](./example.py)

Run it:

```bash
python example.py
```

## Contributing and Local Development

### 1) Clone and enter the project

```bash
git clone https://github.com/swe-students-spring2026/3-package-scarlet_macaw.git
cd 3-package-scarlet_macaw
```

### 2) Set up virtual environment and dependencies

```bash
pip install pipenv
pipenv install --dev
pipenv shell
```

### 3) Run tests

```bash
pytest
```

### 4) Build package artifacts

```bash
python -m build
```

### 5) Collaboration workflow

```bash
git checkout -b feature/your-feature-name
# make changes
pytest
git add .
git commit -m "Describe your change"
git push -u origin feature/your-feature-name
```

Then open a Pull Request to `main` and request teammate review.

## Cross-Platform Run Instructions

These commands work on macOS, Linux, and Windows (PowerShell), as long as Python 3.9+ and `pip` are installed:

1. `pip install pipenv`
2. `pipenv install --dev`
3. `pipenv run pytest`
4. `pipenv run python example.py`

## Environment Variables and Starter Data



## Secret Configuration Files



## Teammates

- [Laura Liu](https://github.com/lauraliu518)
- [Yutong Liu](https://github.com/Abbyyyt)
- [Bryce Lin](https://github.com/blin03)
- [Yuliang Liu](https://github.com/yl11529)
- [Teammate Five](https://github.com/username5)