# AGENTS_COLLABORATION.md — GitHub Workflow for Branches, Issues & PRs

This document defines how AI agents and developers collaborate using GitHub.  
It ensures that contributions are traceable, reviewable, and CI-compliant.

---

## 🧭 Collaboration Goals

✔ Clean and readable Git history  
✔ Traceability from Issue → Branch → PR → Merge  
✔ No broken code reaches `main`  
✔ Ensures continuous deployment readiness

---

## 📝 1️⃣ Issue Workflow

All changes must start with an Issue.

Steps:

1. Search existing issues to avoid duplicates
2. Create a new issue if needed, including:
   - **Title:** Clear and concise
   - **Body:** Problem + Proposed solution + Acceptance criteria
   - **Labels:** `bug`, `feature`, `docs`, `tech-debt`

3. Assign priority and milestone if known

Issue format example:

As a <user/agent>
I want <feature or fix>
So that <value provided>