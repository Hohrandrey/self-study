from .UserBase_model import UserBase


class UserInDB(UserBase):
    hashed_password : str