import os

password_file = os.getenv("HOME") + "/.local/share/PyPassMan/db"


def create_file():
    os.makedirs(os.path.dirname(password_file), exist_ok=True)
    with open(password_file, "w") as f:
        f.write("")


def check_file_exists():
    return os.path.isfile(password_file)


def remove_file():
    os.remove(password_file)
