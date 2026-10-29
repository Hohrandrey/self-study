# db.py
# Симуляция базы данных пользователей

USERS_DATA = [
    {"username": "admin", "password": "adminpass"}  # В реальной базе данных пароли должны храниться в виде хэшей
]

def get_user(username: str):
    """
    Функция для поиска пользователя по имени пользователя.
    В реальном проекте это должно быть запросом к базе данных.
    """
    for user in USERS_DATA:
        if user.get("username") == username:
            return user
    return None
