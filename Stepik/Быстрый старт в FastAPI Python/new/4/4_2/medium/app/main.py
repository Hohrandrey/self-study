from fastapi import FastAPI, Depends, HTTPException, status, Response
from fastapi.security import OAuth2PasswordRequestForm
from passlib.hash import bcrypt
import secrets


USERS_DATA = [
    {"username": "admin", "password": bcrypt.hash("adminpass")}
]
app = FastAPI()


def find_user_in_DB(username):
    for user in USERS_DATA:
        if secrets.compare_digest(user["username"], username):
            return True
    return False


@app.post('/register')
async def register(user: OAuth2PasswordRequestForm = Depends()):
    if find_user_in_DB(user.username):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="User already exists")
    else:
        hashed_password = bcrypt.hash(user.password)
        USERS_DATA.append({"username":user.username,"password":hashed_password})
        return {"message":"New user created"}


@app.post('/login')
async def login(user):
    if not find_user_in_DB(user.username):
        pass