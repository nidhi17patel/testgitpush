import pymongo
client = pymongo.MongoClient("mongodb+srv://Nidhi:1234@cluster0.whtng.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "Nidhi",
    "Email" : "nidhi17patel@gmail.com",
    "surname" : "Patel"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

print("Happy")