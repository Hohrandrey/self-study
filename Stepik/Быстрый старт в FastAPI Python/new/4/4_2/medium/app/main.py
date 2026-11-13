from fastapi import FastAPI, Depends, HTTPException, status, Response
from fastapi.security import OAuth2PasswordRequestForm
from passlib.hash import bcrypt
import secrets
from .security import create_jwt_token, get_user_from_token
from fastapi_limiter.depends import RateLimiter
from pyrate_limiter import Duration, Limiter, Rate


USERS_DATA = [
    {"username": "admin", "password": bcrypt.hash("adminpass")}
]
app = FastAPI()


def find_user_in_DB(username):
    for user in USERS_DATA:
        if secrets.compare_digest(user["username"], username):
            return user
    return None


@app.post('/register',
          dependencies=[Depends(RateLimiter(limiter=Limiter(Rate(1, 60))))]
          )
async def register(user: OAuth2PasswordRequestForm = Depends()):
    if find_user_in_DB(user.username):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="User already exists",
                            headers={'WWW-Authenticate': 'Bearer'}
                            )
    else:
        hashed_password = bcrypt.hash(user.password)
        USERS_DATA.append({"username":user.username,"password":hashed_password})
        return {"message":"New user created"}


@app.post('/login',
          dependencies=[Depends(RateLimiter(limiter=Limiter(Rate(5, 60))))]
          )
async def login(user: OAuth2PasswordRequestForm = Depends()):
    user_from_DB = find_user_in_DB(user.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={'WWW-Authenticate': 'Bearer'}
        )
    elif bcrypt.verify(user.password, user_from_DB['password']):
        token = create_jwt_token({"sub": user.username})
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization failed",
            headers={'WWW-Authenticate': 'Bearer'}
        )


@app.get('/protected_resource')
async def protected_resource(cur_user: str = Depends(get_user_from_token)):
    user = find_user_in_DB(cur_user)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="User not found",
        headers={'WWW-Authenticate': 'Bearer'}
    )