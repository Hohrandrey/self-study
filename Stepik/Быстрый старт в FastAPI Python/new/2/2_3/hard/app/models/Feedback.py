from pydantic import BaseModel, Field, field_validator, EmailStr


class Contact_model(BaseModel):
    email: EmailStr = Field(..., min_length=3, max_length=254)
    phone: str = Field(None, min_length=7, max_length=15)

    @field_validator('phone')
    @classmethod
    def validate_phone(cls, number:str):
        if all(num.isdigit() for num in number.lower()):
            return number
        raise ValueError("Использование недопустимых слов")


class Feedback(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)
    contact: Contact_model

    @field_validator('message')
    @classmethod
    def validate_message(cls, value:str):
        if any(bad_word in value.lower() for bad_word in ['редис', 'бяк', 'козяв']):
            raise ValueError("Использование недопустимых слов")
        return value

