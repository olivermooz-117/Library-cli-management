# this is the parent class, it represents a normal user of the library system.
class User:
    """
    Base class representing a regular library user.
    Encapsulates user data and borrow-related behaviour.
    """
#__init__()runs automatically whenever a user object is created
    def __init__(self, user_id: str, username: str, role: str = "user"):
        self._id = user_id          # encapsulated with _
        self._username = username
        self._role = role

    #Properties (getters) 
    #they allow safe access to private attributes.
    @property
    def id(self):
        return self._id

    @property
    def username(self):
        return self._username

    @property
    def role(self):
        return self._role

    # Display 
    #prints formatted user information.

    def display_info(self):
        print(f"  ID       : {self._id}")
        print(f"  Username : {self._username}")
        print(f"  Role     : {self._role}")

    def __repr__(self):
    #__repr__ controls how the object appears when printed.
        return f"User(username={self._username}, role={self._role})"


class Admin(User):
    """
    Admin user — inherits from User, adds admin-only actions.
    Demonstrates inheritance.
    """
#constructor  method creates an admin object.
    def __init__(self, user_id: str, username: str):
        super().__init__(user_id, username, role="admin")
#method overriding-this replaces the parents display_info()with a customized version.
    def display_info(self):
        """Overrides parent to show admin badge."""
        super().display_info()
        print("  Access   : ADMIN (full privileges)")

    def __repr__(self):
        return f"Admin(username={self._username})"