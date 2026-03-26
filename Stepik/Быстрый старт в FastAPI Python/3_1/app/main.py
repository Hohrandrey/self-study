from fastapi import FastAPI
from .models.models import UserCreate

app = FastAPI()

users = []

@app.post("/create_user")
async def create_user(user: UserCreate):
    users.append(user)
    return user


@app.get("/product/{product_id}")
async def res(product_id):
    return {users[product_id]}


@app.get("/products/search")
async def res(keyword, category = None, limit = None):
    if category:
