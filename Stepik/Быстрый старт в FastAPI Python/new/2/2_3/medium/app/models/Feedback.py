from pydantic import BaseModel, Field, field_validator

class Feedback(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)

    @field_validator('message')
    @classmethod
    def validate_message(cls, value:str):
        if any(bad_word in value.lower() for bad_word in ['редис', 'бяк', 'козяв']):
            raise ValueError("Использование недопустимых слов")
        return value