# AGENTS.md — Agent Guide for greetings-lib

This document is intended for AI coding agents (e.g. Codex, Copilot, Cursor, Gemini-CLI, etc.).  
It describes how to build the project, run tests & linting, maintain code style, and use Docker.  
Use this as the canonical “machine-readable” specification of project conventions and workflows.

---

## 🧰 Project Overview

**Project name:** greetings-lib  
**Purpose:** A small Python library that provides a greeting function via library import or CLI entry point (`worker`).  
**Language:** Python ≥ 3.11  
**Package layout:** standard `src/` layout  
**Entry point CLI:** `worker = greetings_lib.greetings:greet` (defined in `pyproject.toml`)

---

## 🛠 Development Environment & Setup
* See `docs/agents/AGENTS_ENVIRONMENT.md` for details.
---

## ✅ Code Style, Linting & Formatting
* See `docs/agents/AGENTS_LINTING.md` for details.
---

## 🧪 Testing & Coverage
* See `docs/agents/AGENTS_TESTS.md` for details.
---

## 🔄 CI / GitHub Actions Workflow
* See `docs/agents/AGENTS_CI.md` for details.
---

## 🎯 Coding Guidelines
* See `docs/agents/AGENTS_CODING_GUIDELINES.md` for details.
---

## 📌 GitHub Collaboration Workflow (Branches, Issues & PRs)
Follow this standardized flow for all contributions.
### 1️⃣ Create or Update an Issue
- Before writing code, confirm the change is tracked in an issue
- Include clear description + acceptance criteria
- Reference related PRs/issues when available

### 2️⃣ Create a Working Branch
Name convention:

* ```feature/<short-description>```
* ```fix/<short-description>```
* ```docs/<short-description>```
```bash
Example:
git checkout -b feature/add-logging
```

### 3️⃣ Implement Code & Tests
- Follow `AGENTS.md` formatting, linting, and testing rules
- Commit in small units with descriptive messages:
```bash
git add .
git commit -m "feat: add logging to greet function"
```

### 4️⃣ Push Branch to GitHub
```bash
git push -u origin feature/add-logging
```

### 5️⃣ Create Pull Request (PR)
PR checklist:

✔ Link to issue using keywords: “Fixes #123”  
✔ Tests added/updated  
✔ Ruff formatting + lint clean  
✔ CI must pass  

Keep PRs small and focused.

### 6️⃣ Code Review Process
- Respond to feedback promptly
- Make fixup commits until approved

---


## ⚠️ Additional Notes

* Avoid pushing .venv/ or Docker-specific files to package index or PyPI
* When updating dependencies, maintain version pins in pyproject.toml
* If adjusting lint or formatting rules, run full test + lint + format suite before merging
* For large changes, update this file to reflect new workflows or conventions
* Do Not Commit directly to `main`
* Do Not merge PRs
* Do Not Skip tests for functionality changes

---

## 🧠 For AI Agents: What to Remember

Before making any changes or generating new code, read this file — it contains authoritative instructions for building, testing, formatting, and packaging the project.
Treat it as “source of truth” for conventions:

* Use uv, not pip install directly
* Use the src/ layout
* Respect lint/format rules — or CI will fail
* Add tests anytime functionality changes