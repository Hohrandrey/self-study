from pydantic import BaseModel, Field


class user_login(BaseModel):
    username: str
    password: str
