install:
	poetry install
	poetry run pre-commit install

dev:
	poetry run fastapi dev verbumapi/main.py

lint:
	poetry run ruff check

lint_fix:
	poetry run ruff check --fix

format:
	poetry run ruff format
