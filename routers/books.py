from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from database.db import users_db 

book_router = APIRouter()


class Book(BaseModel):
    id: int
    title: str
    author: str
    is_available: bool = True



@book_router.get("/", response_model=List[Book])
def get_books():
    return books_db


@book_router.get("/{book_id}", response_model=Book)
def get_book(book_id: int):
    book = next((b for b in books_db if b.id == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@book_router.post("/", response_model=Book)
def create_book(book: Book):
    if any(b.id == book.id for b in books_db):
        raise HTTPException(status_code=400, detail="Book ID already exists")
    books_db.append(book.dict())
    return book


@book_router.put("/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    for book in books_db:
        if book["id"] == book_id:
            book.update(updated_book.dict())
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# Delete Book
@book_router.delete("/{book_id}")
def delete_book(book_id: int):
    global books_db
    books_db = [book for book in books_db if book["id"] != book_id]
    return {"message": "Book deleted"}


@book_router.put("/{book_id}/unavailable")
def mark_book_unavailable(book_id: int):
    for book in books_db:
        if book["id"] == book_id:
            book["is_available"] = False
            return {"message": "Book marked as unavailable"}
    raise HTTPException(status_code=404, detail="Book not found")

 