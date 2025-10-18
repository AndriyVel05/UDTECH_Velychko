# GitHub Setup Instructions

## Крок 1: Ініціалізація Git репозиторію

Відкрийте термінал у папці проекту та виконайте:

```bash
git init
git add .
git commit -m "Initial commit: Automation test project for Shooters Global"
```

## Крок 2: Створення GitHub репозиторію

1. Перейдіть на https://github.com/
2. Натисніть "New repository" (зелена кнопка)
3. Введіть назву репозиторію: `TestTask_UDTech` або `ShootersGlobal-Automation`
4. Виберіть "Public"
5. **НЕ** додавайте README, .gitignore, або license (вони вже є)
6. Натисніть "Create repository"

## Крок 3: Підключення локального репозиторію до GitHub

GitHub покаже вам команди. Виконайте їх у терміналі:

```bash
git remote add origin https://github.com/YOUR_USERNAME/TestTask_UDTech.git
git branch -M main
git push -u origin main
```

Замініть `YOUR_USERNAME` на ваш GitHub username.

## Крок 4: Перевірка

Перейдіть на https://github.com/YOUR_USERNAME/TestTask_UDTech та перевірте, що всі файли завантажилися.

## Важливо!

- Файл `.env` буде автоматично проігнорований (додано в `.gitignore`)
- Ваші облікові дані **НЕ** будуть опубліковані на GitHub
- Переконайтеся, що `.env` є в списку `.gitignore` перед push

## Оновлення репозиторію (після змін)

```bash
git add .
git commit -m "Опис змін"
git push
```

## Клонування репозиторію на іншому комп'ютері

```bash
git clone https://github.com/YOUR_USERNAME/TestTask_UDTech.git
cd TestTask_UDTech
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows PowerShell
pip install -r requirements.txt
# Створіть .env файл з вашими credentials
pytest tests/ -v
```
