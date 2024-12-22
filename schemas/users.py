from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    name: str
    email: str
    is_active: bool = True

class User(UserBase):
     id: int
    

class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    name: Optional [str] = None
    email: Optional [str] = None
    is_active: bool = True
