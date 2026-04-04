from fastapi import FastAPI, Response, Cookie
from .models.login_model import user_login
from uuid import uuid4


app = FastAPI()


db = {
  "username": "user123",
  "password": "password123"
}


sessions = []


@app.post("/login")
async def login(user: user_login, response: Response):
    if user.username == db["username"] and user.password == db["password"]:
        key = str(uuid4())
        sessions.append(key)
        response.set_cookie(key="session_token", value=key, httponly=True)
        return {"session_token": key}
    return {"message": "Unauthorized"}


@app.get("/user")
async def user(session_token=Cookie(None)):
    if session_token in sessions:
        return {
            "username": db["username"],
            "message": "Authorized successfully"
        }
    return {"message": "Unauthorized"}