# 🔧 Troubleshooting Canvas Loading

## Проблема: Canvas не знаходиться після логіну

### Можливі причини:

1. **Canvas завантажується на іншій сторінці**
   - Після логіну може бути редірект
   - Потрібна додаткова навігація

2. **Canvas завантажується довго**
   - Unity додаток може завантажуватися 2-3 хвилини
   - Потрібно більше часу

3. **Canvas має інший ID або структуру**
   - ID може бути динамічним
   - Елемент може бути в iframe

### Діагностика:

Запустіть діагностичний скрипт:
```powershell
.venv\Scripts\python.exe diagnostic_script.py
```

Це покаже:
- URL після кожного кроку
- Скільки canvas елементів знайдено
- Атрибути кожного canvas
- Чи є кнопка Next
- Screenshot сторінки
- Частину HTML коду

### Ручна перевірка:

1. Відкрийте https://events.shooters.global/
2. Натисніть "Build for Free"  
3. Залогіньтесь
4. Натисніть OK (якщо є)
5. **ЩО ВИ БАЧИТЕ?**
   - Чи з'являється canvas автоматично?
   - Чи потрібно куди

сь перейти?
   - Чи є кнопка "Start", "Create", "New Project"?
   - Який URL після всіх дій?

### Можливі рішення:

#### Рішення 1: Збільшити timeout
```python
# В utils/config.py
BUILDER_LOAD_TIMEOUT = 180  # 3 хвилини
```

#### Рішення 2: Чекати конкретний URL
```python
# В builder_page.py
from selenium.webdriver.support import expected_conditions as EC

def wait_for_builder_url(self):
    WebDriverWait(self.driver, 60).until(
        EC.url_contains("builder")  # або який URL має бути
    )
```

#### Рішення 3: Canvas в iframe
```python
# Якщо canvas в iframe
def switch_to_canvas_iframe(self):
    iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
    for iframe in iframes:
        self.driver.switch_to.frame(iframe)
        try:
            canvas = self.driver.find_element(By.ID, "unity-app-canvas")
            return True  # Canvas знайдено в цьому iframe
        except:
            self.driver.switch_to.default_content()
    return False
```

#### Рішення 4: Чекати завантаження Unity
```python
# Чекати поки Unity ініціалізується
def wait_for_unity_ready(self):
    # Unity додає клас або атрибут коли готовий
    WebDriverWait(self.driver, 120).until(
        lambda d: d.execute_script(
            "return typeof UnityLoader !== 'undefined'"
        )
    )
```

### Якщо canvas НЕ на тій сторінці:

Можливо потрібно:
1. Натиснути "Create Project" або подібну кнопку
2. Вибрати шаблон проекту
3. Дочекатися ще одного редіректу

**Подивіться в diagnostic_script.py що він знайшов!**
