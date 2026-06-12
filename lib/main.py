import argparse
from cli import run, show_books, login_menu, register_menu

parser = argparse.ArgumentParser(description="Library CLI System")
parser.add_argument("--login", action="store_true", help="Go straight to login")
parser.add_argument("--register", action="store_true", help="Go straight to register")
parser.add_argument("--books", action="store_true", help="View all books")

args = parser.parse_args()

if __name__ == "__main__":
    if args.login:
        login_menu()
    elif args.register:
        register_menu()
    elif args.books:
        show_books()
    else:
        run()