from getpass import getpass
import hashlib
from validate_username import validate

def update_info(collection, matched_account):
    prev_data={}
    updated_data={}
    field=input("Which field would you like to update: ").lower()

    if field=="password":
        new_password=getpass("Enter new Password: ")
        new_password=hashlib.md5(new_password.encode()).hexdigest()
        prev_data={
            "password": matched_account["password"]
        }
        updated_data={
            "$set": {
                "password": new_password # hashed password
            }
        }


    elif field=="name":
        new_name=input("Enter new name: ")

        prev_data={
            "name": matched_account["name"]
        }
        updated_data={
            "$set": {
                "name": new_name
            }
        }

    elif field in ["number", "phone", "mobile", "mob", "phn"]:
        new_mob_no=input("Enter new Mobile Number: ")

        prev_data={
            "mob_no": matched_account["mob_no"]
        }
        updated_data={
            "$set": {
                "mob_no": new_mob_no
            }
        }

    elif field=="email":
        new_email=input("Enter new Email address: ")

        prev_data={
            "email": matched_account["email"]
        }
        updated_data={
            "$set": {
                "email": new_email
            }
        }

    elif field=="username":
        new_username=input("Enter new username: ")
        prev_data={
            "username": matched_account["username"]
        }
        updated_data={
            "$set": {
                "username": new_username
            }
        }

    print("Processing your request...")
    collection.update_one(prev_data, updated_data)
    print("Changes updated.\n")