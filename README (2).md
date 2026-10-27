# Practice 01 — First FastAPI Backend

## Цель занятия

Сегодня мы:

- создадим backend на FastAPI
- запустим web server
- создадим API endpoints
- посмотрим Swagger UI
- сделаем первый git commit

---

# Что должно получиться

К концу занятия у вас должен работать backend:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs

---

# 1. Проверка окружения

## Python

Проверьте версию Python:

```bash
python --version
```

или:

```bash
py --version
```

---

## Git

```bash
git --version
```

---

## VS Code

Убедитесь, что VS Code установлен.

---

# 2. Создание проекта

Создайте папку проекта:

```bash
mkdir web-course
cd web-course
```

Откройте проект в VS Code:

```bash
code .
```

---

# 3. Установка FastAPI

Установите FastAPI и uvicorn:

```bash
python -m pip install fastapi uvicorn
```

---

# 4. Первый backend

Создайте файл:

```text
main.py
```

Добавьте код:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Web"}
```

---

# 5. Запуск сервера

Запустите backend:

```bash
python -m uvicorn main:app --reload
```

---

# 6. Проверка работы

Откройте в браузере:

```text
http://127.0.0.1:8000
```

Если всё работает — вы увидите JSON response.

---

# 7. Swagger UI

Откройте:

```text
http://127.0.0.1:8000/docs
```

Попробуйте:
- открыть endpoint
- нажать "Try it out"
- выполнить request

---

# 8. Добавляем новые endpoints

Добавьте endpoint:

```python
@app.get("/about")
async def about():
    return {"course": "Web Development"}
```

---

Добавьте ещё один endpoint:

```python
@app.get("/users")
async def users():
    return {
        "users": ["Alex", "Maria", "Ivan"]
    }
```

---

# 9. Индивидуальное задание

Тема вашего API указана в файле:

```text
variants.md
```

Создайте endpoint:

```text
GET /info
```

который возвращает информацию по вашей теме.

Пример:

```json
{
  "theme": "movies"
}
```

---

# 10. Git

Инициализируйте git repository:

```bash
git init
```

---

Проверьте статус:

```bash
git status
```

---

Сделайте первый commit:

```bash
git add .
git commit -m "Initial FastAPI project"
```

---

# Что должно быть в результате

У вас должен быть:

- working FastAPI project
- несколько endpoints
- Swagger UI
- git repository
- минимум 1 commit

---

# Частые проблемы

---

## uvicorn не найден

Попробуйте:

```bash
python -m uvicorn main:app --reload
```

---

## pip не найден

Попробуйте:

```bash
python -m pip install fastapi uvicorn
```

---

## Сервер не запускается

Проверьте:
- файл называется `main.py`
- объект называется `app`

---

# Домашнее задание

Добавьте endpoints:

- `/hello`
- `/contacts`
- `/status`

Каждый endpoint должен возвращать JSON.