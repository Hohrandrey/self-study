from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


"""
запуск: uvicorn main:app --reload
шабло: uvicorn "название файла":"Название функции" --reload
http://localhost:8000
"""
