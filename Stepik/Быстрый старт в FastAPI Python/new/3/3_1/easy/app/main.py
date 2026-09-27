from fastapi import FastAPI
from .models.UserCreate import UserCreate

app = FastAPI()
users: list[UserCreate] = []


@app.post('/create_user')
async def create_user(user: UserCreate):
    users.append(user)
    return user

@app.get('/users')
async def get_users():
    return users