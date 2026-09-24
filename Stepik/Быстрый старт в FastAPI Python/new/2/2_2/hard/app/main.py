from fastapi import FastAPI
from .models.User import User

app = FastAPI()

@app.post('/user')
async def create_user(user: User):
    user_plus_adult = dict(user)
    user_plus_adult['is_adult'] = user.age >=18
    return user_plus_adult