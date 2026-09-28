from fastapi import FastAPI, Response, Cookie, HTTPException
from .models.user_model import user_login
from uuid import uuid4
from itsdangerous import URLSafeSerializer


app = FastAPI()

#БД
dict_of_users = [
    {
        'username':'master',
        'password':'1234',
        'id' : None
    },
    {
        'username':'master',
        'password':'1234',
        'id' : None
    }
]

#
id_serializer = URLSafeSerializer(secret_key="!!!Супер_Секретный_Ключ!!!")

#
@app.post('/login')
async def login(user: user_login, response: Response):
    for el in dict_of_users:
        if el['username'] == user.username and el['password'] == user.password:
            s_id = str(uuid4())
            session_token = id_serializer.dumps(s_id)
            el['id'] = s_id
            response.set_cookie(key='session_token', value=session_token, httponly=True, max_age=120)
            return el
    return "Неправильный логин или пароль"

#
@app.get('/profile')
async def profile(session_token = Cookie(None)):
    for el in dict_of_users:
        try:
            checked_id = id_serializer.loads(session_token)
        except:
            raise HTTPException(status_code=401, detail={"message": "Invalid session"})

        if session_token and checked_id in el.values():
            return el

    raise HTTPException(status_code=401, detail={"message": "Unauthorized"})