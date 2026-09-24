from fastapi import FastAPI
from .models.user import User

app = FastAPI()
users = User(name = "John Doe", id = 1)

@app.get('/users')
async def get_users():
    return users