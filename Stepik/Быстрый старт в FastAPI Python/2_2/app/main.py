from fastapi import FastAPI
from .models_app.user_model import User


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}


#задание базового уровня
User = User(name = "John Doe", id = 1)
@app.get("/user")
async def read_user():
    return User