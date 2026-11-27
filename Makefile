.PHONY: help install test lint format run clean

help:
	@echo "Доступные команды:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Установить зависимости через Poetry
	poetry install

test: ## Запустить тесты
	poetry run python -m pytest

lint: ## Проверить код линтерами
	poetry run ruff check src/. tests/.
	poetry run black --check src/. tests/.
	poetry run isort --check-only src/. tests/.

format: ## Отформатировать код
	poetry run ruff check --fix --unsafe-fixes src/. tests/.
	poetry run black src/. tests/.
	poetry run isort src/. tests/.

run: ## Запустить прототип
	poetry run python src/main.py

clean: ## Очистить кэш и временные файлы
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .ruff_cache .mypy_cache