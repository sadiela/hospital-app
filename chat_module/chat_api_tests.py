from requests import put, get
import pymongo 
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
    'sender':'DrSmith', # use id from people database
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
#filepath = r'C:\Users\sadie\Documents\BU\spring_2022\ec530\hospital-app\cert\X509-cert-1835095331508356146.pem'
filepath = r'/Users/sadiela/Documents/courses_spring_2022/ec530/cert/X509-cert-1835095331508356146.pem'

uri  = r"mongodb+srv://cluster0.ipuos.mongodb.net/healthDB?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
mongodb_client = pymongo.MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile=filepath)

db = mongodb_client['healthDB']
chats_collection = db['chats']
doc_count = chats_collection.count_documents({})
print(doc_count)

## CLEAR DB BEFORE TESTING ##
x = chats_collection.delete_many({})
print(x.deleted_count, "documents deleted")

## PERFORM ADD TESTS (THREE VALID, TWO INVALID)
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
res1 = put('http://127.0.0.1:5000/chat/add', data=json.dumps(chat_object), headers=headers)#.json()
print(res1,res1.content.decode())
res2 = put('http://127.0.0.1:5000/chat/add', data=json.dumps(chat_object2), headers=headers)#.json()
print(res2,res2.content.decode())
res3 = put('http://127.0.0.1:5000/chat/add', data=json.dumps(chat_object3), headers=headers)#.json()
print(res3,res3.content.decode())
res4 = put('http://127.0.0.1:5000/chat/add', data=json.dumps(invalid_chat_object), headers=headers)#.json()
print(res4,res4.content.decode())
res5 = put('http://127.0.0.1:5000/chat/add', data=json.dumps(invalid_chat_object1), headers=headers)#.json()
print(res5,res5.content.decode())


print(chats_collection.distinct('chatid'))
print(chats_collection.distinct('text_message'))

## GET BY CHAT ID TESTS ##
res6 = get('http://127.0.0.1:5000/chat/message/0')
print(res6,res6.content.decode())
res7 = get('http://127.0.0.1:5000/chat/message/8')
print(res7,res7.content.decode())

## GET BY SESSION ID TESTS ##
res8 = get('http://127.0.0.1:5000/chat/session/1')
print(res8,res8.content.decode())
res9 = get('http://127.0.0.1:5000/chat/session/2')
print(res9,res9.content.decode())

## GET BY USER ID TESTS ##
res10 = get('http://127.0.0.1:5000/chat/user/JohnDoe')
print(res10,res10.content.decode())
res11 = get('http://127.0.0.1:5000/chat/user/DrSmith')
print(res11,res11.content.decode())

## GET ALL MESSAGES TESTS ##
res12 = get('http://127.0.0.1:5000/chat/messages')
print(res12,res12.content.decode())

## DELETE MESSAGES TESTS ##
res13 = get('http://127.0.0.1:5000/chat/delete/0')
print(res13,res13.content.decode())
res14 = get('http://127.0.0.1:5000/chat/delete/2')
print(res14,res14.content.decode())

print(chats_collection.distinct('chatid'))
print(chats_collection.distinct('text_message'))

## HAVEN'T TESTED IMAGE/VOICE DATA
