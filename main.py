from fastapi import FastAPI

# Создаём приложение FastAPI.
app = FastAPI()


# Главная страница возвращает приветствие в формате JSON.
@app.get("/")
async def root():
    return {"message": "Hello Web"}


# Информация о курсе.
@app.get("/about")
async def about():
    return {"course": "Web Development"}


# Список пользователей.
@app.get("/users")
async def users():
    return {"users": ["Alex", "Maria", "Ivan"]}


# Вариант 9: служба такси, сущности — водитель и поездка.
@app.get("/info")
async def info():
    return {
        "variant": 9,
        "theme": "Taxi Service",
        "entities": ["Driver", "Trip"]
    }


# Дополнительное приветствие.
@app.get("/hello")
async def hello():
    return {"message": "Привет!"}


# Учебный пример контактных данных.
@app.get("/contacts")
async def contacts():
    return {"email": "student@example.com"}


# Проверка работы сервера.
@app.get("/status")
async def status():
    return {"status": "ok"}
