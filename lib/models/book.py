import uuid
from storage import load_books, save_books


class Book:
    def __init__(self, title: str, author: str, genre: str, book_id: str = None):
        self._id = book_id or str(uuid.uuid4())
        self._title = title
        self._author = author
        self._genre = genre
        self._is_borrowed = False
        self._borrowed_by = None   # stores username of borrower

    # ── Properties ───────────────────────────
    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def is_borrowed(self):
        return self._is_borrowed

    # ── Borrow / Return ───────────────────────
    def borrow(self, username: str) -> bool:
        if self._is_borrowed:
            print(f"[!] '{self._title}' is already borrowed by {self._borrowed_by}.")
            return False
        self._is_borrowed = True
        self._borrowed_by = username
        print(f"[✓] '{self._title}' borrowed by {username}.")
        return True

    def return_book(self) -> bool:
        if not self._is_borrowed:
            print(f"[!] '{self._title}' is not currently borrowed.")
            return False
        borrower = self._borrowed_by
        self._is_borrowed = False
        self._borrowed_by = None
        print(f"[✓] '{self._title}' returned (was borrowed by {borrower}).")
        return True

    # ── Serialisation (to/from dict for JSON) ─
    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "title": self._title,
            "author": self._author,
            "genre": self._genre,
            "is_borrowed": self._is_borrowed,
            "borrowed_by": self._borrowed_by,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Book":
        book = cls(
            title=data["title"],
            author=data["author"],
            genre=data["genre"],
            book_id=data["id"],
        )
        book._is_borrowed = data.get("is_borrowed", False)
        book._borrowed_by = data.get("borrowed_by", None)
        return book

    def display(self):
        status = f"Borrowed by {self._borrowed_by}" if self._is_borrowed else "Available"
        print(f"  [{self._id[:8]}] {self._title} — {self._author} ({self._genre}) | {status}")

    def __repr__(self):
        return f"Book(title={self._title}, author={self._author})"


# ── Library-level book functions (used by CLI) ─────────────────────────────

def get_all_books() -> list:
    """Return all books as Book objects."""
    return [Book.from_dict(b) for b in load_books()]


def save_all_books(books: list):
    """Save a list of Book objects to JSON."""
    save_books([b.to_dict() for b in books])


def find_book_by_id(book_id: str):
    """Return a Book object by its ID prefix (first 8 chars OK), or None."""
    books = get_all_books()
    for book in books:
        if book.id.startswith(book_id):
            return book, books
    return None, books


def add_book(title: str, author: str, genre: str) -> bool:
    """Add a new book and persist."""
    books = get_all_books()
    new_book = Book(title, author, genre)
    books.append(new_book)
    save_all_books(books)
    print(f"[✓] Book '{title}' added (ID: {new_book.id[:8]}).")
    return True


def delete_book(book_id: str) -> bool:
    """Delete a book by ID prefix."""
    book, books = find_book_by_id(book_id)
    if not book:
        print(f"[!] Book with ID '{book_id}' not found.")
        return False
    if book.is_borrowed:
        print(f"[!] Cannot delete '{book.title}' — it is currently borrowed.")
        return False
    books = [b for b in books if not b.id.startswith(book_id)]
    save_all_books(books)
    print(f"[✓] Book '{book.title}' deleted.")
    return True