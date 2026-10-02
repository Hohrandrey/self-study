from fastapi import FastAPI, Response, Cookie, HTTPException
from .models.user_model import user_login
from uuid import uuid4
from datetime import datetime
from time import time
from itsdangerous import URLSafeSerializer, SignatureExpired, BadSignature

app = FastAPI()

#БД
dict_of_users = [
    {
        'username':'master',
        'password':'1234',
        'id' : None,
        'last_login' : None
    },
    {
        'username':'user2',
        'password':'67',
        'id' : None,
        'last_login' : None
    }
]


id_serializer = URLSafeSerializer(secret_key="!!!Супер_Секретный_Ключ!!!")


@app.post('/login')
async def login(user: user_login, response: Response):
    s_id = str(uuid4())
    timest = int(time())
    session_token = id_serializer.dumps({"sid": s_id, "ld": timest})
    for el in dict_of_users:
        if el['username'] == user.username and el['password'] == user.password:
            el['id'] = s_id
            response.set_cookie(key='session_token', value=session_token, httponly=True, max_age=300, secure=False)
            return el
    return "Неправильный логин или пароль"

@app.get('/')
async def root():
    return dict_of_users

#
@app.get('/profile')
async def profile(session_token = Cookie(None)):
    for el in dict_of_users:
        try:
            checked_id_and_date = id_serializer.loads(session_token, max_age=180)
            checked_id = checked_id_and_date['sid']
        except SignatureExpired:
            raise HTTPException(status_code=401, detail={"message":"Session expired"})
        except BadSignature:
            raise HTTPException(status_code=401, detail={"message": "Invalid session"})

        if session_token and (checked_id in el.values()):
            return el

    raise HTTPException(status_code=401, detail={"message": "Unauthorized"})