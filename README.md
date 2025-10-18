# Тестове завдання AQA - Shooters Global Automation

Проект автоматизації тестування для сайту [events.shooters.global](https://events.shooters.global/) з використанням Python Selenium та паттерну Page Object Model.

## 📋 Опис проекту

Автоматизований тест виконує наступні кроки:
1. Відкриває сторінку https://events.shooters.global/
2. Натискає на кнопку "Build for Free"
3. Логінується з використанням попередньо створених облікових даних
4. Очікує завантаження білдера (елемент canvas з насічками)
5. Виконує вихід з системи (Logout)

## 🛠 Технології

- **Python 3.13+**
- **Selenium WebDriver 4.15+** - для автоматизації браузера (з вбудованим Selenium Manager)
- **Pytest 7.4+** - тестовий фреймворк
- **Python-dotenv** - робота зі змінними оточення
- **Chrome Browser** - браузер для виконання тестів (автоматичне завантаження ChromeDriver)

## 📁 Структура проекту

```
TestTask_UDTech/
│
├── pages/                      # Page Object класи
│   ├── __init__.py
│   ├── base_page.py           # Базовий клас для всіх сторінок
│   ├── home_page.py           # Головна сторінка
│   ├── login_page.py          # Сторінка логіну
│   └── builder_page.py        # Сторінка білдера
│
├── tests/                      # Тестові сценарії
│   ├── __init__.py
│   ├── conftest.py            # Pytest конфігурація та fixtures
│   └── test_shooters_global.py # Основні тести
│
├── utils/                      # Утиліти та конфігурація
│   ├── __init__.py
│   ├── config.py              # Конфігураційні налаштування
│   ├── locators.py            # Локатори елементів
│   └── driver_factory.py      # Фабрика для створення WebDriver
│
├── .env                        # Змінні оточення (credentials)
├── .gitignore                  # Git ignore файл
├── requirements.txt            # Python залежності
└── README.md                   # Цей файл
```

## 🚀 Встановлення та налаштування

### Передумови

1. **Python 3.8+** встановлений на системі
2. **Google Chrome** браузер встановлений
3. **Git** (опціонально, для клонування репозиторію)

### Крок 1: Клонування репозиторію

```bash
git clone https://github.com/your-username/TestTask_UDTech.git
cd TestTask_UDTech
```

### Крок 2: Створення віртуального середовища

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

**Linux/MacOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Крок 3: Встановлення залежностей

```bash
pip install -r requirements.txt
```

### Крок 4: Налаштування облікових даних

**СПОСІБ 1: Через Python (РЕКОМЕНДУЄТЬСЯ для уникнення проблем з кодуванням)**
```powershell
.venv\Scripts\python.exe -c "with open('.env', 'w', encoding='utf-8') as f: f.write('EMAIL=your_email@example.com\nPASSWORD=your_password\n')"
```

**СПОСІБ 2: Вручну**
Створіть файл `.env` (UTF-8 без BOM) з вмістом:
```env
EMAIL=your_email@example.com
PASSWORD=your_password
```

**ВАЖЛИВО:** 
- Створіть новий аккаунт на сайті https://events.shooters.global/
- Використовуйте одноразову пошту (наприклад, https://temp-mail.org/, https://10minutemail.com/)
- Збережіть облікові дані у файлі `.env`

## ▶️ Запуск тестів

⚠️ **ВАЖЛИВО на Windows:** Використовуйте Python з віртуального середовища напряму:

### Рекомендований спосіб (Windows):

```powershell
# Запуск всіх тестів
.venv\Scripts\python.exe -m pytest tests/

# З детальним виводом
.venv\Scripts\python.exe -m pytest tests/ -v -s

# Або через run_tests.py
.venv\Scripts\python.exe run_tests.py
```

### Альтернативні способи:

```bash
# Якщо PowerShell дозволяє скрипти або на Linux/Mac
pytest tests/
```

### Запустити з детальним виводом:

```bash
pytest tests/ -v
```

### Запустити з виводом print statements:

```bash
pytest tests/ -v -s
```

### Запустити конкретний тест:

```bash
pytest tests/test_shooters_global.py::TestShootersGlobal::test_login_builder_logout_flow -v -s
```

### Запустити тести з HTML звітом:

```bash
pip install pytest-html
pytest tests/ --html=report.html --self-contained-html
```

## 🎯 Що тестується

### test_login_builder_logout_flow
Основний тест, який перевіряє повний флоу:
- ✅ Відкриття головної сторінки
- ✅ Натискання кнопки "Build for Free"
- ✅ Введення email та пароля
- ✅ Логін в систему
- ✅ Очікування завантаження білдера (canvas елемент)
- ✅ Вихід з системи

### test_login_with_valid_credentials
Додатковий тест для перевірки логіну:
- ✅ Валідація форми логіну
- ✅ Перевірка успішного входу

## 🏗 Паттерн Page Object Model

Проект використовує паттерн Page Object Model для кращої організації коду:

### BasePage
Містить загальні методи для всіх сторінок:
- `find_element()` - пошук елементу з очікуванням
- `click()` - клік по елементу
- `enter_text()` - введення тексту
- `wait_for_element_visible()` - очікування видимості елементу

### HomePage
Методи для головної сторінки:
- `open()` - відкриття сторінки
- `click_build_for_free()` - клік по кнопці "Build for Free"

### LoginPage
Методи для сторінки логіну:
- `enter_email()` - введення email
- `enter_password()` - введення пароля
- `login()` - повний процес логіну

### BuilderPage
Методи для сторінки білдера:
- `wait_for_builder_to_load()` - очікування завантаження білдера
- `logout()` - вихід з системи

## ⚙️ Конфігурація

Файл `utils/config.py` містить:
- `BASE_URL` - URL сайту
- `DEFAULT_TIMEOUT` - базовий таймаут (10 сек)
- `EXTENDED_TIMEOUT` - розширений таймаут (30 сек)
- `BUILDER_LOAD_TIMEOUT` - таймаут для завантаження білдера (60 сек)
- Креденціали з `.env` файлу

## 🐛 Труднощі під час розробки

### 1. **Динамічне завантаження елементів**
**Проблема:** Елементи на сторінці завантажуються асинхронно, що призводило до помилок `NoSuchElementException`.

**Рішення:** Використання явних очікувань (Explicit Waits) з `WebDriverWait` та `expected_conditions` для всіх критичних елементів.

### 2. **Складність з локаторами**
**Проблема:** Деякі елементи мають динамічні ID або складну структуру DOM.

**Рішення:** Використання XPath локаторів з прив'язкою до стабільних атрибутів (`name`, `type`, текстовий вміст).

### 3. **Завантаження білдера (Canvas)**
**Проблема:** Canvas елемент білдера може завантажуватися довго, особливо при повільному інтернеті.

**Рішення:** Встановлено розширений таймаут (`BUILDER_LOAD_TIMEOUT = 60 сек`) та додаткові перевірки видимості елементу.

### 4. **Модальні вікна після логіну**
**Проблема:** Іноді після логіну з'являється модальне вікно з кнопкою "OK", іноді ні.

**Рішення:** Використання `try-except` блоку для обробки необов'язкового модального вікна.

### 5. **Автоматичне керування ChromeDriver**
**Проблема:** Необхідність ручного завантаження та оновлення ChromeDriver для різних версій Chrome.

**Рішення:** Використання бібліотеки `webdriver-manager`, яка автоматично завантажує відповідну версію драйвера.

### 6. **Налаштування для різних ОС**
**Проблема:** Різні команди для активації віртуального середовища на Windows/Linux/MacOS.

**Рішення:** Документація всіх варіантів команд у README файлі.

## 📊 Можливі покращення

- [ ] Додати screenshot при падінні тестів
- [ ] Інтеграція з Allure для красивих звітів
- [ ] Паралельний запуск тестів (pytest-xdist)
- [ ] Додати тести для негативних сценаріїв (невірний логін/пароль)
- [ ] Docker контейнер для запуску тестів
- [ ] CI/CD інтеграція (GitHub Actions)
- [ ] Додати логування (logging module)

## 📝 Вимоги до завдання

- ✅ Python + Selenium
- ✅ Паттерн Page Object
- ✅ Публічний GitHub репозиторій
- ✅ Тести в Chrome браузері
- ✅ README з інструкціями
- ✅ Використання облікових даних з одноразової пошти
- ✅ Опис труднощів під час розробки

## 👤 Автор

Створено як тестове завдання для позиції AQA Engineer.

## 📄 Ліцензія

Цей проект створено для освітніх цілей як тестове завдання.
