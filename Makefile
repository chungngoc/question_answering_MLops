help:
	@echo "Available commands:"
	@echo "  make install   Install dependencies"
	@echo "  make run       Run API locally"
	@echo "  make test      Run tests"
	@echo "  make lint      Run linting"
	@echo "  make format    Format code"

install:
	pip install --upgrade pip && \
		pip install -r requirements.txt

run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

test:
	pytest -v -m "not slow"

test-all:
	pytest -v

lint:
	flake8 app

format:
	black app