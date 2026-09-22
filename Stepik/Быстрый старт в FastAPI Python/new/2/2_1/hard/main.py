import decimal

from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class nums(BaseModel):
    num1: decimal.Decimal
    num2: decimal.Decimal

@app.post('/calculate')
async def root(data: nums):
    return data, {'result': data.num1 + data.num2}