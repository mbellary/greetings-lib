# Greetings Lib

![Tests](https://github.com/mbellary/greetings-lib/actions/workflows/tests.yml/badge.svg)
[![Coverage Status](https://img.shields.io/codecov/c/github/mbellary/greetings-lib)](https://codecov.io/gh/<YOUR-USERNAME>/greetings-lib)


A simple Python package that provides a greeting function and includes automated testing and code quality enforcement.

## 🚀 Installation

Use `uv` to install the package in editable mode:

```bash
uv pip install -e .
```

## 🧑‍💻 Usage

Import and use the greet function:

```python
from greetings_lib.greetings import greet
print(greet("World"))  # Output: Hello from World!
```
Or use the CLI entry point:
```bash
worker World
```

## 🧪 Running Tests + Coverage
Install development dependencies:
```bash
uv pip install -e ".[dev]"
```
Run tests with coverage:
```bash
uv run pytest --cov=greetings_lib --cov-report=term
```

## 🧹 Formatting & Linting (Ruff)
Format code:
```bash
uv run ruff format .
```
Lint:
```bash
uv run ruff check .
```
CI will fail if formatting/linting errors exist.

## 🔄 Pre-commit Hooks
Auto-format & autofix before every commit:
```bash
uv pip install pre-commit
pre-commit install
```
Hooks used:
### ruff (lint with automatic fixes)
### ruff-format (code formatting)

## 🛠 Development Workflow
```bash
uv pip install -e ".[dev]"
uv run ruff format .
uv run ruff check .
uv run pytest --cov
```

## 🏗 Project Structure
```bash
greetings-lib/
│─ .github/workflows/tests.yml
│─ docs/
├─ src/greetings_lib/
│   ├─ __init__.py
│   └─ greetings.py
├─ tests/test_greetings.py
│─ .coverage
│─ .pre-commit-config.yaml
├─ pyproject.toml
├─ README.md
└─ uv.lock
```

## 🔄 Continuous Integration
GitHub Actions automatically:
### ✔ Installs dependencies 
### ✔ Checks formatting and linting with Ruff
### ✔ Runs tests with pytest + coverage
### ✔ Upload coverage results to Codecov

