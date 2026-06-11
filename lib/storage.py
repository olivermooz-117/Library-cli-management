import json
import os

DATA_DIR = os.path.join(os.path.dirname(_file_), "data")
USERS_FILE = os.path.join(DATA_DIR, "users.json")
BOOKS_FILE = os.path.join(DATA_DIR, "books.json")


def _ensure_data_dir():
    """Make sure the data folder exists."""
    os.makedirs(DATA_DIR, exist_ok=True)


def load_users():
    """Load all users from users.json. Returns a list."""
    _ensure_data_dir()
    if not os.path.exists(USERS_FILE):
        return []
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_users(users):
    """Save a list of user dicts to users.json."""
    _ensure_data_dir()
    try:
        with open(USERS_FILE, "w") as f:
            json.dump(users, f, indent=4)
        return True
    except IOError as e:
        print(f"[ERROR] Could not save users: {e}")
        return False


def load_books():
    """Load all books from books.json. Returns a list."""
    _ensure_data_dir()
    if not os.path.exists(BOOKS_FILE):
        return []
    try:
        with open(BOOKS_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_books(books):
    """Save a list of book dicts to books.json."""
    _ensure_data_dir()
    try:
        with open(BOOKS_FILE, "w") as f:
            json.dump(books, f, indent=4)
        return True
    except IOError as e:
        print(f"[ERROR] Could not save books: {e}")
        return False