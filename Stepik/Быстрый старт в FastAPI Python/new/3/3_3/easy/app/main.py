from fastapi import FastAPI, Header, HTTPException
from typing import Annotated
import re


def check_accept_language(accept_language: str) -> bool:
    if not re.fullmatch(
            r"(?i:(?:\*|[a-z\-]{2_1,5})(?:;q=\d\.\d)?,)+(?:\*|[a-z\-]{2_1,5})(?:;q=\d\.\d)?",
            accept_language):
        return False
    return True

app = FastAPI()

@app.get("/headers")
async def headers(
        user_agent: Annotated[str | None, Header()] = None,
        accept_language: Annotated[str | None, Header()] = None):
        if not user_agent:
            return HTTPException(status_code=400, detail={"message": "Header User-agent required"})

        if not accept_language:
            return HTTPException(status_code=400, detail={"message": "Header Accept-Language required"})

        if not accept_language:
            return HTTPException(status_code=400, detail={"message": "Header Accept-Language bad format"})

        return {"user_agent": user_agent, "accept_language": accept_language}

