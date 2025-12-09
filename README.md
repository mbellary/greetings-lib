# Greetings Lib

![Tests](https://github.com/<YOUR-USERNAME>/greetings-lib/actions/workflows/tests.yml/badge.svg)

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

## 🧪 Running Tests
Install development dependencies:
```bash
uv pip install -e ".[dev]"
```
Run tests:
```bash
uv run pytest -v
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

## 🛠 Development Workflow
```bash
uv pip install -e ".[dev]"
uv run ruff format .
uv run ruff check .
uv run pytest
```

## 🏗 Project Structure
```bash
greetings-lib/
├─ src/greetings_lib/
│   ├─ __init__.py
│   └─ greetings.py
├─ tests/test_greetings.py
├─ pyproject.toml
├─ README.md
└─ .github/workflows/tests.yml
```

## 🔄 Continuous Integration
GitHub Actions automatically:
### ✔ Installs dependencies 
### ✔ Checks formatting and linting with Ruff
### ✔ Runs tests with pytest

