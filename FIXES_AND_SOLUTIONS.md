# ⚠️ ВАЖЛИВІ ВИПРАВЛЕННЯ ТА ПОРАДИ

## ✅ Виправлені проблеми

### 1. Проблема з WebDriver Manager (Win32/Win64)
**Симптом:** `OSError: [WinError 193] %1 is not a valid Win32 application`

**Рішення:** Перейшли на вбудований Selenium Manager (Selenium 4.6+)
- Видалена залежність від `webdriver-manager`
- Selenium тепер автоматично завантажує правильний ChromeDriver
- Працює як на Win32, так і на Win64

**Оновлений файл:** `utils/driver_factory.py`

### 2. Проблема з .env файлом (UTF-8 BOM)
**Симптом:** `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff`

**Рішення:** Файл `.env` мав неправильне кодування (UTF-16 LE BOM)
- Перестворено файл з правильним кодуванням UTF-8
- Оновлено `utils/config.py` для явного вказання шляху до `.env`

**Як перестворити .env:**
```powershell
.venv\Scripts\python.exe -c "with open('.env', 'w', encoding='utf-8') as f: f.write('EMAIL=your_email@example.com\nPASSWORD=your_password\n')"
```

### 3. Проблема з PowerShell Execution Policy  
**Симптом:** Cannot be loaded because running scripts is disabled

**Рішення:** Використовуйте прямий виклик Python:
```powershell
# Замість:
.venv\Scripts\Activate.ps1

# Використовуйте:
.venv\Scripts\python.exe run_tests.py
# або
.venv\Scripts\python.exe -m pytest tests/
```

## 🚀 Правильний спосіб запуску тестів

### Варіант 1: Через Python (РЕКОМЕНДУЄТЬСЯ)
```powershell
.venv\Scripts\python.exe run_tests.py
```

### Варіант 2: Через pytest напряму
```powershell
.venv\Scripts\python.exe -m pytest tests/ -v -s
```

### Варіант 3: Batch файл (Windows CMD)
Двічі клікніть на `run_tests.bat`

### Варіант 4: Якщо PowerShell дозволяє скрипти
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
pytest tests/ -v -s
```

## 🔧 Troubleshooting

### Тест не запускається: ModuleNotFoundError
```powershell
# Переконайтесь що використовуєте Python з .venv:
.venv\Scripts\python.exe -m pip list

# Переінсталюйте залежності:
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### Браузер не відкривається
```powershell
# Перевірте чи встановлено Google Chrome:
# Chrome має бути встановлений в системі!

# Selenium Manager автоматично завантажить ChromeDriver
```

### EMAIL та PASSWORD = None
```powershell
# Перестворіть .env файл:
.venv\Scripts\python.exe -c "with open('.env', 'w', encoding='utf-8') as f: f.write('EMAIL=your_email@example.com\nPASSWORD=your_password\n')"

# Перевірте що працює:
.venv\Scripts\python.exe -c "from utils.config import Config; print(Config.EMAIL)"
```

## 📝 Оновлений requirements.txt

Webdriver-manager більше не потрібен (Selenium Manager вбудований):

```
selenium==4.15.2
pytest==7.4.3
python-dotenv==1.0.0
```

## 🎯 Перевірка що все працює

```powershell
# 1. Перевірка віртуального середовища
.venv\Scripts\python.exe --version
# Повинно показати: Python 3.13.7

# 2. Перевірка пакетів
.venv\Scripts\python.exe -m pip list | Select-String "selenium|pytest|dotenv"
# Повинні бути: selenium, pytest, python-dotenv

# 3. Перевірка .env
.venv\Scripts\python.exe -c "from utils.config import Config; print(f'EMAIL: {Config.EMAIL[:10]}...')"
# Повинно показати початок email

# 4. Запуск тесту
.venv\Scripts\python.exe -m pytest tests/ -v
# Повинен відкритися Chrome і запуститися тест
```

## 📊 Результат виправлень

| Проблема | Статус | Рішення |
|----------|--------|---------|
| Win32 application error | ✅ Виправлено | Selenium Manager |
| UTF-8 BOM в .env | ✅ Виправлено | Перестворено файл |
| PowerShell Execution Policy | ✅ Обійдено | Прямий виклик Python |
| ModuleNotFoundError | ✅ Виправлено | Використання .venv\Scripts\python.exe |

## 💡 Best Practices

1. **Завжди використовуйте повний шлях до Python:**
   ```powershell
   .venv\Scripts\python.exe -m pytest tests/
   ```

2. **Створюйте .env через Python для правильного кодування:**
   ```powershell
   .venv\Scripts\python.exe -c "with open('.env', 'w', encoding='utf-8') as f: f.write('EMAIL=...\nPASSWORD=...\n')"
   ```

3. **Перевіряйте конфігурацію перед запуском тестів:**
   ```powershell
   .venv\Scripts\python.exe -c "from utils.config import Config; print(Config.EMAIL)"
   ```

## 📅 Дата оновлення: 17 жовтня 2025

Всі виправлення протестовані та працюють!
