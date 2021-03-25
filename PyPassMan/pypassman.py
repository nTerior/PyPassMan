from argparse import ArgumentParser
from getpass import getpass

from prettytable.prettytable import PrettyTable

from PyPassMan.database import Database
from PyPassMan.utils import create_file, check_file_exists, remove_file


def parse_args():
    parser = ArgumentParser(description="Store your passwords in an encrypted way")
    parser.add_argument(
        "option", choices=["add", "remove", "rm", "set", "show", "reset"],
        help="The option what you want to do:"
             "\"add\" adds a new account."
             "\"remove\", \"rm\" removes an account."
             "\"set\" updated an account"
             "\"show\" lists all passwords"
             "\"reset\" resets the password manager"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    if not check_file_exists():
        print("Thanks for using PyPassMan. Please enter your master password. "
              "Make sure to store it safely, you will need it to use this password manager")
        while True:
            password = getpass("Please enter your new master password: ")
            verify = getpass("Please verify your new master password: ")
            if password == verify:
                break
            print("\nERROR: The passwords do not match")
        create_file()
        db = Database.create(password)
    else:
        password = getpass("Master Password: ")
        db = Database(password)

    option = args.option
    executable = Executable()
    getattr(Executable, option)(executable, db)


class Executable:
    def add(self, db: Database):
        db.add_account(input("Account name: "), getpass("Password: "))
        db.store()

    def remove(self, db: Database):
        db.remove_account(input("Account name: "))
        db.store()

    def rm(self, db: Database):
        self.remove(db)

    def set(self, db: Database):
        name = input("Account name: ")
        db.remove_account(name)
        db.add_account(name, getpass("Password: "))
        db.store()

    def reset(self, db: Database):
        if input(
                "Do you really want to reset reset?\nAll passwords and additional data will be lost. [y/N] "
        ).lower() != "y":
            exit(0)

        remove_file()
        print("The password manager has been fully reset")

    def show(self, db: Database):
        table = PrettyTable()
        table.field_names = ["Account", "Password"]

        for key in db.data.keys():
            if key == "verify":
                continue
            table.add_row([key, db.data[key]["password"]])

        print(table if len(list(filter(lambda x: x != "verify", db.data.keys()))) != 0 else "Empty database")
