import requests 
import json
from flask import Flask, request, jsonify
#from helper import *
from flask_pymongo import PyMongo
from flask_restful import reqparse, abort, Api, Resource


app = Flask(__name__)
api = Api(app)

mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/health_db")
db = mongodb_client.db
db.chat.drop()

chats = db.chat # chat collection in database

def abort_if_chat_doesnt_exist(id_type, resource_id):
    # findone fails
    if resource_id not in chats:
        abort(404, message="Todo {} doesn't exist".format(resource_id))

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Chat(Resource):
    def get(self, chatid):
        chat = chats.find_one({'chatid':chatid})
        print("OBJECT", chat)
        del chat['_id']
        print("OBJECT NOW:", chat)
        print("TYPE:", type(chat))
        return json.dumps(chat), 200
    def put(self, chatid):
        data = request.get_json()
        print("IN PUT METHOD")
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
api.add_resource(Chat, '/chat/<int:chatid>')
api.add_resource(Session, '/session/<int:sessionid>')


if __name__ == '__main__':
    app.run(debug=True)