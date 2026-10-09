from pydantic import BaseModel, field_validator
from fastapi import Header
from typing import Annotated
import re

class CommonHeaders(BaseModel):
    user_agent: Annotated[str, Header()]
    accept_language: Annotated[str, Header()]

    @field_validator('accept_language')
    @classmethod
    def accept_language_validator(cls, accept_language: str) -> str:
        if not re.fullmatch(
                r"(?i:(?:\*|[a-z\-]{2_1,5})(?:;q=\d\.\d)?,)+(?:\*|[a-z\-]{2_1,5})(?:;q=\d\.\d)?",
                accept_language):
            raise ValueError({"message":"Wrong structure accept_language"})
        return accept_language
