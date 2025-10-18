# Quick Start Guide

## Швидкий запуск тестів (після встановлення)

### 1. Активувати віртуальне середовище

**Windows PowerShell:**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows CMD:**
```cmd
.venv\Scripts\activate.bat
```

### 2. Запустити тести

**Простий запуск:**
```bash
pytest tests/
```

**З детальним виводом:**
```bash
pytest tests/ -v -s
```

**Через Python скрипт:**
```bash
python run_tests.py
```

**Запустити тільки основний тест:**
```bash
pytest tests/test_shooters_global.py::TestShootersGlobal::test_login_builder_logout_flow -v -s
```

### 3. Перевірка структури проекту

```bash
tree /F /A
```

### 4. Перевірка встановлених пакетів

```bash
pip list
```

### 5. Оновлення залежностей

```bash
pip install -r requirements.txt --upgrade
```

## Корисні команди

### Запуск тестів з маркерами (якщо додати @pytest.mark.smoke)

```bash
pytest -m smoke -v
```

### Запуск тестів з HTML звітом

```bash
pip install pytest-html
pytest tests/ --html=report.html --self-contained-html
```

### Запуск тестів з покриттям коду

```bash
pip install pytest-cov
pytest tests/ --cov=pages --cov=utils --cov-report=html
```

### Очистка кешу pytest

```bash
pytest --cache-clear
```

### Показати доступні fixtures

```bash
pytest --fixtures
```

### Показати доступні маркери

```bash
pytest --markers
```

## Troubleshooting

### Проблема: ChromeDriver не запускається

**Рішення:** Оновіть webdriver-manager
```bash
pip install --upgrade webdriver-manager
```

### Проблема: Selenium не може знайти елементи

**Рішення:** Збільшіть таймаути в `utils/config.py`

### Проблема: Тести падають через .env

**Рішення:** Перевірте, що файл `.env` існує і містить:
```
EMAIL=your_email@example.com
PASSWORD=your_password
```

## Структура команд для різних сценаріїв

### Розробка нового тесту
1. Створити тест в `tests/test_*.py`
2. Запустити тільки новий тест: `pytest tests/test_file.py::test_name -v -s`
3. Переконатись що тест проходить
4. Зробити commit

### Додавання нової сторінки (Page Object)
1. Створити файл в `pages/new_page.py`
2. Наслідувати від `BasePage`
3. Додати локатори в `utils/locators.py`
4. Написати тести

### Запуск перед commit
```bash
pytest tests/ -v
```

### Запуск на CI/CD
```bash
pytest tests/ -v --tb=short --junitxml=test-results.xml
```
