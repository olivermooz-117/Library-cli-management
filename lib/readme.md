# 📚 Library CLI Management System

A comprehensive command-line library management system built in Python that allows users to manage books, track borrowing, and persist data using JSON files. Perfect for learning Python OOP, file handling, and CLI development.

## Features

- **User Authentication** - Register and login with secure password hashing
- **Role-Based Access** - Regular users and administrators with different permissions
- **Book Management** - Add, view, borrow, and return books
- **Persistent Storage** - All data saved to JSON files automatically
- **User Tracking** - Track which user added each book
- **Search Functionality** - Find books by title or author
- **Borrow History** - View all books borrowed by a user
- **Admin Controls** - Delete books and view all borrowed books

##  Project Structure
ibrary-cli-management/
├── main.py # Entry point - run this file
├── cli.py # Command-line interface logic
├── auth.py # User authentication (login/register)
├── storage.py # JSON file handling
├── models/
│ ├── book.py # Book class and operations
│ └── user.py # User class (optional)
├── data/
│ ├── books.json # All books stored here
│ └── users.json # All users stored here