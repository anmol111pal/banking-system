def show_stats(collection, matched_account):
    
    if matched_account["name"]!="admin" and matched_account["username"]!="admin":
        return
    print("\nBank Stats:\n")
    
    total_account_holders=0
    total_balance_amount=0.0
    
    all_docs=collection.find({}) # will get all docs
    
    for doc in all_docs:
        if doc["name"]!="admin" and doc["username"]!="admin":
            total_account_holders+=1
            total_balance_amount+=doc["balance"]
    
    print("Total Account Holders: %d" %total_account_holders)
    print("Total Balance Amount: %.2f\n" %total_balance_amount)