from fastapi import FastAPI, Cookie, Response, HTTPException
from .models.user_model import user_login
from uuid import uuid4


app = FastAPI()
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


@app.post('/login')
async def login(login: user_login, response: Response):
    for el in dict_of_users:
        if el['username'] == login.username and el['password'] == login.password:
            id = str(uuid4())
            el['id'] = id
            response.set_cookie(key='session_token', value=id, httponly=True)
            return el
    return {"message": "Unauthorized"}


@app.get('/user')
async def get_user(session_token = Cookie(None)):
    for el in dict_of_users:
        if session_token and session_token == el['id']:
            return el
    raise HTTPException(status_code=401, detail="Unauthorized")