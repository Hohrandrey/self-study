from fastapi import FastAPI, Header, HTTPException

app = FastAPI()


@app.get("/headers")
def get_headers(user_agent: str | None = Header(None), accept_language: str | None = Header(None)):
    if not user_agent or not accept_language:
        raise HTTPException(status_code=<int>, detail="<str>")
    return {"User-Agent" : user_agent, "Accept-Language" : accept_language}