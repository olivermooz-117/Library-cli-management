import hashlib
import uuid
from storage import load_users, save_users


# function decorators for access control. They wrap around functions to check if a user is logged in or if they have admin privileges before allowing the function to execute.
def require_login(func):
    """Decorator that blocks a function if no user is logged in."""
    def wrapper(current_user, *args, **kwargs):
        if current_user is None:
            print("[!] You must be logged in to do that.")
            return None
        return func(current_user, *args, **kwargs)
    return wrapper

# Admin-only decorator. It checks if the current user has an admin role before allowing access to certain functions. If the user is not an admin, it prints a warning message and prevents the function from executing.
def require_admin(func):
    """Decorator that blocks a function if the user is not an admin."""
    def wrapper(current_user, *args, **kwargs):
        if current_user is None or current_user.get("role") != "admin":
            print("[!] Admin access required.")
            return None
        return func(current_user, *args, **kwargs)
    return wrapper


# password hashing function. It takes a plaintext password and returns a hashed version using SHA-256. This is used to securely store passwords in the JSON file without exposing the actual password. 
def _hash_password(password: str) -> str:
    """Return a SHA-256 hash of the password."""
    return hashlib.sha256(password.encode()).hexdigest()


# auth functions for registering and logging in users. They interact with the JSON storage to save and verify user credentials.
def register(username: str, password: str, role: str = "user") -> bool:
    """
    Register a new user.
    role can be 'user' or 'admin'.
    Returns True on success, False if username already exists.
    """
    if not username or not password:
        print("[!] Username and password cannot be empty.")
        return False

    users = load_users()

    # Check for duplicate username
    for u in users:
        if u["username"].lower() == username.lower():
            print(f"[!] Username '{username}' is already taken.")
            return False

    new_user = {
        "id": str(uuid.uuid4()),
        "username": username,
        "password": _hash_password(password),
        "role": role,
    }

    users.append(new_user)
    save_users(users)
    print(f"[✓] User '{username}' registered successfully as {role}.")
    return True

# The login function checks the provided username and password against the stored user data. It loads all users from the JSON file, hashes the input password, and compares it to the stored hashed passwords. If a match is found, it returns the user dictionary; otherwise, it returns None and prints an error message.
def login(username: str, password: str):
    """
    Attempt to log in.
    Returns the user dict on success, None on failure.
    """
    users = load_users()
    hashed = _hash_password(password)

    for u in users:
        if u["username"].lower() == username.lower() and u["password"] == hashed:
            print(f"[✓] Welcome back, {u['username']}! (Role: {u['role']})")
            return u

    print("[!] Invalid username or password.")
    return None