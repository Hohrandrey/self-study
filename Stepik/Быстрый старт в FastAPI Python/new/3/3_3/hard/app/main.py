from datetime import datetime
from fastapi import FastAPI, Response, Header, HTTPException
from .models.CommonHeaders_model import CommonHeaders
from typing import Annotated


app = FastAPI()


@app.get("/headers")
async def get_headers(headers: Annotated[CommonHeaders, Header()]):
    return headers


@app.get("/info")
async def get_info(headers: Annotated[CommonHeaders, Header()], response: Response):
    response.headers["X-Server-Time"]= datetime.now().isoformat()
    return {
        "message": "Добро пожаловать! Ваши заголовки успешно обработаны.",
        "headers": headers
    }