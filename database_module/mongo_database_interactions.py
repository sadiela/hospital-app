from pymongo import MongoClient
import gridfs

#db = MongoClient().gridfs_example

# Connect to MongoDB
client = MongoClient(port=27017)

# create gridfs instancex
#fs = gridfs.GridFS(db)

# Create database
db = client.healthdb
chatcol = db.chat
db.chat.drop()

print(db.list_collection_names())

# insert chat objects as dictionaries:
textchat1 = {
    'chatid': 1,
    'sessionid': 1,
    'sender':'John Doe', # use id from people database
    'recipients':['Dr. Smith'], # probably use ids for this
    'timestamp':'2020-03-27T19:46:21',
    'message_type': 'text',
    'message':'Hello!'
}

# Load image from memory

imagechat1 = {
    'chatid': 1,
    'sessionid': 1,
    'sender':'John Doe', # use id from people database
    'recipients':['Dr. Smith'], # probably use ids for this
    'timestamp':'2020-03-27T19:46:21',
    'message_type': 'image',
    'message':'Hello!'
}

result = db.chat.insert_one(textchat1)

print(result.acknowledged, result.inserted_id)

chatInstance = db.chat.find_one({'chatid':1})

print(chatInstance)

print("ALL DOCUMENTS")
cursor = db.chat.find({})
for document in cursor:
    print(document)
