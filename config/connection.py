import pymongo

def connect():
    client = pymongo.MongoClient("mongodb+srv://anmol111pal:PPap1310@banking-app-cluster.ywek7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

    db = client["Banking-app-cluster"]
    collection=db["bank-records"]
    return collection