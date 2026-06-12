# Library CLI Management System

A comprehensive command-line library management system built in Python that allows users to manage books, track borrowing, and persist data using JSON files. Perfect for learning Python OOP, file handling, and CLI development.

## Features

- User Authentication - Register and login with secure password hashing
- Role-Based Access - Regular users and administrators with different permissions
- Book Management - Add, view, borrow, and return books
- Persistent Storage - All data saved to JSON files automatically
- User Tracking - Track which user added each book
- Search Functionality- Find books by title or author
- Borrow History - View all books borrowed by a user
- Admin Controls - Delete books and view all borrowed books

  ## Data Persistence:
  - All data stored in JSON files
  - Automatic saving/loading of books and users
  - Error handling for file operations
##  Program used

- Language: Python 3.x
- Libraries: 
  - uuid - Unique ID generation
  - json - Data persistence
  - os/sys - System operations
## Project Structure
Library-cli-management/

├── lib/
│   ├── data/
│   │   ├── books.json
│   │   └── users.json
│   └── models/
│       ├── __init__.py
│       ├── book.py
│       └── user.py
        ├── auth.py
        ├── cli.py
        ├── main.py
├── readme.md
        ├── storage.py
├── Pipfile
├── Pipfile.lock
└── requirements.txt
