
class User:#this is the parent class
    """
    Base class representing a regular library user.
    Encapsulates user data and borrow-related behaviour.
    """

    def __init__(self, user_id: str, username: str, role: str = "user"):#init runs automatically whenever a user object is created
        self._id = user_id          # encapsulated with _
        self._username = username
        self._role = role

    # ── Properties (getters) ──────────────────
    @property#they allow access to private attributes without exposing them directly, maintaining encapsulation.
    def id(self):
        return self._id

    @property
    def username(self):
        return self._username

    @property
    def role(self):
        return self._role

    # ── Display ───────────────────────────────
    def display_info(self):#prints formatted user information
        print(f"  ID       : {self._id}")
        print(f"  Username : {self._username}")
        print(f"  Role     : {self._role}")

    def __repr__(self):#controls how the object appears when printed
        return f"User(username={self._username}, role={self._role})"


class Admin(User):
    """
    Admin user — inherits from User, adds admin-only actions.
    Demonstrates inheritance.
    """
#constructor method creates an admin object.
    def __init__(self, user_id: str, username: str):
        super().__init__(user_id, username, role="admin")

    def display_info(self):
        """Overrides parent to show admin badge."""
        super().display_info()
        print("  Access   : ADMIN (full privileges)")

    def __repr__(self):
        return f"Admin(username={self._username})"