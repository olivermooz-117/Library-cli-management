import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import auth
from models.book import get_all_books, save_all_books, find_book_by_id, add_book, delete_book


def clear():
    os.system("clear")


def pause():
    input("\nPress Enter to continue...")


def register_menu():
    print("\n--- REGISTER ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    role = input("Role (user/admin): ")
    if role != "admin":
        role = "user"
    auth.register(username, password, role)
    pause()


def login_menu():
    print("\n--- LOGIN ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = auth.login(username, password)
    pause()
    return user


def show_books():
    print("\n--- ALL BOOKS ---")
    books = get_all_books()
    if not books:
        print("No books found.")
    for book in books:
        book.display()
    pause()


def borrow_menu(current_user):
    print("\n--- BORROW A BOOK ---")
    show_books()
    book_id = input("Enter Book ID (first 8 chars): ")
    book, books = find_book_by_id(book_id)
    if not book:
        print("Book not found.")
    else:
        if book.borrow(current_user["username"]):
            save_all_books(books)
    pause()


def return_menu(current_user):
    print("\n--- RETURN A BOOK ---")
    books = get_all_books()
    my_books = [b for b in books if b._borrowed_by == current_user["username"]]
    if not my_books:
        print("You have no borrowed books.")
        pause()
        return
    for b in my_books:
        b.display()
    book_id = input("\nEnter Book ID to return: ")
    book, books = find_book_by_id(book_id)
    if not book:
        print("Book not found.")
    elif book._borrowed_by != current_user["username"]:
        print("You did not borrow that book.")
    else:
        book.return_book()
        save_all_books(books)
    pause()


def add_book_menu(current_user):
    if current_user["role"] != "admin":
        print("Admins only.")
        return
    print("\n--- ADD A BOOK ---")
    title = input("Title: ")
    author = input("Author: ")
    genre = input("Genre: ")
    add_book(title, author, genre)
    pause()


def delete_book_menu(current_user):
    if current_user["role"] != "admin":
        print("Admins only.")
        return
    print("\n--- DELETE A BOOK ---")
    show_books()
    book_id = input("Enter Book ID to delete: ")
    from models.book import delete_book
    delete_book(book_id)
    pause()


def view_borrowed_menu(current_user):
    if current_user["role"] != "admin":
        print("Admins only.")
        return
    print("\n--- BORROWED BOOKS ---")
    books = get_all_books()
    borrowed = [b for b in books if b.is_borrowed]
    if not borrowed:
        print("No books are currently borrowed.")
    for b in borrowed:
        b.display()
    pause()


def run():
    current_user = None

    while True:
        clear()

        if current_user is None:
            print("\n==== LIBRARY SYSTEM ====")
            print("1. Login")
            print("2. Register")
            print("3. View Books")
            print("0. Exit")
            choice = input("\nChoose: ")

            if choice == "1":
                current_user = login_menu()
            elif choice == "2":
                register_menu()
            elif choice == "3":
                show_books()
            elif choice == "0":
                print("Goodbye!")
                sys.exit(0)
            else:
                print("Invalid option.")
                pause()

        else:
            is_admin = current_user["role"] == "admin"
            print(f"\n==== LIBRARY SYSTEM ====")
            print(f"Logged in as: {current_user['username']} ({current_user['role']})")
            print("1. View all books")
            print("2. Borrow a book")
            print("3. Return a book")
            if is_admin:
                print("4. Add a book")
                print("5. Delete a book")
                print("6. View all borrowed")
            print("0. Logout")
            choice = input("\nChoose: ")

            if choice == "1":
                show_books()
            elif choice == "2":
                borrow_menu(current_user)
            elif choice == "3":
                return_menu(current_user)
            elif choice == "4" and is_admin:
                add_book_menu(current_user)
            elif choice == "5" and is_admin:
                delete_book_menu(current_user)
            elif choice == "6" and is_admin:
                view_borrowed_menu(current_user)
            elif choice == "0":
                print(f"Logged out. Bye {current_user['username']}!")
                current_user = None
                pause()
            else:
                print("Invalid option.")
                pause()