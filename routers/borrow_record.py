from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import date
from typing import List
from database.db import users_db, books_db

borrow_router = APIRouter()


class BorrowRecord(BaseModel):
    user_id: int
    book_id: int
    borrow_date: date
    return_date: date = None


borrow_db = []


@borrow_router.post("/borrow")
def borrow_book(record: BorrowRecord):
    
    user = next((u for u in users_db if u["id"] == record.user_id), None)
    if not user or not user["is_active"]:
        raise HTTPException(status_code=400, detail="User not active or not found")

   
    book = next((b for b in books_db if b["id"] == record.book_id), None)
    if not book or not book["is_available"]:
        raise HTTPException(status_code=400, detail="Book not available or not found")

   
    if any(r for r in borrow_db if r["user_id"] == record.user_id and r["book_id"] == record.book_id and not r["return_date"]):
        raise HTTPException(status_code=400, detail="User already borrowed this book")

    
    borrow_db.append(record.dict())
    book["is_available"] = False
    return {"message": "Book borrowed successfully", "record": record}


@borrow_router.put("/return")
def return_book(user_id: int, book_id: int):
    for record in borrow_db:
        if record["user_id"] == user_id and record["book_id"] == book_id and not record["return_date"]:
            record["return_date"] = date.today()
            book = next((b for b in books_db if b["id"] == book_id), None)
            if book:
                book["is_available"] = True
            return {"message": "Book returned successfully"}
    raise HTTPException(status_code=404, detail="Borrow record not found")


@borrow_router.get("/", response_model=List[BorrowRecord])
def get_all_borrow_records():
    return borrow_db


@borrow_router.get("/user/{user_id}", response_model=List[BorrowRecord])
def get_user_borrow_records(user_id: int):
    user_records = [r for r in borrow_db if r["user_id"] == user_id]
    if not user_records:
        raise HTTPException(status_code=404, detail="No borrow records found for this user")
    return user_records
