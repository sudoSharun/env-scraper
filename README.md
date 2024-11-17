# Env Extractor

`env-extractor` is a Python package designed to scan Python files for environment variables and save them in either `.env` or JSON format. It supports extraction from Python files that use common methods for environment variable retrieval, such as `os.getenv`, `os.environ.get`, `dotenv`, and `environs`.

## Features

- Extracts environment variable names and types from Python code.
- Supports output in `.env` or JSON format.
- Scans an entire folder or specific Python files.
- Uses Python’s Abstract Syntax Tree (AST) to safely parse and analyze code.

## Installation

### Using `pip`

You can install the `env-extractor` package directly from GitHub using `pip`:

```bash
pip install git+https://github.com/sudoSharun/env-scraper
