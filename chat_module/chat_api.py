import requests 
import json
from flask import Flask, request, jsonify, Blueprint
#from helper import *
from flask_pymongo import PyMongo
from database_module.mongo_database import mongodb_client
from flask_restful import fields, marshal_with, reqparse, Resource


chat_blueprint = Blueprint('chat_blueprint', __name__)

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

def custom_find(coll, key, value):
    res = []
    if value is not None:
        for x in coll.find({key:value}):
            del x['_id']
            print(x)
            res.append(x)
    else:
        for x in coll.find():
            del x['_id']
            res.append(x)
    return res

#@marshal_with
@chat_blueprint.route('/', methods=['GET', 'POST'])
def add_chat():
    print("ADDING CHAT")
    if request.is_json: # check data is in correct format
        chat_data = request.get_json() 
    print("CHAT DATA:", chat_data)
    chats = mongodb_client.db.chats
    res = chats.insert_one(chat_data)
    return "Added a chat"

@chat_blueprint.route('/message/<chatid>', methods=['GET'])
def get_message(chatid):
    print("Getting message with ID: " + str(chatid))
    chats = mongodb_client.db.chats
    message = custom_find(chats, 'chatid', chatid)
    print("OBJECT NOW:", message)
    print("TYPE:", type(message))
    return json.dumps(message), 200

@chat_blueprint.route('/session/<sessionid>', methods=['GET'])
def get_session_messages(sessionid):
    print("Getting messages from session: " + str(sessionid))
    chats = mongodb_client.db.chats
    messages = custom_find(chats, 'sessionid', sessionid)
    print("OBJECT NOW:", messages)
    print("TYPE:", type(messages))
    return json.dumps(messages), 200

@chat_blueprint.route('/user/<userid>', methods=['GET'])
def get_user_messages(userid):
    print("Getting messages from user" + str(userid))
    chats = mongodb_client.db.chats
    messages = custom_find(chats, 'sender', userid)
    print("OBJECT NOW:", messages)
    print("TYPE:", type(messages))
    return json.dumps(messages), 200

@chat_blueprint.route('/delete/<chatid>', methods=['POST'])
def delete_message(chatid):
    print("Deleting message with id:" + str(chatid))
    chats = mongodb_client.db.chats
    res = chats.delete_one({'chatid', chatid})
    return json.dumps(res)

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

class Session(Resource):
    def get(self, sessionid):
        all_chats = []
        for chat in chats.find({'sessionid':sessionid}):
            del chat['_id']
            all_chats.append(chat)
        #del chat_obj['_id']
        print("OBJECT NOW:", all_chats)
        print("TYPE:", type(all_chats))
        return json.dumps(all_chats), 200

api.add_resource(HelloWorld, '/')
api.add_resource(Chat, '/chat/<int:chatid>', '/chat')
api.add_resource(Session, '/session/<int:sessionid>')

'''

if __name__ == '__main__':
    app1 = Flask(__name__)
    app1.register_blueprint(chat_blueprint, url_prefix='/chat')

    '''# DB SETUP
    '''''''''

    app1.run(debug=True)
