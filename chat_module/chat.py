from xml.dom import ValidationErr
import requests 
import json
from flask import Flask, request, jsonify, Blueprint
#from helper import *
import pymongo
#import certifi
from database_module.mongo_database import mongodb_client
from marshmallow import Schema, fields

'''uri = "mongodb+srv://cluster0.ipuos.mongodb.net/healthDB?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
client = pymongo.MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile='/Users/sadiela/Documents/courses_spring_2022/ec530/cert/X509-cert-1835095331508356146.pem')
'''
db = mongodb_client['healthDB']
chats = db['chats']
chats.create_index([("chatid", pymongo.ASCENDING)], unique=True)


chat_blueprint = Blueprint('chat_blueprint', __name__)

class ChatSchema(Schema):
    chatid = fields.Int(required=True)
    sessionid = fields.Int(required=True)
    sender = fields.Str(required=True)
    recipients = fields.List(fields.String, required=True)
    timestamp = fields.DateTime(required=True)
    text_message = fields.Str()
    voice_message = fields.Raw()
    video_message = fields.Raw()

#db = mongodb_client.db
#print(type(db))
#db.chat.drop()
#chats = db.chat # chat collection in database

# Need to be able to:
#   - add a new chat to the DB (one at a time only )
#   - get chat by ID
#   - get chat by session
#   - get chats by user
#   - delete chat

def insertion_index(nums):
    n = 0
    s = set(nums)
    while n in s:
        n += 1
    return n

def custom_find(coll, key, value):
    res = []
    if value is not None:
        vals = coll.find({key:value})
    else: 
        vals = coll.find()
    for x in vals:
        del x['_id']
        print(x)
        res.append(x)
    return res

@chat_blueprint.route('/add', methods=['GET', 'POST', 'PUT'])
def add_chat():
    print("ADDING CHAT")
    if request.is_json: # check data is in correct format
        chat_data = request.get_json() 
        try:
            chat_data = ChatSchema().load(chat_data)
        except ValidationErr as err:
            print(err.messages)
            print(err.valid_data)
        print("CHAT DATA TYPE:", type(chat_data))
        print("CHAT DATA:", chat_data)
        id_vals = chats.distinct('chatid')
        new_id = insertion_index(id_vals)
        chat_data['chatid'] = new_id
        res = chats.insert_one(chat_data)
        print("CHAT ADDED")
        return str(res)
    return "Invalid data", 400

@chat_blueprint.route('/message/<chatid>', methods=['GET'])
def get_message(chatid):
    print("Getting message with ID: " + chatid)
    #db = client['healthDB']
    #chats = db['chats']
    message = custom_find(chats, 'chatid', int(chatid))
    print("OBJECT NOW:", message)
    print("TYPE:", type(message))
    return jsonify(message), 200

@chat_blueprint.route('/session/<sessionid>', methods=['GET'])
def get_session_messages(sessionid):
    print("Getting messages from session: " + sessionid)
    #db = client['healthDB']
    #chats = db['chats']
    messages = custom_find(chats, 'sessionid', int(sessionid))
    print("OBJECT NOW:", messages)
    return jsonify(messages), 200

@chat_blueprint.route('/user/<userid>', methods=['GET'])
def get_user_messages(userid):
    print("Getting messages from user" + userid)
    #db = client['healthDB']
    #chats = db['chats']
    messages = custom_find(chats, 'sender', userid)
    print("OBJECT NOW:", messages)
    print("TYPE:", type(messages))
    return jsonify(messages), 200

@chat_blueprint.route('/messages', methods=['GET'])
def get_all_messages():
    print("Getting messages")
    output = []
    messages = chats.find()
    for i, x in enumerate(messages):
        print(i, x)
        del x['_id']
        output.append(x)
    return jsonify(output), 200

@chat_blueprint.route('/delete/<chatid>', methods=['GET', 'POST'])
def delete_message(chatid):
    print("Deleting message with id:" + chatid)
    #chats = mongodb_client.db.chats
    res = chats.delete_one({'chatid':int(chatid)})
    return str(res.acknowledged), 200

@chat_blueprint.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource (chat) could not be found.</p>", 404

'''
def abort_if_chat_doesnt_exist(id_type, resource_id):
    # findone fails
    chat = chats.find_one({id_type:resource_id})
    if not chat.acknowledge: # not in chats:
        abort(404, message="id {} in {} doesn't exist".format(resource_id, id_type))

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Chat(Resource):
    def get(self, chatid=None):
        if chatid is not None:
            chat = chats.find_one({'chatid':chatid})
        else:
            chat = chats.find_one({'chatid':chatid})
        del chat['_id']
        print("OBJECT NOW:", chat)
        print("TYPE:", type(chat))
        return json.dumps(chat), 200
    def put(self):
        data = request.get_json()
        print('DATA:', data)
        print("TYPE:", type(data))
        result = chats.insert_one(data)
        return {'result':result.acknowledged}, 200

'''

if __name__ == '__main__':
    app1 = Flask(__name__)
    app1.register_blueprint(chat_blueprint, url_prefix='/chat')

    '''# DB SETUP
    '''''''''

    app1.run(debug=True)
