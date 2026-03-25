from fastapi import FastAPI
from .models.models import UserCreate

app = FastAPI()

users = []

@app.post("/create_user")
async def create_user(user: UserCreate):
    users.append(user)
    return user


@app.get("/res")
async def res():
    return {"users": users}
