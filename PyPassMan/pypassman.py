#!/bin/python
from getpass import getpass

from PyPassMan.database import Database
from PyPassMan.utils import create_file, check_file_exists


def main():
    if not check_file_exists():
        print("A new database needs to be created.")
        while True:
            password = getpass("Please enter your master password: ")
            verify = getpass("Please verify your master password: ")
            if password == verify:
                break
            print("\nERROR: The passwords do not match\n")
        create_file()
        db = Database.create(password)
    else:
        password = getpass("Password: ")
        db = Database(password)
