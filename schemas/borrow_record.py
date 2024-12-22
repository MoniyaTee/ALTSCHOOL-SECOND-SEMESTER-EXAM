from pydantic import BaseModel
from typing import Optional
from datetime import date

class BorrowRecord(BaseModel):
    user_id: int
    book_id: int


class Borrow(BorrowRecord):
    id: int
    borrow_date: date


class BorrowCreate(BorrowRecord):
    pass


class BorrowReturn(BorrowRecord):
    return_date: Optional[date] = None