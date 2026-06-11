import hashlib
import uuid
from storage import load_users, save_users


# ──────────────────────────────────────────────
# Decorator: require login
# ──────────────────────────────────────────────
def require_login(func):
    """Decorator that blocks a function if no user is logged in."""
    def wrapper(current_user, *args, **kwargs):
        if current_user is None:
            print("[!] You must be logged in to do that.")
            return None
        return func(current_user, *args, **kwargs)
    return wrapper


def require_admin(func):
    """Decorator that blocks a function if the user is not an admin."""
    def wrapper(current_user, *args, **kwargs):
        if current_user is None or current_user.get("role") != "admin":
            print("[!] Admin access required.")
            return None
        return func(current_user, *args, **kwargs)
    return wrapper


# ──────────────────────────────────────────────
# Password hashing
# ──────────────────────────────────────────────
def _hash_password(password: str) -> str:
    """Return a SHA-256 hash of the password."""
    return hashlib.sha256(password.encode()).hexdigest()


# ──────────────────────────────────────────────
# Auth functions
# ──────────────────────────────────────────────
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