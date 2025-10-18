# 🔍 Debugging Guide - Поради по налагодженню тестів

## Поточна проблема: Builder Canvas не завантажується

### Симптоми:
- Тест успішно логінується ✓
- OK button натискається ✓
- Canvas element не знаходиться протягом 60 секунд ✗

### Можливі причини:

1. **Canvas має інший ID або не завантажується**
   - Білдер може бути на іншій сторінці
   - Canvas може мати динамічний ID
   - Unity додаток може довго завантажуватися

2. **Потрібна додаткова навігація**
   - Після логіну може бути ще якась сторінка
   - Потрібно натиснути ще щось перед білдером

3. **Повільне з'єднання**
   - Unity білдер завантажує багато ресурсів
   - Може потребувати більше 60 секунд

### Рішення які вже застосовано:

✅ **Додано альтернативні локатори:**
```python
CANVAS_ELEMENT = (By.XPATH, "//canvas[@id='unity-app-canvas']")
CANVAS_ELEMENT_ALT = (By.CSS_SELECTOR, "canvas#unity-app-canvas")
ANY_CANVAS = (By.TAG_NAME, "canvas")  # Знайде будь-який canvas
```

✅ **Додано діагностику:**
- Виводить поточний URL
- Показує які локатори спробовано
- Показує чи знайдено елемент

✅ **Збільшено затримки після логіну:**
- 2 сек після Sign In
- 3 сек після OK button
- Дає час для редіректу

### Наступні кроки для налагодження:

#### 1. Перевірити URL після логіну
```python
# Додати в тест:
print(f"URL after login: {driver.current_url}")
```

#### 2. Зробити screenshot
```python
# Додати в тест:
driver.save_screenshot("after_login.png")
```

#### 3. Подивитися HTML структуру
```python
# Додати в тест:
print(driver.page_source[:1000])  # Перші 1000 символів
```

#### 4. Перевірити всі елементи canvas
```python
# Додати в тест:
canvases = driver.find_elements(By.TAG_NAME, "canvas")
print(f"Found {len(canvases)} canvas elements")
for i, canvas in enumerate(canvases):
    print(f"Canvas {i}: id={canvas.get_attribute('id')}, class={canvas.get_attribute('class')}")
```

### Команди для ручного тестування:

#### Відкрити браузер і залишити відкритим:
```python
from utils.driver_factory import DriverFactory
from utils.config import Config
from pages.home_page import HomePage
from pages.login_page import LoginPage

driver = DriverFactory.create_driver()
home = HomePage(driver)
home.open()
home.click_build_for_free()

login = LoginPage(driver)
login.login(Config.EMAIL, Config.PASSWORD)

# Браузер залишиться відкритим для інспекції
input("Press Enter to close browser...")
driver.quit()
```

#### Виконати в PowerShell:
```powershell
.venv\Scripts\python.exe -c "
from utils.driver_factory import DriverFactory
from utils.config import Config
from pages.home_page import HomePage
from pages.login_page import LoginPage
import time

driver = DriverFactory.create_driver()
home = HomePage(driver)
home.open()
time.sleep(2)
home.click_build_for_free()
time.sleep(2)

login = LoginPage(driver)
login.login(Config.EMAIL, Config.PASSWORD)

print('Waiting for builder...')
time.sleep(10)
print(f'Current URL: {driver.current_url}')

canvases = driver.find_elements('tag name', 'canvas')
print(f'Found {len(canvases)} canvas elements')

input('Press Enter to close...')
driver.quit()
"
```

### Тимчасові рішення:

#### Збільшити таймаут:
```python
# В utils/config.py
BUILDER_LOAD_TIMEOUT = 120  # Збільшити до 2 хвилин
```

#### Додати явне очікування URL:
```python
# В tests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Дочекатися певного URL
WebDriverWait(driver, 30).until(
    EC.url_contains("builder")  # або який URL має бути
)
```

#### Чекати будь-який canvas:
```python
# В builder_page.py
def is_any_canvas_present(self):
    try:
        canvases = self.driver.find_elements(By.TAG_NAME, "canvas")
        return len(canvases) > 0
    except:
        return False
```

### Що перевірити на сайті вручну:

1. ✓ Відкрити https://events.shooters.global/
2. ✓ Натиснути "Build for Free"
3. ✓ Ввести email та password
4. ✓ Натиснути Sign In
5. ❓ **ЯКА СТОРІНКА З'ЯВЛЯЄТЬСЯ?**
6. ❓ **ЧИ Є КНОПКА OK?**
7. ❓ **КУДИ РЕДІРЕКТИТЬ ПІСЛЯ OK?**
8. ❓ **ЧИ З'ЯВЛЯЄТЬСЯ CANVAS АВТОМАТИЧНО?**
9. ❓ **ЧИ ПОТРІБНО ЩЕ ЩОСЬ НАТИСНУТИ?**

### Перевірка в браузері DevTools:

1. Відкрити DevTools (F12)
2. Після логіну виконати в Console:
```javascript
// Знайти всі canvas
document.querySelectorAll('canvas')

// Знайти canvas з ID
document.getElementById('unity-app-canvas')

// Показати всі canvas з атрибутами
Array.from(document.querySelectorAll('canvas')).map(c => ({
    id: c.id,
    class: c.className,
    visible: c.offsetParent !== null
}))
```

### Логи для аналізу:

Тест виводить:
- ✓ OK button clicked after login
- Current URL: [який URL?]
- Waiting for canvas element...
- [Результат пошуку]

**ПОТРІБНО ПОБАЧИТИ ЦІ ЛОГИ ПРИ ЗАПУСКУ ТЕСТУ!**

---

**Створено:** 17 жовтня 2025  
**Статус:** В процесі налагодження  
**Наступний крок:** Запустити тест і проаналізувати логи
