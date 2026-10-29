from fastapi import FastAPI, Depends
import jwt


app = FastAPI()


@app.post('login')
async def login():
    pass


@app.get('/protected_resource')
async def protected_resource():
    pass