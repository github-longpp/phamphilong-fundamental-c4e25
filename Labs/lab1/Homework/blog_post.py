from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
db = client.get_database()
posts = db["PPLong"]

new_post = {
    "Name": "Phạm Phi Long",
    "Class": "C4E25",
    "content": '''
        I love C4E25
    ''',
}

posts.insert_one(new_post)
client.close()