SHELL := /bin/bash
PROJECT_DIR ?= $(shell git rev-parse --show-toplevel)


.PHONY: install-dev
install-dev:
	poetry env use 3.12
	poetry install --with dev


.PHONY: activate-env
activate-env:
	poetry shell


.PHONY: format
format:
	poetry run black $(PROJECT_DIR)/src/
	poetry run isort $(PROJECT_DIR)/src/


.PHONY: lint
lint:
	poetry run mypy $(PROJECT_DIR)/src/
	poetry run pylint --recursive=y $(PROJECT_DIR)/src/ --fail-under=9.9


.PHONY: start-dev-server
start-dev-server:
	PYTHONPATH=$(PROJECT_DIR)/src/ uvicorn src.app:app --host 127.0.0.1 --port 8000 --reload
