install:
	uv sync

run:
	uv run gendiff -h

diff:
	uv run gendiff tests/fixtures/file1.json tests/fixtures/file2.json

diff_json:
	uv run gendiff tests/fixtures/file1.json tests/fixtures/file2.json -f json

diff_yml:
	uv run gendiff tests/fixtures/file1.yml tests/fixtures/file2.yml

diff_plain:
	uv run gendiff tests/fixtures/file1.json tests/fixtures/file2.json -f plain

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=genediff --cov-report xml

lint:
	uv run ruff check

check: test lint

build:
	uv build

.PHONY: install test lint selfcheck check build