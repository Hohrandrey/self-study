from pydantic import BaseModel

class user_login(BaseModel):
    username: str
    password: str
    id: str | None = None
    last_login: int | None = None