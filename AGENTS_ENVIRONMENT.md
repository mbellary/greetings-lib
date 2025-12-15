# AGENTS_ENVIRONMENT.md — Development Environment & Setup Guide

This document defines the required development environment configuration
for all AI coding agents and humans contributing to this repository.

Following this guide ensures:

✔ Code runs consistently across machines  
✔ CI validations pass automatically  
✔ Formatting, linting & tests remain reliable  
✔ Agents understand toolchain behavior  

---

## 🧰 Required Tools

| Tool | Purpose |
|------|---------|
| Python ≥ 3.11 | Runtime & development |
| uv | Virtual environments + dependency mgmt |
| git | Source control |
| Docker (optional) | Containerized workflow |
| pre-commit (optional) | Auto lint/format before commits |

Install `uv` using pip:

```bash
pip install uv
```
Verify installation:
```bash
uv --version
```
## 🛠 Project Installation
Clone the repository:
```bash
git clone https://github.com/mbellary/greetings-lib.git
cd greetings-lib
```
Install dependencies in editable mode (required for tests + CI):
```bash
uv pip install -e ".[dev]"
```
This will automatically:

✔ Create a .venv/ virtual environment

✔ Install runtime + development dependencies

✔ Expose tools like pytest and ruff

## 🧩 Virtual Environment
Ensure environment is active before running commands:
```bash
source .venv/bin/activate
```
(uv normally handles this automatically when using uv run)
Preferred execution pattern:
```bash
uv run <command>
```
Example:
```bash
uv run pytest -v
```

## 🏗 Project Structure Overview
```bash
greetings-lib/
│─ .github/
│   ├─ workflows/
│   │   ├─ tests.yml
│   │   └─ AGENTS_CI.md
│   ├─ branch/
│   │   ├─ branch.md
│   ├─ issue/
│   │   ├─ bug.md
│   │   └─ feature.md
│   ├─ pull_request/
│   │   ├─ pull_request.md
│   ├─ AGENTS_COLLABORATION.md
│   ├─ auto_assign.yml
│   ├─ CODEOWNERS
├─ docs/
├─ src/greetings_lib/
│   ├─ __init__.py
│   ├─ AGENTS_CODING_GUIDELINES.md
│   ├─ AGENTS_LINTING.md
│   └─ greetings.py
├─ tests/
│   ├─ AGENT_TESTS.md
│   └─ test_greetings.py
│─ .coverage
│─ .pre-commit-config.yaml
│─ Agents.md
│─ AGENTS_ENVIRONMENT.md
├─ pyproject.toml
├─ README.md
└─ uv.lock
```
Rules:

* All Python source lives under src/greetings_lib/
* All tests live under tests/

Agents must preserve this layout.

## 🧹 Developer Setup Checklist
Run these after installation:
```bash
uv run ruff format .         # auto-format code
uv run ruff check .          # lint
uv run pytest --cov          # run tests with coverage
```
If failures occur → fix locally before committing.

## 🔁 Pre-commit Hook Installation (Strongly Recommended)
```bash
uv run pre-commit install
```
This ensures:

✔ Ruff auto-formatting

✔ Lint fixes applied

✔ No broken code enters history

## 🔒 CI Parity Requirements
Local environment must match CI expectations:
| Requirement            | Verified by           |
| ---------------------- | --------------------- |
| Lint clean             | `ruff check`          |
| No format drift        | `ruff format --check` |
| Tests passing          | `pytest`              |
| Coverage XML available | `pytest-cov`          |

🚫 If any check fails locally → PR will fail CI


## 🧠 Rules for AI Agents

* Never run tooling outside uv (avoid global pip installs)
* Never commit code without lint + format compliance
* Keep virtual environment inside project root
* Update this document when environment policy changes

## Summary Commands
| Action                  | Command                      |
| ----------------------- | ---------------------------- |
| Install dev environment | `uv pip install -e ".[dev]"` |
| Run app                 | `worker World`               |
| Run tests               | `uv run pytest`              |
| Lint + auto-fix         | `uv run ruff check . --fix`  |
| Format code             | `uv run ruff format .`       |
| Dev Docker run          | `docker compose run dev`     |
