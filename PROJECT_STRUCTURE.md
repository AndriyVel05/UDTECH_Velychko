# Структура проекту TestTask_UDTech

```
TestTask_UDTech/
│
├── .venv/                          # Віртуальне середовище Python (не завантажується в Git)
│
├── pages/                          # Page Object класи (паттерн Page Object Model)
│   ├── __init__.py                # Ініціалізаційний файл пакету
│   ├── base_page.py               # Базовий клас з загальними методами для всіх сторінок
│   │                              #   - find_element, click, enter_text, wait_for_element, etc.
│   ├── home_page.py               # Головна сторінка (events.shooters.global)
│   │                              #   - open(), click_build_for_free()
│   ├── login_page.py              # Сторінка логіну
│   │                              #   - enter_email(), enter_password(), login()
│   └── builder_page.py            # Сторінка білдера
│                                  #   - wait_for_builder_to_load(), logout()
│
├── tests/                          # Тестові сценарії
│   ├── __init__.py                # Ініціалізаційний файл пакету
│   ├── conftest.py                # Pytest конфігурація та fixtures
│   │                              #   - Налаштування тестів, загальні fixtures
│   └── test_shooters_global.py    # Основні автоматизовані тести
│                                  #   - test_login_builder_logout_flow()
│                                  #   - test_login_with_valid_credentials()
│
├── utils/                          # Утиліти, конфігурація, допоміжні файли
│   ├── __init__.py                # Ініціалізаційний файл пакету
│   ├── config.py                  # Конфігураційні налаштування
│   │                              #   - BASE_URL, timeouts, browser settings
│   │                              #   - Завантаження credentials з .env
│   ├── locators.py                # Локатори для всіх елементів на сторінках
│   │                              #   - HomePageLocators, LoginPageLocators, BuilderPageLocators
│   └── driver_factory.py          # Фабрика для створення WebDriver instance
│                                  #   - create_driver() - налаштування Chrome
│
├── .env                            # Змінні оточення (EMAIL, PASSWORD)
│                                  # ⚠️ НЕ ЗАВАНТАЖУЄТЬСЯ В GIT (в .gitignore)
│
├── .gitignore                      # Файли та папки, що ігноруються Git
│                                  # - .venv/, .env, __pycache__, *.pyc, etc.
│
├── pytest.ini                      # Конфігурація Pytest
│                                  # - Налаштування запуску тестів, маркери, logging
│
├── requirements.txt                # Python залежності проекту
│                                  # - selenium, pytest, webdriver-manager, python-dotenv
│
├── run_tests.py                    # Скрипт для швидкого запуску всіх тестів
│                                  # Використання: python run_tests.py
│
├── README.md                       # Головна документація проекту
│                                  # - Опис, встановлення, запуск, труднощі
│
├── GITHUB_SETUP.md                 # Інструкції для завантаження на GitHub
│                                  # - Як створити репозиторій, push код
│
├── QUICK_START.md                  # Швидкий старт та корисні команди
│                                  # - Команди для запуску тестів, troubleshooting
│
└── PROJECT_STRUCTURE.md            # Цей файл - детальний опис структури

```

## Опис ключових компонентів

### 📁 pages/ - Page Object Model

Кожен файл представляє окрему сторінку веб-додатку:

- **base_page.py** - батьківський клас для всіх Page Objects
  - Містить загальні методи роботи з елементами
  - Використовує явні очікування (WebDriverWait)
  
- **home_page.py** - представляє головну сторінку
  - Методи для взаємодії з головною сторінкою
  
- **login_page.py** - представляє сторінку авторизації
  - Методи для введення креденшелів та логіну
  
- **builder_page.py** - представляє білдер
  - Методи для очікування завантаження та виходу з системи

### 🧪 tests/ - Тестові сценарії

- **conftest.py** - загальна конфігурація Pytest
  - Fixtures (наприклад, driver fixture)
  - Налаштування маркерів
  
- **test_shooters_global.py** - автоматизовані тести
  - Імплементація тестових сценаріїв
  - Використання Page Objects

### ⚙️ utils/ - Утиліти

- **config.py** - централізована конфігурація
  - URLs, timeouts, browser settings
  - Завантаження environment variables
  
- **locators.py** - всі локатори в одному місці
  - Організовані по класам для кожної сторінки
  - Використовує tuple формат: (By.TYPE, "selector")
  
- **driver_factory.py** - створення WebDriver
  - Автоматичне завантаження ChromeDriver
  - Налаштування опцій браузера

## Принципи організації

### 1. Separation of Concerns (Розділення відповідальностей)
- Логіка сторінок окремо від тестів
- Локатори окремо від логіки
- Конфігурація окремо від коду

### 2. DRY (Don't Repeat Yourself)
- Спільна логіка в BasePage
- Повторювані дії винесені в методи
- Конфігурація в одному місці

### 3. Page Object Pattern
- Кожна сторінка = окремий клас
- Методи представляють дії користувача
- Тести викликають методи, а не працюють з WebDriver напряму

### 4. Читабельність
- Описові назви методів
- Docstrings для всіх класів та методів
- Коментарі для складних секцій

## Workflow роботи з проектом

### Додавання нового тесту:
1. Визначити які сторінки потрібні
2. Додати локатори в `utils/locators.py` (якщо потрібно)
3. Додати методи в Page Objects (якщо потрібно)
4. Написати тест в `tests/`
5. Запустити та перевірити

### Додавання нової сторінки:
1. Створити новий файл в `pages/`
2. Наслідувати від `BasePage`
3. Додати локатори в `utils/locators.py`
4. Реалізувати методи сторінки
5. Використати в тестах

## Git Workflow

```bash
# Початкове налаштування
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/USERNAME/REPO.git
git push -u origin main

# Робота над новими фічами
git checkout -b feature/new-test
# ... зміни ...
git add .
git commit -m "Add new test for feature X"
git push origin feature/new-test
# Створити Pull Request на GitHub

# Оновлення з remote
git pull origin main
```

## Важливі зауваження

⚠️ **Безпека:**
- Ніколи не комітьте `.env` файл
- Переконайтесь що `.env` в `.gitignore`
- Не зберігайте паролі в коді

✅ **Best Practices:**
- Завжди використовуйте віртуальне середовище
- Оновлюйте `requirements.txt` при додаванні пакетів
- Пишіть описові commit messages
- Запускайте тести перед commit
- Використовуйте явні очікування, а не time.sleep()

📝 **Документація:**
- Додавайте docstrings до нових методів
- Оновлюйте README при змінах
- Коментуйте складну логіку
