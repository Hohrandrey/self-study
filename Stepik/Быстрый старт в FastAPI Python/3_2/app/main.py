from fastapi import FastAPI, Response, Cookie
from .models.login_model import user_login
from uuid import uuid4
from .encrypt_decrypt import encrypt_decrypt

app = FastAPI()


db = [
    {"user_id": str(uuid4()), "username": "user123", "password": "password123"},
    {"user_id": str(uuid4()), "username": "user456", "password": "password456"},
]

sessions = []


@app.post("/login")
async def login(user: user_login, response: Response):
    for elem in db:
        if user.username == elem["username"] and user.password == elem["password"]:
            user_id = elem["user_id"]
            sessions.append(user_id)
            signature = encrypt_decrypt(user_id)
            session_token = f"{user_id}.{signature}"
            response.set_cookie(
                key="session_token", value=session_token, httponly=True, max_age=3600
            )
            return {"message": "Authorized successfully"}
    return {"message": "Unauthorized"}


# Средний уровень
@app.get("/profile")
async def profile(session_token=Cookie(None)):
    cookie_halfs = session_token.split(".", maxsplit=1)
    user_id = cookie_halfs[0]
    if user_id == encrypt_decrypt(cookie_halfs[1], False):
        for elem in db:
            if elem["user_id"] == user_id:
                return {"username": elem["username"], "password": elem["password"]}
    return {"message": "Unauthorized"}
