from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from .models.user_model import User

app = FastAPI()
security = HTTPBasic()


USER_DATA = [
    User(username="admin", password="admin"),
    User(username="john", password="1234")
]

def identity_user(username: str):
    for user in USER_DATA:
        if user.username == username:
            return user
    return None

def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    user = identity_user(credentials.username)
    if user is None or user.password != credentials.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"}
        )
    return user

@app.get('/login')
async def get_login(user: User = Depends(authenticate_user)):
    return {'message': 'You got my secret, welcome', 'user': user}