# Shooters Global Automation Test

Automated test for [events.shooters.global](https://events.shooters.global/) using Python, Selenium and Page Object Pattern.

## Installation

1. Install Python 3.8+
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create `.env` file with credentials:
```
EMAIL=your_email@example.com
PASSWORD=your_password
```

## Run Tests

```bash
python -m pytest tests/ -v
```

Or use the test runner:
```bash
python run_tests.py
```

## Project Structure

```
pages/          - Page Object classes
tests/          - Test scenarios
utils/          - Configuration and utilities
```

## Requirements

- Python 3.8+
- Chrome browser
- Selenium WebDriver
- pytest
