# LIBRARY
A FastAPI-based library management system that allows users to perform CRUD operations for users, books, and borrow records. The system includes features like borrowing and returning books while adhering to user and book constraints.

## Features

User Endpoints

Create, read, update, and delete user accounts.

Deactivate a user by setting is_active to False.

Book Endpoints

Create, read, update, and delete books.

Mark a book as unavailable (e.g., lost or under maintenance).

Borrow Operations

Borrow a book:

Allows an active user to borrow an available book.

Ensures a user cannot borrow the same book more than once.

Updates the book’s is_available status to False if successfully borrowed.

Return a book:

Marks a borrowed book as returned by updating the return_date in the BorrowRecord.

Sets the book’s is_available status back to True.

Borrow Record Management

View borrowing records for a specific user.

View all borrowing records.

## instalation
1. clone the repository
git clone https://github.com/MoniyaTee/ALTSCHOOL-SECOND-SEMESTER-EXAM.git
2. Navigate to the project directory:
cd ALTSCHOOL-SECOND-SEMESTER-EXAM

3. Create and activate a virtual environment
Windows:
python -m venv venv
.\venv\Scripts\activate
macOS/Linux:
python3 -m venv venv
source venv/bin/activate


## Usage

## Endpoints

Access the interactive API documentation at:

Swagger UI: http://127.0.0.1:8000/docs
