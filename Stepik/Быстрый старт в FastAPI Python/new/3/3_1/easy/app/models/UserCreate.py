from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int | None = Field(None, ge=0, le=130)
    is_subscribed: bool | None = None