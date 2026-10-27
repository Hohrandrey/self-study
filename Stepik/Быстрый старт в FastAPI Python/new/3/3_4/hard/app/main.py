import secrets
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext
from .models.User_model import User
from .models.UserInDB_model import UserInDB


app = FastAPI()
security = HTTPBasic()
fake_users_db = []
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def auth_user(credentials: HTTPBasicCredentials = Depends(security)) -> User:
    for el in fake_users_db:
        if (secrets.compare_digest(el.username.encode('utf-8'), credentials.username.encode('utf-8'))
                and pwd_context.verify(credentials.password, el.hashed_password)):
            return credentials.username
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                         detail="Incorrect username or password",
                         headers={"WWW-Authenticate" : "Basic"}
                         )


@app.post('/register')
async def register(user : User) -> dict:
    hashed_password = pwd_context.hash(user.password)
    fake_users_db.append(UserInDB(username=user.username, hashed_password=hashed_password))
    return {"message" : "User created successfully"}


@app.get('/login')
async def login(username : User = Depends(auth_user)):
    return {"message" : f"Welcome, {username}!"}


@app.get('/')
async def index():
    return fake_users_db