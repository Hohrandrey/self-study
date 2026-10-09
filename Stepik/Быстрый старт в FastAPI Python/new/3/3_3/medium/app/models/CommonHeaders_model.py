from pydantic import BaseModel, field_validator
import re

class CommonHeaders(BaseModel):
    user_agent: str
    accept_language: str

    @field_validator('accept_language')
    @classmethod
    def accept_language_validator(cls, accept_language: str) -> str:
        pattern = r'^[a-zA-Z]{1,8}(?:-[a-zA-Z0-9]{1,8})*(?:\s*;\s*q\s*=\s*\d(?:\.\d{1,3})?)?(?:\s*,\s*[a-zA-Z]{1,8}(?:-[a-zA-Z0-9]{1,8})*(?:\s*;\s*q\s*=\s*\d(?:\.\d{1,3})?)?)*$'
        if not re.fullmatch(pattern, accept_language.strip()):
            raise ValueError({"message": "Wrong structure accept_language"})
        return accept_language
