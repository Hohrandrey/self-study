import jwt
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from .config import Settings


oath2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_jwt_token(data: dict) -> str:
    to_encode = data.copy()
    expire_time = datetime.now()