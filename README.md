# my-python-backend

Python backend learning project with modern tooling.

## Tech Stack
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **Tools:** uv, Ruff, mypy, pytest, Docker

## Setup

```bash
# Install dependencies
uv sync

# Run linter
uv run ruff check .

# Run type checker
uv run mypy src/

# Run formatter
uv run ruff format src/
```

## Project Structure
```
src/
├── my_python_backend/
│   ├── __init__.py
│   └── main.py
```