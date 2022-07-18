def withdraw(collection, matched_account, amount):

    if amount==0.0:
        return

    if matched_account["balance"]-amount>0:
        prev={
            "balance": matched_account["balance"]
        }

        newValue={
            "$set":{"balance": matched_account["balance"]-amount}
        }

        collection.update_one(prev, newValue)

        print("Amount withdrawn.")
        new_balance=collection.find_one({
            "username": matched_account["username"],
            "password": matched_account["password"]
        })["balance"]

        print("\nCurrent Balance: %.2f\n" %new_balance)
    else:
        print("\nCurrent Balance: %.2f\n" %matched_account["balance"])
        print("Not enough amount in account.")