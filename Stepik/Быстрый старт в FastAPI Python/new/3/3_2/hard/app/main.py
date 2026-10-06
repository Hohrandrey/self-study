from fastapi import FastAPI, Response, Cookie, HTTPException
from .models.user_model import user_login
from uuid import uuid4
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
    for el in dict_of_users:
        if el['username'] == user.username and el['password'] == user.password:
            if not el['id']:
                s_id = str(uuid4())
                el['id'] = s_id
            else:
                s_id = el['id']

            timest = int(time())
            session_token = id_serializer.dumps({"sid": s_id, "ld": timest})
            response.set_cookie(key='session_token', value=session_token, httponly=True, max_age=300, secure=False)
            return el, session_token

    return "Неправильный логин или пароль"

@app.get('/')
async def root():
    return dict_of_users


@app.get('/profile')
async def profile(response: Response, session_token: str = Cookie(None)):
    if not session_token:
        raise HTTPException(status_code=401, detail={"message": "Invalid session"})

    try:
        checked_id_and_date = id_serializer.loads(session_token, max_age=300)
        checked_id = checked_id_and_date['sid']
    except SignatureExpired:
        raise HTTPException(status_code=401, detail={"message":"Session expired"})
    except BadSignature:
        raise HTTPException(status_code=401, detail={"message": "Invalid session"})

    timest = int(time())
    time_diff = timest - checked_id_and_date['ld']

    if time_diff > 300:
        raise HTTPException(status_code=401, detail={"message": "Session expired"})
    elif 180 <= time_diff <= 300:
        session_token = id_serializer.dumps({"sid": checked_id, "ld": timest})
        response.set_cookie(key='session_token', value=session_token, httponly=True, max_age=300, secure=False)

    for el in dict_of_users:
        if checked_id == el['id']:
            return el, session_token

    raise HTTPException(status_code=401, detail={"message": "Unauthorized"})