import requests 
import json
from flask import Flask, request, jsonify, Blueprint
#from helper import *
from flask_pymongo import PyMongo
from flask_restful import reqparse, abort, Api, Resource
from database_module.mongo_database import mongodb_client


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

@chat_blueprint.route('/newmessage', methods=['POST'])
def add_chat():
    return "Adding a chat"

@chat_blueprint.route('/message/<chatid>', methods=['GET'])
def get_message(chatid):
    print("Getting message with ID: " + str(chatid))
    chats = mongodb_client.db.chats
    print(type(chats))
    if chatid is not None:
        chat = chats.find_one({'chatid':chatid})
    else:
        chat = chats.find_one({'chatid':chatid})
    del chat['_id']
    print("OBJECT NOW:", chat)
    print("TYPE:", type(chat))
    return json.dumps(chat), 200

@chat_blueprint.route('/session/<sessionid>', methods=['GET'])
def get_session_messages(sessionid):
    return "Getting messages from session: " + str(sessionid)

@chat_blueprint.route('/user/<userid>', methods=['GET'])
def get_user_messages(userid):
    return "Getting messages from user" + str(userid)

@chat_blueprint.route('/delete/<messageid>', methods=['POST'])
def delete_message(messageid):
    return "Deleting message with id:" + str(messageid)

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
