from pydantic import BaseModel, field_validator
import re

class CommonHeaders(BaseModel):
    user_agent: str
    accept_language: str
    x_current_version: str

    @field_validator('accept_language')
    @classmethod
    def accept_language_validator(cls, accept_language: str) -> str:
        pattern = r'^[a-zA-Z]{1,8}(?:-[a-zA-Z0-9]{1,8})*(?:\s*;\s*q\s*=\s*\d(?:\.\d{1,3})?)?(?:\s*,\s*[a-zA-Z]{1,8}(?:-[a-zA-Z0-9]{1,8})*(?:\s*;\s*q\s*=\s*\d(?:\.\d{1,3})?)?)*$'
        if not re.fullmatch(pattern, accept_language.strip()):
            raise ValueError({"message": "Wrong structure accept_language"})
        return accept_language


    @field_validator('x_current_version')
    @classmethod
    def x_current_version_validator(cls, x_current_version: str) -> str:
        MINIMUM_APP_VERSION = "0.0.2".split('.')
        pattern = r'^\d+\.\d+\.\d+$'
        if not re.fullmatch(pattern, x_current_version):
            raise ValueError({"message": "Wrong structure x_current_version"})
        if x_current_version.split('.') < MINIMUM_APP_VERSION:
            raise ValueError({"message": "Too old version"})
        return x_current_version