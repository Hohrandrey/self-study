from fastapi import FastAPI

#app = FastAPI()
my_app = FastAPI()

#@app.get("/")
@my_app.get("/")
async def root():
    #return {"message": "Добро пожаловать в моё приложение FastAPI!"}
    return {"message": "Авторелоад действительно работает"}

# запуск был через uvicorn main:app --reload
# теперь запуск через: uvicorn main:my_app --reload