import pymongo

client = pymongo.MongoClient("mongodb+srv://ineuron:#Paddy123@cluster0.bcaa7ro.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {"Name":"Padmaranjan",
     "EmailID":"padmaranjansaha@gmail.com",
     "Surname":"Saha",
     "Name1":"Padmaranjan1",
     "EmailID1":"padmaranjansaha1@gmail.com",
     "Surname1":"Saha1"
    }

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
