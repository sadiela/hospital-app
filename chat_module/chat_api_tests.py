from requests import put, get
import pymongo 
import certifi
import json


### TEST CASES ###
# - insert valid chat data
# - insert invalid chat data
#   - missing a required field
#   - has all required fields but value is the wrong type
# - get message by chatid
#   - for chat that exists
#   - for chat not present in DB
# - get message(s) by sessionid
#   - for session that exists
#   - for session not present in DB
# - get message(s) by userid
#   - for user that exists
#   - for user not present in DB
# - get all messages
# - delete a chat by id

# VALID
chat_object = {
    'chatid': 0,
    'sessionid': 1,
    'sender':'JohnDoe', # use id from people database
    'recipients':['DrSmith'], # probably use ids for this
    'timestamp':'2020-03-27T19:46:21',
    'text_message':'Hello!'
}

# VALID
chat_object2 = {
    'chatid': 1,
    'sessionid': 1,
    'sender':'JohnDoe', # use id from people database
    'recipients':['DrSmith'], # probably use ids for this
    'timestamp':'2020-03-27T19:48:00',
    'text_message': 'How are you doing?',
}

# VALID
chat_object3 = {
    'chatid': 2,
    'sessionid': 1,
    'sender':'Dr. Smith', # use id from people database
    'recipients':['JohnDoe'], # probably use ids for this
    'timestamp':'2020-03-27T19:48:00',
    'text_message': 'I am well. Thank you for asking!',
}

# MISSING REQUIRED SENDER FIELD
invalid_chat_object = {
    'chatid': 3,
    'sessionid': 1,
    'recipients':['DrSmith'], # probably use ids for this
    'timestamp':'2020-03-27T19:46:21',
    'text_message':'Hello!'
}

# WRONG TYPE FOR SENDER FIELD
invalid_chat_object1 = {
    'chatid': 4,
    'sessionid': 1,
    'sender':5, # use id from people database
    'recipients':['DrSmith'], # probably use ids for this
    'timestamp':'2020-03-27T19:46:21',
    'text_message':'Hello!'
}

## CONNECT TO DB ##
#uri = "mongodb+srv://cluster0.ipuos.mongodb.net/healthDB?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
client = pymongo.MongoClient("mongodb+srv://sadiela:xs5MaYfQUs8M9E5O@cluster0.ipuos.mongodb.net/healthDB?retryWrites=true&w=majority")

db = client['healthDB']
chats_collection = db['chats']
doc_count = chats_collection.count_documents({})
print(doc_count)

## CLEAR DB BEFORE TESTING ##
x = chats_collection.delete_many({})
print(x.deleted_count, "documents deleted")

## PERFORM ADD TESTS (THREE VALID, TWO INVALID)
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
res1 = put('http://127.0.0.1:5000/chat/add', data=json.dumps(chat_object), headers=headers)#.json()
res2 = put('http://127.0.0.1:5000/chat/add', data=json.dumps(chat_object2), headers=headers)#.json()
res3 = put('http://127.0.0.1:5000/chat/add', data=json.dumps(chat_object3), headers=headers)#.json()
res4 = put('http://127.0.0.1:5000/chat/add', data=json.dumps(invalid_chat_object), headers=headers)#.json()
res5 = put('http://127.0.0.1:5000/chat/add', data=json.dumps(invalid_chat_object1), headers=headers)#.json()

print(chats_collection.distinct('chatid'))
print(chats_collection.distinct('text_message'))

## GET BY CHAT ID TESTS ##
print(get('http://127.0.0.1:5000/chat/message/0'))
print(get('http://127.0.0.1:5000/chat/message/8'))

## GET BY SESSION ID TESTS ##
print(get('http://127.0.0.1:5000/chat/session/1'))
print(get('http://127.0.0.1:5000/chat/session/2'))

## GET BY USER ID TESTS ##
print(get('http://127.0.0.1:5000/chat/user/JohnDoe'))
print(get('http://127.0.0.1:5000/chat/user/DrSmith'))

## GET ALL MESSAGES TESTS ##
print(get('http://127.0.0.1:5000/chat/messages'))

## DELETE MESSAGES TESTS ##
print(get('http://127.0.0.1:5000/chat/delete/0'))
print(get('http://127.0.0.1:5000/chat/delete/2'))


print(chats_collection.distinct('chatid'))
print(chats_collection.distinct('text_message'))

