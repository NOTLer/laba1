# Taxi Service — лабораторная работа №1

Вариант 9. Сущности: Driver (водитель), Trip (поездка).

Простой backend на FastAPI. Все маршруты возвращают JSON.

## Запуск

Открыть терминал в папке `laba1`:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Сервер: http://127.0.0.1:8000

Swagger UI: http://127.0.0.1:8000/docs

## Что сделано и как

В `main.py` создано приложение `app = FastAPI()`. Декораторы `@app.get(...)` задают адреса GET-запросов. Функции возвращают словари Python, которые FastAPI преобразует в JSON.

| Маршрут | Ответ |
| --- | --- |
| `/` | Приветствие Hello Web |
| `/about` | Название курса |
| `/users` | Список пользователей |
| `/info` | Вариант 9, Taxi Service, сущности Driver и Trip |
| `/hello` | Приветствие на русском |
| `/contacts` | Учебный email |
| `/status` | Статус ok |

Последние три маршрута — домашнее задание. Комментарии в коде стоят на отдельных строках.

## Git

Эта папка — отдельный локальный репозиторий. GitHub для коммитов не нужен.

После изменения файлов выполнить из папки `laba1`:

```bash
git add .
git commit -m "Update lab 1"
git status
```

Посмотреть историю:

```bash
git log --oneline
```
