from fastapi import FastAPI, HTTPException, Header
import re

app = FastAPI()

def check_accept_language_header(accept_language):
    pass


@app.get("/headers")
async def get_headers(user_agent: str = Header(None), accept_language: str = Header(None)):
    if not accept_language:
        raise HTTPException(status_code=400, detail="Header Accept-Language not found")

    if not user_agent:
        raise HTTPException(status_code=400, detail="Header User-Agent not found")

    if not re.fullmatch("(?i:(?:\*|[a-z\-]{2,5})(?:;q=\d\.\d)?,)+(?:\*|[a-z\-]{2,5})(?:;q=\d\.\d)?", accept_language):
        raise HTTPException(status_code=400, detail="Header Accept-Language bad format")

    return {"User-Agent" : user_agent, "Accept-Language" : accept_language}