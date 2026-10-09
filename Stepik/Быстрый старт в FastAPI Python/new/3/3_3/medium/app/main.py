from time import time
from fastapi import FastAPI, Response
from .models.CommonHeaders_model import CommonHeaders


app = FastAPI()


@app.get("/headers")
async def get_headers(headers: CommonHeaders):
    return headers


@app.get("/info")
async def get_info(headers: CommonHeaders, response: Response):
    response.headers["X-Server-Time"]=str(int(time()))
    return {
        "message": "Добро пожаловать! Ваши заголовки успешно обработаны.",
        "headers": headers
    }