# AGENTS_CI.md — CI/CD Pipeline Execution & Rules

This document guides AI agents on running, validating, and maintaining the
Continuous Integration (CI) pipeline for this repository.

The CI pipeline enforces the following:

✔ Code style  
✔ Linting and formatting  
✔ Unit tests and coverage  
✔ Automated artifact validation  
✔ Deployment readiness (optional future)

---

## 🤖 GitHub Actions Pipeline Overview

The workflow file is located at: `.github/workflows/tests.yml`

Pipeline triggers:

| Event | Action |
|-------|--------|
| `push` to `main` | Full CI run |
| `pull_request` targeting `main` | Full CI run |

Agents must ensure CI is green **before** merging changes.

---

## 🧱 CI Pipeline Stages

| Stage | Action | Tool | Must Pass |
|-------|--------|------|:--------:|
| 1 | Install dependencies | `uv` | ✔ |
| 2 | Format check | `ruff format --check` | ✔ |
| 3 | Lint rules | `ruff check` | ✔ |
| 4 | Test execution | `pytest` | ✔ |
| 5 | Coverage report | `pytest-cov` | ✔ |
| 6 | Coverage upload | Codecov |✔  |

A PR **must not** be merged unless **all required** checks pass.

---

## 🔍 Coverage Upload (Codecov)

Two ways coverage may upload:

| Repository Type | Upload Method | Token Required |
|-----------------|---------------|----------------|
| Public Repository | Codecov GitHub App | ❌ |
| Private Repository | Codecov Token | ✔ |

If a token is required:

Add in repo → **Settings → Secrets → Actions → `CODECOV_TOKEN`**

Then ensure workflow contains:

```yaml
with:
  token: ${{ secrets.CODECOV_TOKEN }}
  files: coverage.xml
  fail_ci_if_error: true
```
Coverage badge:
```markdown
[![Coverage](https://img.shields.io/codecov/c/github/mbellary/greetings-lib)](https://codecov.io/gh/mbellary/greetings-lib)
```

## ⚠️ Common CI Failures & Fixes
| Failure                 | Cause                       | Fix                                      |
| ----------------------- | --------------------------- | ---------------------------------------- |
| Format errors           | Ruff formatting drift       | `uv run ruff format .`                   |
| Lint errors             | Static rule violations      | `uv run ruff check . --fix`              |
| Module import errors    | Wrong path structure        | Ensure `src/greetings_lib/*`             |
| Pytest failures         | Behavior changes not tested | Update/add tests                         |
| Coverage upload failure | Missing Codecov token       | Configure token or disable fail on error |

## 🔄 Required CI Updates with Feature Work

Any PR adding new behavior must:

✔ Include new tests

✔ Update formatting + lint rules if needed

✔ Maintain stable workflow in .github/workflows/tests.yml

✔ Update coverage badge target if repo name changes

✔ Update AGENTS docs if tools change

## 🌐 Branch Strategy in CI
| Branch      |     Allowed?    | Notes                      |
| ----------- | :-------------: | -------------------------- |
| `main`      | ❌ direct pushes | PR only                    |
| `feature/*` |        ✔        | Must pass CI               |
| `fix/*`     |        ✔        | Issues should reference PR |
| `docs/*`    |        ✔        | CI still enforced          |


`main` must always be green.

## 🧠 For AI Agents

Before pushing code:

* Run local validations:
    ```bash
    uv run ruff format .
    uv run ruff check .
    uv run pytest --cov
    ```
* Never skip tests or lint to “fix later”
* Update this file if CI logic changes