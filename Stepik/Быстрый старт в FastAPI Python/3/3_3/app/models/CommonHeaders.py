from pydantic import BaseModel

class CommonHeaders(BaseModel):
    user_agent: str