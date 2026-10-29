from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = SettingsConfigDict(
        # файл с окружением
        env_file = '.env',
        # зависимость от регистра
        case_sensitive = True,
        # игнорирование остальных переменных
        extra = 'ignore'
    )


# кэшируем настройки
@lru_cache()
def get_settings():
    return Settings()