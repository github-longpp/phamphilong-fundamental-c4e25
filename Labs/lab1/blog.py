from pymongo import *
uri = "mongodb://admin:admin1@ds127988.mlab.com:27988/c4e25"

#1. Connect to mLab server
client = MongoClient(uri)

#2. Get a database
db = client.get_database()

#3. Get a collection
post_collection = db["posts"]

#4. Create a document
# post = {"title": "Days",  #field title
#         "content": "Hôm nay trời bão",  #field content
        
# }

#5. Insert document
# post_collection.insert_one(post)

# client.close()
post_list = post_collection.find()
first_post = post_list[0]
print(first_post)

for post in post_list:
    print(post)