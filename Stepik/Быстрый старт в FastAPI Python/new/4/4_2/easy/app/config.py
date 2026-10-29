from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        # файл с окружение
        env_file = '.env'
        # зависимость от регистра
        case_sensitive = True
