# main.py
from fastapi import FastAPI, Depends
from security import create_jwt_token, get_user_from_token
from models import User
from db import get_user, USERS_DATA

app = FastAPI()

# Маршрут для аутентификации пользователя.
# Если данные правильные, возвращается JWT токен.
@app.post("/login")
async def login(user_in: User):
    """
    Этот маршрут проверяет учетные данные пользователя и возвращает JWT токен, если данные правильные.
    """
    # В реальной практике пароли необходимо сравнивать с хэшами, а не в открытом виде
    for user in USERS_DATA:
        if user.get("username") == user_in.username and user.get("password") == user_in.password:
            # Если проверка прошла успешно, генерируем токен для пользователя
            token = create_jwt_token({"sub": user_in.username})  # "sub" — это subject, в нашем случае имя пользователя
            return {"access_token": token, "token_type": "bearer"}
    # Если данные неверные, возвращаем ошибку
    return {"error": "Invalid credentials"}

# Защищённый маршрут, который возвращает информацию о пользователе,
# если токен в запросе действителен.
@app.get("/about_me")
async def about_me(current_user: str = Depends(get_user_from_token)):
    """
    Этот маршрут защищен и требует токен. Если токен действителен, мы возвращаем информацию о пользователе.
    """
    user = get_user(current_user)
    if user:
        return user
    # Если пользователь не найден, возвращаем ошибку
    return {"error": "User not found"}
