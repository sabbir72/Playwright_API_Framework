# Playwright API Framework

A lightweight API test automation framework built with Python, pytest, and Playwright's request API. The project is organized to support reusable API clients, payload handling, assertions, and report generation.

## Project Structure

- api/ - API client and resource wrappers
  - api_client.py - shared HTTP client implementation
  - auth_api.py - authentication-related API helpers
  - posts_api.py - posts resource helpers
  - products_api.py - products resource helpers
  - users_api.py - users resource helpers
- tests/ - pytest test cases
- utils/ - configuration, JSON helpers, logging, and random data utilities
- payloads/ - JSON payload files used by tests
- reports/ - generated HTML/Allure reports
- schemas/ - schema-related files if used by tests

## Prerequisites

- Python 3.10+
- pip
- Virtual environment (recommended)

## Setup

1. Create and activate a virtual environment
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables
   Create a .env file in the project root with values such as:
   ```env
   BASE_URL=https://reqres.in
   TIMEOUT=30000
   REQRES_API_KEY=
   POSTS_BASE_URL=https://jsonplaceholder.typicode.com
   ```

## Run Tests

Run the full suite:
```bash
pytest -q
```

Run a specific test file:
```bash
pytest -q tests/test_auth.py
```

Generate Allure report:
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## Notes

- The framework uses pytest fixtures and logging utilities to keep test code readable.
- Test reports are generated under the reports/ and allure-results/ folders.
