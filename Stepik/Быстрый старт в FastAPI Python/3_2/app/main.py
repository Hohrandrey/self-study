from fastapi import FastAPI, Response
from .models.login_model import user_login


app = FastAPI()


@app.post("/login")
async def login(user_login, response: Response):
    pass


@app.get("/user")
async def user():
    pass