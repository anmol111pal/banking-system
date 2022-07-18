def delete_account(collection, matched_account):
    confirm=input("Are you sure you want to Delete your Account ? (Y/n): ").lower()

    if confirm.startswith("y"):
        print("Deleting Account...")
        collection.delete_one({
            "username": matched_account["username"],
            "password": matched_account["password"],
            "name": matched_account["name"]
        })
        print("Account deleted successfully.\n")