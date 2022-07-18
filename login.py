import hashlib
from getpass import getpass

def login(collection):
    print("Login into your Account.")
    entered_username=input("Enter your username: ")
    entered_password=getpass("Enter your password: ")
    entered_password=hashlib.md5(entered_password.encode()).hexdigest()
    global matched_account
    matched_account=collection.find_one({
        "username": entered_username,
        "password": entered_password
    })

    if matched_account is not None:
        print("Successfully logged in as %s." %matched_account["name"])
        return matched_account
    else:
        print("Login Failed.")
        return None