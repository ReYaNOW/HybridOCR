dev:
	poetry run fastapi dev verbumapi/main.py

lint:
	ruff check verbumapi/

lint_fix:
	ruff check --fix verbumapi/