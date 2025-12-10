---
name: 🐞 Bug Report
about: Something is not working correctly
labels: bug
---

## 🔥 Problem Summary
`worker` command prints wrong output when input contains numbers.

---

## 🧩 Steps to Reproduce
```bash
worker 123
Expected: Hello from 123!
Actual: crashes
```

---

## 📌 Expected Outcome
CLI handles numeric inputs safely.

---

## 🧪 Acceptance Criteria
- [ ] Test added that confirms correct behavior
- [ ] Fix implemented & verified
- [ ] Ruff formatting + lint clean
- [ ] CI pipeline green

---

## 📎 Logs / Evidence
Paste traceback or screenshots.

---

## 🧠 Notes for AI agents
Check type handling inside `greet()` function.