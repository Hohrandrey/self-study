from pydantic import  BaseModel, Field, field_validator, EmailStr


class UserCreate(BaseModel):
    name: str = Field(min_length=1)
    email: EmailStr
    age : int | None
    is_subscribed : bool

    @field_validator('age')
    def age_validator(cls, age):
        if age < 0 or age > 150:
            raise ValueError("Некорректный возраст")