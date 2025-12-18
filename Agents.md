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

## 🛠 Development Environment & Setup Guidelines
* See `docs/agents/AGENTS_ENVIRONMENT.md` for details.
---

## ✅ Code Style, Linting & Formatting Guidelines
* See `docs/agents/AGENTS_LINTING.md` for details.
---

## 🧪 Testing & Coverage Guidelines
* See `tests/AGENTS_TESTS.md` for details.
---

## 🔄 CI / GitHub Actions Guidelines
* See `.github/workflows/AGENTS_CI.md` for details.
---

## 🎯 Coding Guidelines
* See `docs/agents/AGENTS_CODING_GUIDELINES.md` for details.
---

## 📌 GitHub Collaboration Workflow and Guidelines (Branches, Issues & PRs)
* See `.github/AGENTS_COLLABORATION.md` for details.

---

## 🧠 For AI Agents: What to Remember

Before making any changes or generating new code, read this file — it contains authoritative instructions for building, testing, formatting, packaging and github collaboration for this project.
Treat it as “source of truth” for conventions:

* Use uv, not pip install directly
* Use the src/ layout
* Respect lint/format rules — or CI will fail
* Add tests anytime functionality changes
* Create duplicate issues
* Rewrite code without justification
* Produce large PRs when smaller is possible.
* When updating dependencies, maintain version pins in pyproject.toml
* Do Not Commit directly to `main`
* Do Not merge PRs
* Do Not Skip tests for functionality changes
* Do Not push .venv/ or Docker-specific files to package index or PyPI
* For large changes, update this file to reflect new workflows or conventions

---

# ExecPlans

When writing features or significant refactors, use an ExecPlan (as described in PLANS.md) from design to implementation. ExecPlans are living documents and should be referred to and updated frequently throughout implementation. Store new execplans in plans/$short-feature-name/, e.g.: plans/greetings for the greetings feature.

When instructed to implement an ExecPlan, implement it from start to finish autonomously, solving issues that arise independently. Work tirelessly, diligently; indefatigably. You have infinite time to complete ExecPlans, your context window will auto-compact, so refer back to the ExecPlan whenever it is no longer in your context window and diligently maintain it.