from fastapi import FastAPI
from pydantic import BaseModel

app_hard = FastAPI()

class Nums(BaseModel):
    num1 : float
    num2: float


@app_hard.post("/calculate")
async def calculate(res:Nums):
    return {f"Результат вычислений: {res.num1} + {res.num2} = {res.num1+res.num2}"}
