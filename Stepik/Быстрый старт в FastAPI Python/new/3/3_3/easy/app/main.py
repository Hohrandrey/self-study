from fastapi import FastAPI, Header, HTTPException
from typing import Annotated

app = FastAPI()

@app.get("/headers")
async def headers(
        user_agent: Annotated[str | None, Header()] = None,
        accept_language: Annotated[str | None, Header()] = None):
    return {"user_agent": user_agent, "accept_language": accept_language}

