install:
	uv sync

run:
	uv run gendiff -h

diff:
	uv run gendiff tests/fixtures/file3.json tests/fixtures/file4.json

diff_json:
	uv run gendiff tests/fixtures/file3.json tests/fixtures/file4.json -f json

diff_yml:
	uv run gendiff tests/fixtures/file3.yml tests/fixtures/file4.yml

diff_plain:
	uv run gendiff tests/fixtures/file3.json tests/fixtures/file4.json -f plain

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff tests/ --cov-report xml

lint:
	uv run ruff check

check: test lint

build:
	uv build

.PHONY: install test lint  check build