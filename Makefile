.PHONY: help setup run test clean

help:
	@echo "Available commands:"
	@echo "  make setup  - Initialize environment"
	@echo "  make run    - Run the main application/script"
	@echo "  make test   - Run tests"
	@echo "  make clean  - Remove temporary files"

# === EXAMPLES ===
# setup:
# 	pip install -r requirements.txt
# run:
# 	python src/main.py
# test:
# 	pytest tests/

setup:
	@echo "Installing Ruby and Node dependencies..."
	bundle install
	npm install

serve:
	@echo "Starting Jekyll local server..."
	bundle exec jekyll serve --livereload

test:
	@echo "Running Python unit tests..."
	pytest -o pythonpath=scripts --ignore=_site tests/

verify-refs:
	@echo "Running reference & hallucination audit..."
	python -u scripts/verify_references.py

test-e2e:
	@echo "Running Playwright E2E tests..."
	npx playwright test

clean:
	@echo "Cleaning up generated site and test artifacts..."
	bundle exec jekyll clean

