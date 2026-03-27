from fastapi import FastAPI
from .models.models import UserCreate

app = FastAPI()
#Задание по программированию базового уровня
"""
users = []

@app.post("/create_user")
async def create_user(user: UserCreate):
    users.append(user)
    return user
"""

#Задача программирования повышенной сложности
sample_product_1 = {
    "product_id": 123,
    "name": "Smartphone",
    "category": "Electronics",
    "price": 599.99
}

sample_product_2 = {
    "product_id": 456,
    "name": "Phone Case",
    "category": "Accessories",
    "price": 19.99
}

sample_product_3 = {
    "product_id": 789,
    "name": "Iphone",
    "category": "Electronics",
    "price": 1299.99
}

sample_product_4 = {
    "product_id": 101,
    "name": "Headphones",
    "category": "Accessories",
    "price": 99.99
}

sample_product_5 = {
    "product_id": 202,
    "name": "Smartwatch",
    "category": "Electronics",
    "price": 299.99
}

products = [sample_product_1, sample_product_2, sample_product_3, sample_product_4, sample_product_5]

@app.get("/product/{product_id}")
async def res(product_id:int):
    ans = f'Не найден товар с id - {product_id}'
    for dicts in products:
        if dicts["product_id"] == product_id:
            ans = dicts
    return ans


@app.get("/products/search")
async def res(keyword, category = None, limit = 10):
    ans = []
    if category:
        for dicts in products:
            if (dicts["category"] == category) and (keyword in dicts["name"]):
                ans.append(dicts)
    if len(ans) == 0:
        return 'Товары не найдены'
    return ans[:int(limit)]