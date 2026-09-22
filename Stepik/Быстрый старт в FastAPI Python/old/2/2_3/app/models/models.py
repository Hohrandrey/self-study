from pydantic import BaseModel, Field, field_validator, EmailStr


class Contact(BaseModel):
    email: EmailStr
    phone: str = Field(default=None, min_length=7, max_length=15)

    @field_validator("phone")
    def check_phone(cls, phone):
        if (not phone.isdigit()) and phone is not None:
            raise ValueError("Номер должен состоять только из чисел!")


class Feedback(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    message: str = Field(min_length=10, max_length=500)
    contact: Contact

    @field_validator("message")
    def check_message(cls, message):
        bad_words = ["редис", "бяк", "козявка"]
        for word in bad_words:
            if word in message:
                raise ValueError("Использование недопустимых слов")
        return message
