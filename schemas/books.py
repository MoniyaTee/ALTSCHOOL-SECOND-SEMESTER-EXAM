from pydantic import BaseModel
from typing import Optional


class BookBase(BaseModel):
    name: str
    email: str
    is_availabe: bool = True

class Book(BookBase):
     id: int
    

class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    name: Optional [str] = None
    email: Optional [str] = None
    is_available: bool = True