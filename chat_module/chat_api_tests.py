from requests import put, get
import json

chat_object = {
    'chatid': 0,
    'sessionid': 1,
    'sender':'John Doe', # use id from people database
    'recipients':['Dr. Smith'], # probably use ids for this
    'timestamp':'2020-03-27T19:46:21',
    'message_type': 'text',
    'message':'Hello!'
}

chat_object2 = {
    'chatid': 1,
    'sessionid': 1,
    'sender':'John Doe', # use id from people database
    'recipients':['Dr. Smith'], # probably use ids for this
    'timestamp':'2020-03-27T19:48:00',
    'message_type': 'text',
    'message':'How are you doing?'
}

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
res1 = put('http://127.0.0.1:5000/chat', data=json.dumps(chat_object), headers=headers)#.json()
print(res1)
res2 = put('http://127.0.0.1:5000/chat', data=json.dumps(chat_object2), headers=headers)#.json()


print(get('http://127.0.0.1:5000/chat/session/1'))#.json()
