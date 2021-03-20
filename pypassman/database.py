import pickle

from cryptography import decrypt_file, encrypt_file

VERIFY_DATA = "@D87MJGP5W$a2DUs"


class Database:
    def __init__(self, password: str):
        self.password = password
        self.data = {
            "verify": VERIFY_DATA
        }
        try:
            db_data = pickle.loads(decrypt_file(password), encoding="utf-8")
            if db_data["verify"] != self.data["verify"]:
                print("The password is invalid!")
                exit(0)
        except:
            print("The password is invalid!")
            exit(0)

        self.data = db_data

    def store(self):
        encrypt_file(self.password, pickle.dumps(self.data))

    @staticmethod
    def create(password: str):
        data = {
            "verify": VERIFY_DATA
        }
        encrypt_file(password, pickle.dumps(data))
        return Database(password)
