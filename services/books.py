from schemas.books import Book, BookBase, BookCreate, BookUpdate
from database.db import users_db, books_db
from datetime import date


class BookServices:

    @staticmethod
    def get_books():
        return books_db
    

    @staticmethod
    def get_books(id):
        user = book_services.get_users()
        for u in user: 
            if u["id"] == id:
                main_book = u 
                break
        return main_book                

    @staticmethod
    def create_book(book: BookCreate):
        new_book = Book(id=len(book_services.get_books()) + 1, **book.model_dump())
        book.append(new_book)
        return new_book
    
    @staticmethod
    def update_book(book: Book, data: BookCreate):
        book.name = data.name
        book.email = data.mail
        return book
    
    @staticmethod
    def part_update_book(book: Book, data: BookUpdate):
        update_data = data.model_dump(exclude_unset=True).items()
        for key, value in update_data:
            setattr(book, key, value)
            return book
        
    @staticmethod
    def delete_book(id):
        book = book_services.get_book(id)
        book.remove(book)
        return {"message":  "book deleted!"}


















book_services = BookServices()