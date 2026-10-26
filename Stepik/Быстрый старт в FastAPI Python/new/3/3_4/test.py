from fastapi import FastAPI, Depends, status, HTTPException
from pydantic import BaseModel
from fastapi.security import HTTPBasic, HTTPBasicCredentials

#Создаем приложение FastAPI и экземпляр HTTPBasic, который будет использоваться для извлечения учетных данных из запросов.
app = FastAPI()
security = HTTPBasic()

#Здесь создается модель User, описывающая структуру данных пользователя, и простая симуляция базы данных в виде списка объектов
class User(BaseModel):
    username: str
    password: str

# Симуляция базы данных в виде списка объектов пользователей
USER_DATA = [
    User(**{"username": "user1", "password": "pass1"}),
    User(**{"username": "user2", "password": "pass2"})
]

#Функция authenticate_user получает учетные данные из запроса через механизм зависимостей FastAPI.
#Если пользователь не найден или введенный пароль не совпадает с сохраненным, выбрасывается исключение с кодом 401 (Unauthorized).
def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    user = get_user_from_db(credentials.username)
    if user is None or user.password != credentials.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return user

#Функция get_user_from_db ищет пользователя по имени в нашей симулированной базе данных.
#Если пользователь найден, функция возвращает его объект; если нет — возвращает None.
def get_user_from_db(username: str):
    for user in USER_DATA:
        if user.username == username:
            return user
    return None

@app.get("/protected_resource/")
def get_protected_resource(user: User = Depends(authenticate_user)):
    return {"message": "You have access to the protected resource!", "user_info": user}
