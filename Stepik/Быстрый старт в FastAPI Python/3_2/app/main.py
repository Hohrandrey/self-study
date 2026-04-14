import time
from fastapi import FastAPI, Response, Cookie
from .models.login_model import user_login
from uuid import uuid4
from .encrypt_decrypt import encrypt_decrypt

app = FastAPI()


db = [
    {"user_id": str(uuid4()), "username": "user123", "password": "password123"},
    {"user_id": str(uuid4()), "username": "user456", "password": "password456"},
]



def cookie(id):
    user_id = id
    time_stamp = int(time.time())
    signature = encrypt_decrypt(user_id+'.'+str(time_stamp))
    session_token = f"{user_id}.{time_stamp}.{signature}"

    return session_token


@app.post("/login")
async def login(user: user_login, response: Response):
    for elem in db:
        if user.username == elem["username"] and user.password == elem["password"]:
            session_token = cookie(elem["user_id"])

            response.set_cookie(
                key="session_token",
                value=session_token,
                httponly=True,
                max_age=300,
                secure=False
            )

            return {"message": "Authorized successfully"}
    return {"message": "Unauthorized"}



@app.get("/profile")
async def profile(response: Response, session_token=Cookie(None)):
    if not session_token:
        response.status_code = 401
        return {"message": "Invalid session"}

    cookie_thirds = session_token.split(".", maxsplit=2)
    if len(cookie_thirds) != 3:
        response.status_code = 401
        return {"message": "Invalid session"}

    user_id = cookie_thirds[0]
    timestamp_cookie = int(cookie_thirds[1])
    signature = cookie_thirds[2]
    enc_time_id = encrypt_decrypt(signature, False)

    if not enc_time_id or enc_time_id != f"{user_id}.{timestamp_cookie}":
        response.status_code = 401
        return {"message": "Invalid session"}

    cur_time_stamp = int(time.time())

    if cur_time_stamp - timestamp_cookie >= 300:
        response.status_code = 401
        return {"message": "Session expired"}


    username = None
    password = None
    for elem in db:
        if elem["user_id"] == user_id:
            username = elem["username"]
            password = elem["password"]

    if not username or not password:
        response.status_code = 401
        return {"message": "Invalid session"}

    if 180 <= cur_time_stamp - timestamp_cookie < 300:
        new_session_token = cookie(user_id)
        response.set_cookie(
            key="session_token",
            value=new_session_token,
            httponly=True,
            max_age=300,
            secure=False
        )
    return {"username": username, "password": password}
