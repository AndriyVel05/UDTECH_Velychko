# 📚 Документація проекту - Зміст

## Вітаємо у проекті TestTask_UDTech!

Цей проект є автоматизованим тестуванням сайту Shooters Global Events з використанням Python, Selenium та паттерна Page Object Model.

---

## 🚀 Швидкий старт

**Якщо ви тут вперше:**
1. Почніть з [README.md](README.md) - основна документація
2. Далі [QUICK_START.md](QUICK_START.md) - команди для запуску
3. Перегляньте [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) - загальний огляд

**Для запуску тестів:**
- Windows: Двічі клікніть на `run_tests.bat` або `run_tests.ps1`
- Або в терміналі: `pytest tests/ -v -s`

---

## 📖 Документація

### Основні файли

| Файл | Опис | Коли використовувати |
|------|------|---------------------|
| **[README.md](README.md)** | Головна документація проекту | Початок роботи, встановлення, запуск |
| **[QUICK_START.md](QUICK_START.md)** | Швидкі команди та приклади | Потрібна конкретна команда |
| **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** | Загальний огляд проекту | Швидко зрозуміти що є в проекті |

### Детальна інформація

| Файл | Опис | Коли використовувати |
|------|------|---------------------|
| **[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)** | Детальна структура проекту | Потрібно зрозуміти організацію коду |
| **[GITHUB_SETUP.md](GITHUB_SETUP.md)** | Інструкції для GitHub | Завантаження проекту на GitHub |
| **[CHECKLIST.md](CHECKLIST.md)** | Чек-лист перед публікацією | Перед push на GitHub |

---

## 🗂 Структура проекту

```
TestTask_UDTech/
│
├── 📁 pages/              - Page Object класи
│   ├── base_page.py      - Базовий клас
│   ├── home_page.py      - Головна сторінка
│   ├── login_page.py     - Сторінка логіну
│   └── builder_page.py   - Сторінка білдера
│
├── 📁 tests/              - Тестові сценарії
│   ├── conftest.py       - Pytest конфігурація
│   └── test_shooters_global.py - Тести
│
├── 📁 utils/              - Утиліти та конфігурація
│   ├── config.py         - Налаштування
│   ├── locators.py       - Локатори елементів
│   └── driver_factory.py - WebDriver factory
│
├── 📄 .env                - Облікові дані (НЕ в Git!)
├── 📄 requirements.txt    - Python залежності
├── 📄 pytest.ini          - Pytest конфігурація
└── 📄 README.md           - Головна документація
```

---

## 🎯 Основні команди

### Встановлення
```bash
# Клонувати репозиторій
git clone https://github.com/YOUR_USERNAME/TestTask_UDTech.git
cd TestTask_UDTech

# Створити віртуальне середовище
python -m venv .venv

# Активувати (Windows PowerShell)
.venv\Scripts\Activate.ps1

# Встановити залежності
pip install -r requirements.txt

# Створити .env файл з credentials
# EMAIL=your_email@example.com
# PASSWORD=your_password
```

### Запуск тестів
```bash
# Простий запуск
pytest tests/

# З детальним виводом
pytest tests/ -v -s

# Через скрипт
python run_tests.py

# Windows - подвійний клік
run_tests.bat  або  run_tests.ps1
```

---

## 📋 Навігація по документації

### Для початківців
1. [README.md](README.md) → Основи проекту
2. [QUICK_START.md](QUICK_START.md) → Перші команди
3. [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) → Що в проекті

### Для розробників
1. [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) → Архітектура
2. Код в `pages/`, `tests/`, `utils/` → Імплементація
3. [QUICK_START.md](QUICK_START.md) → Команди для розробки

### Для публікації
1. [CHECKLIST.md](CHECKLIST.md) → Перевірити перед push
2. [GITHUB_SETUP.md](GITHUB_SETUP.md) → Завантажити на GitHub
3. [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) → Опис для README

---

## 🛠 Технології

- **Python 3.13+** - мова програмування
- **Selenium 4.15** - автоматизація браузера
- **Pytest 7.4** - тестовий фреймворк
- **Chrome WebDriver** - драйвер браузера (auto-managed)
- **Page Object Model** - паттерн проектування

---

## 📞 Корисні посилання

### Код проекту
- [pages/](pages/) - Page Object класи
- [tests/](tests/) - Тестові файли
- [utils/](utils/) - Утиліти та конфігурація

### Конфігурація
- [requirements.txt](requirements.txt) - Залежності
- [pytest.ini](pytest.ini) - Pytest налаштування
- [.gitignore](.gitignore) - Git ignore правила

### Запуск
- [run_tests.py](run_tests.py) - Python скрипт
- [run_tests.bat](run_tests.bat) - Windows batch
- [run_tests.ps1](run_tests.ps1) - PowerShell скрипт

---

## ❓ FAQ

**Q: Як запустити тести вперше?**
A: Дивіться [QUICK_START.md](QUICK_START.md) розділ "Швидкий запуск"

**Q: Як додати новий тест?**
A: Дивіться [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) розділ "Workflow"

**Q: Як завантажити на GitHub?**
A: Дивіться [GITHUB_SETUP.md](GITHUB_SETUP.md)

**Q: Тести не працюють, що робити?**
A: Дивіться [QUICK_START.md](QUICK_START.md) розділ "Troubleshooting"

**Q: Де знайти облікові дані?**
A: Створіть файл `.env` з EMAIL та PASSWORD (приклад в README.md)

---

## ✨ Швидка допомога

| Проблема | Рішення |
|----------|---------|
| Не можу запустити тести | Перевірте `.env` файл та віртуальне середовище |
| ChromeDriver помилка | `pip install --upgrade webdriver-manager` |
| Import помилки | `pip install -r requirements.txt` |
| Git помилки | Дивіться [GITHUB_SETUP.md](GITHUB_SETUP.md) |

---

## 🎓 Навчальні матеріали

### Розуміння проекту
1. Прочитайте [README.md](README.md) - розумієте що і навіщо
2. Подивіться [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) - розумієте як
3. Відкрийте код в `pages/` та `tests/` - побачите реалізацію
4. Запустіть тести - побачите як працює

### Розширення проекту
1. Додайте новий Page Object - [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)
2. Напишіть новий тест - дивіться `tests/test_shooters_global.py`
3. Оновіть документацію - не забудьте про README

---

## 🚀 Готові до старту?

**Рекомендований шлях:**
1. 📖 [README.md](README.md) - Прочитати
2. ⚙️ Встановити залежності (команди вище)
3. 🏃 [QUICK_START.md](QUICK_START.md) - Запустити тести
4. ✅ Все працює? Вітаємо! 🎉

**Для публікації:**
1. ✓ [CHECKLIST.md](CHECKLIST.md) - Перевірити
2. 📤 [GITHUB_SETUP.md](GITHUB_SETUP.md) - Завантажити
3. 🎊 Готово!

---

## 📝 Ліцензія

Проект під ліцензією MIT - дивіться [LICENSE](LICENSE)

---

**Створено:** 17 жовтня 2025  
**Версія:** 1.0  
**Статус:** ✅ Production Ready

**Автор:** TestTask_UDTech  
**Контакт:** Дивіться GitHub профіль

---

💡 **Порада:** Збережіть цей файл в закладки - він містить посилання на всю документацію!
