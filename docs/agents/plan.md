# Plan: Add greet(name, place) function to greetings.py

## Context
- Followed AGENTS_COLLABORATION.md: all work starts from a GitHub issue and is implemented in a feature branch.
- This plan tracks the work for adding a new greet function that prints `Hello {name} from {place}`.

## Related Issue(s)
- TODO: Link newly created feature issue once available.

## Tasks
1. Create GitHub issue using `feature` template describing the new greet(name, place) behavior and acceptance criteria.
2. Create branch from `main` following `.github/BRANCH/branch.md`, e.g., `feature/greet-name-place`.
3. Update `src/greetings_lib/greetings.py` to add `greet(name: str, place: str) -> None` that prints exactly `Hello {name} from {place}`.
4. Add/Update tests under `tests/` to cover the new function with sample inputs.
5. Run local checks as per AGENTS_COLLABORATION.md:
   - `uv run ruff format .`
   - `uv run ruff check . --fix`
   - `uv run pytest --cov`
6. Commit changes with a `feat:` message referencing the issue (e.g., `feat: add greet by name and place

Fixes #<issue-number>`).
7. Push branch and open a PR using `.github/PULL_REQUEST/pull_request.md` template, linking the issue.
8. Ensure CI passes and address any review feedback.

## Status Tracking
- [x] Draft plan created in docs/agents/plan.md
- [ ] Issue created in GitHub
- [ ] Branch created from main
- [ ] Code changes implemented
- [ ] Tests updated/added
- [ ] Local quality checks passing
- [ ] PR opened
- [ ] CI green
- [ ] PR merged