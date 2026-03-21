from pydantic import BaseModel, Field, field_validator, EmailStr


class Contact(BaseModel):
    email : EmailStr
    phone : str = Field(min_lenght = 7, max_lenght = 15)


class Feedback(BaseModel):
    name : str = Field(min_lenght = 2, max_lenght = 50)
    message : str = Field(min_lenght = 10, max_lenght = 500)
    contact : Contact

    @field_validator('message')
    def check_message(cls, message):
        bad_words = ['редис', 'бяк', 'козявка']
        for word in bad_words:
            if word in message:
                raise ValueError("Использование недопустимых слов")
        return message