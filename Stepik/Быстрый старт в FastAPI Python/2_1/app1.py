from fastapi import FastAPI

app1 = FastAPI()


@app1.get("/")
async def app_start():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}
    """
    return {"message": "Авторелоад действительно работает"}
    """
