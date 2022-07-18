from getpass import getpass
import hashlib

def create_account(collection):
    print("\nAccount Creation.\n")
    name=input("Enter name: ")
    username=input("Choose a username: ")
    password=getpass("Choose a password: ")
    password=hashlib.md5(password.encode()).hexdigest()
    mob_no=input("Enter phone number: ")
    email=input("Enter email: ")

    account={
        "name": name,
        "mob_no": mob_no,
        "email": email,
        "balance": 0.0,
        "username": username,
        "password": password # hashed password
    }

    print("Creating Account...")

    # send it to the db
    collection.insert_one(account)
    print("Account Created successfully.")