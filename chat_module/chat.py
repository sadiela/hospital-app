import requests 
import json
from flask import Flask, abort, request, jsonify, Blueprint
#from helper import *
import pymongo
#import certifi
from database_module.mongo_database import mongodb_client
from marshmallow import Schema, fields, ValidationError

db = mongodb_client['healthDB']
chats = db['chats']

chat_blueprint = Blueprint('chat_blueprint', __name__)

class ChatSchema(Schema):
    chatid = fields.Int()#required=True)
    sessionid = fields.Int(required=True)
    sender = fields.Str(required=True)
    recipients = fields.List(fields.String, required=True)
    timestamp = fields.DateTime(required=True)
    text_message = fields.Str()
    voice_message = fields.Raw()
    image_message = fields.Raw()

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
        vals = coll.find({key:value}, projection={'_id': False})
    else: 
        vals = coll.find(projection={'_id': False})
    for x in vals:
        res.append(x)
    return res

@chat_blueprint.route('/add', methods=['GET', 'POST', 'PUT'])
def add_chat():
    print("ADDING CHAT")
    if request.is_json: # check data is in correct format
        chat_data = request.get_json() 
        try:
            chat_data = ChatSchema().load(chat_data)
        except ValidationError as err:
            print(err.messages)
            print(err.valid_data)
            print("INVALID CHAT DATA")
            return "Invalid data", 400
        id_vals = chats.distinct('chatid')
        new_id = insertion_index(id_vals)
        chat_data['chatid'] = new_id
        res = chats.insert_one(chat_data)
        print("CHAT ADDED")
        return str(res.acknowledged)
    print("INVALID REQUEST DATA")
    return "INVALID REQUEST DATA", 400

@chat_blueprint.route('/message/<chatid>', methods=['GET'])
def get_message(chatid):
    print("Getting message with ID: " + chatid)
    #db = client['healthDB']
    #chats = db['chats']
    message = custom_find(chats, 'chatid', int(chatid))
    if len(message)==0:
        print("NO MESSAGES FOUND")
        return "NO MESSAGE WITH ID {chatid} FOUND", 200
    return jsonify(message), 200

@chat_blueprint.route('/session/<sessionid>', methods=['GET'])
def get_session_messages(sessionid):
    print("Getting messages from session: " + sessionid)
    #db = client['healthDB']
    #chats = db['chats']
    messages = custom_find(chats, 'sessionid', int(sessionid))
    print("OBJECT NOW:", messages, len(messages))
    if len(messages)==0:
        print("NO MESSAGES FOUND")
        return "NO MESSAGES WITH SESSION ID {sessionid} FOUND", 200
    return jsonify(messages), 200

@chat_blueprint.route('/user/<userid>', methods=['GET'])
def get_user_messages(userid):
    print("Getting messages from user" + userid)
    #db = client['healthDB']
    #chats = db['chats']
    messages = custom_find(chats, 'sender', userid)
    if len(messages)==0:
        print("NO MESSAGES FOUND")
        return "NO MESSAGES WITH USER ID {userid} FOUND", 200
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
    if len(output)==0:
        print("NO MESSAGES FOUND")
        return "NO MESSAGES FOUND", 200
    return jsonify(output), 200

@chat_blueprint.route('/delete/<chatid>', methods=['GET', 'POST'])
def delete_message(chatid):
    print("Deleting message with id:" + chatid)
    #chats = mongodb_client.db.chats
    res = chats.delete_one({'chatid':int(chatid)})
    return "Deleted successfully:" +str(res.acknowledged), 200

@chat_blueprint.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource (chat) could not be found.</p>", 404

def abort_if_chat_doesnt_exist(id_type, resource_id):
    # findone fails
    chat = chats.find_one({id_type:resource_id})
    if not chat.acknowledge: # not in chats:
        abort(404, message="id {} in {} doesn't exist".format(resource_id, id_type))


if __name__ == '__main__':
    app1 = Flask(__name__)
    app1.register_blueprint(chat_blueprint, url_prefix='/chat')

    '''# DB SETUP
    '''''''''

    app1.run(debug=True)
