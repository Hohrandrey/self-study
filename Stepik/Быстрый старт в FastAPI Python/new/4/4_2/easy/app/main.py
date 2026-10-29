from fastapi import FastAPI, Depends, HTTPException, status
from .security import create_jwt_token, get_user_from_token
from fastapi.security import OAuth2PasswordRequestForm


USERS_DATA = [
    {"username": "admin", "password": "adminpass"}  # В реальной базе данных пароли должны храниться в виде хэшей
]
app = FastAPI()


@app.post('/login')
async def login(user: OAuth2PasswordRequestForm = Depends()):
    for el in USERS_DATA:
        if el["username"] == user.username and el["password"] == user.password:
            token = create_jwt_token({'sub':user.username})
            return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={'WWW-Authenticate': 'Bearer'}
    )


@app.get('/protected_resource')
async def protected_resource(cur_user: str = Depends(get_user_from_token)):
    for user in USERS_DATA:
        if user.get("username") == cur_user:
            return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="User not found",
        headers={'WWW-Authenticate': 'Bearer'}
    )
