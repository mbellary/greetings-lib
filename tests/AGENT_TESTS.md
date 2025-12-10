# 🧪 Testing & Coverage

* Tests are written using pytest, located under tests/
* Example test: tests/test_greetings.py
* To run the full test suite:
```bash
uv run pytest --cov=greetings_lib --cov-report=term
```
* Coverage is collected via ```pytest-cov```

CI (GitHub Actions) also runs tests + coverage + lint + format checks on every push / pull request.