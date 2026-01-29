# API Automation - Pytest Setup Guide

This directory contains refactored test scripts organized as pytest test functions with proper fixtures and markers.

## Project Structure

```
api-automation/
├── tests/
│   ├── __init__.py
│   ├── conftest.py                 # Pytest configuration with fixtures
│   ├── test_api_endpoints.py        # API tests (formerly task1_requests.py)
│   └── test_ui_automation.py        # UI/Playwright tests (formerly task4_playwrightAuto.py)
├── pytest.ini                       # Pytest configuration with markers
├── requirements.txt                 # Project dependencies
└── README_PYTEST.md                 # This file
```

## Features

### 1. Fixtures (conftest.py)
- **api_base_url**: Base URL for JSON Placeholder API
- **practice_url**: URL for Automation Practice site
- **browser**: Session-scoped Playwright browser instance
- **browser_context**: Function-scoped browser context
- **page**: Function-scoped page instance

### 2. Test Markers
- `@pytest.mark.api`: Tests for API endpoints
- `@pytest.mark.ui`: Tests for UI components
- `@pytest.mark.playwright`: Tests using Playwright
- `@pytest.mark.slow`: Slow-running tests
- `@pytest.mark.integration`: Integration tests

### 3. Test Files

#### test_api_endpoints.py
Refactored API tests with proper assertions:
- `test_response_time()`: Validates API response time < 2 seconds
- `test_schema_validation()`: Validates API response schema using Pydantic
- `test_multiple_endpoints()`: Parametrized test for multiple endpoints
- `test_fetch_first_5_posts()`: Fetches and saves first 5 posts to JSON

#### test_ui_automation.py
Refactored UI automation tests:
- `test_checkbox_selection()`: Tests checkbox interaction
- `test_radio_button_selection()`: Tests radio button interaction
- `test_dropdown_selection()`: Tests dropdown selection
- `test_input_field_text()`: Tests text input
- `test_alert_dialog()`: Tests alert dialog handling
- `test_all_ui_elements()`: Comprehensive UI test

## Installation

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install pytest requests pydantic playwright
```

### 2. Install Playwright Browsers
```bash
playwright install
```

## Running Tests

### Run All Tests
```bash
pytest tests/ -v
```

### Run Only API Tests
```bash
pytest tests/ -v -m api
```

### Run Only UI Tests
```bash
pytest tests/ -v -m ui
```

### Run API Tests with Short Output
```bash
pytest tests/test_api_endpoints.py -v
```

### Run Specific Test Function
```bash
pytest tests/test_api_endpoints.py::test_response_time -v
```

### Run with Detailed Output
```bash
pytest tests/ -v -s
```

### Run and Generate Coverage Report
```bash
pytest tests/ --cov=tests --cov-report=html
```

### Run in Parallel (requires pytest-xdist)
```bash
pytest tests/ -n auto
```

### Run with Markers
```bash
# Run only API tests
pytest tests/ -m api

# Run only UI tests
pytest tests/ -m ui

# Run everything except slow tests
pytest tests/ -m "not slow"

# Run API or Playwright tests
pytest tests/ -m "api or playwright"
```

## Configuration (pytest.ini)

The `pytest.ini` file contains:
- Test discovery patterns
- Custom markers definition
- Output verbosity settings
- Assertion output style

## Expected Output

When running all tests, you should see:
```
tests/test_api_endpoints.py::test_response_time PASSED
tests/test_api_endpoints.py::test_schema_validation PASSED
tests/test_api_endpoints.py::test_multiple_endpoints[/posts] PASSED
tests/test_api_endpoints.py::test_multiple_endpoints[/comments] PASSED
tests/test_api_endpoints.py::test_multiple_endpoints[/users] PASSED
tests/test_api_endpoints.py::test_fetch_first_5_posts PASSED
tests/test_ui_automation.py::test_checkbox_selection PASSED
tests/test_ui_automation.py::test_radio_button_selection PASSED
tests/test_ui_automation.py::test_dropdown_selection PASSED
tests/test_ui_automation.py::test_input_field_text PASSED
tests/test_ui_automation.py::test_alert_dialog PASSED
tests/test_ui_automation.py::test_all_ui_elements PASSED

========================= 13 passed in X.XXs =========================
```

## Key Improvements

✅ **Organized Structure**: All tests moved to dedicated `tests/` folder
✅ **Pytest Fixtures**: Reusable fixtures for API URLs and Playwright browser
✅ **Test Markers**: Categorize tests as API, UI, or Playwright
✅ **Assertions**: Proper pytest assertions with meaningful messages
✅ **Configuration**: pytest.ini for test discovery and markers
✅ **Documentation**: This guide for running and understanding tests

## Troubleshooting

### Issue: "pytest not found"
```bash
python -m pip install pytest
```

### Issue: "playwright module not found"
```bash
pip install playwright
playwright install
```

### Issue: "browser not found"
```bash
playwright install chromium
```

### Issue: Tests timeout
Increase timeout in pytest.ini or use:
```bash
pytest tests/ --timeout=300
```

## Next Steps

1. ✅ Run `pytest tests/ -v` to validate all tests
2. ✅ Use `-m` flag to run specific test categories
3. ✅ Add more tests following the same pattern
4. ✅ Integrate with CI/CD pipeline
5. ✅ Generate coverage reports with `--cov` flag
