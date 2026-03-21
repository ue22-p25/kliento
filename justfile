_default:
    just --list

black:
    poetry run black --check .

isort:
    poetry run isort --check .

flake8:
    poetry run flake8

mypy:
    poetry run mypy

[parallel]
lint: black isort flake8 mypy

test *args:
    poetry run pytest {{ args }}

check: lint (test)

setup:
    poetry check
    poetry install

fix:
    poetry run black .
    poetry run isort .
