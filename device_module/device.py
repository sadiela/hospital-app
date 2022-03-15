import requests 
import json
from flask import Flask, request, jsonify, Blueprint
#from helper import *
from flask_pymongo import PyMongo
from flask_restful import fields, marshal_with, reqparse, Resource

device_blueprint = Blueprint('device_blueprint', __name__)

@device_blueprint.route('/')
def index():
    return "This is the device module"

'''
def key(key_str):
    if key in device_keys:
        return key 
    else:
        raise ValueError('{} is not a valid device key'.format(key_str))



post_parser = reqparse.RequestParser()
post_parser.add_argument('key', dest='key', location='form',
                        required=True, type=key, help='The device key')
post_parser.add_argument('name', dest='name', location='form',
                        required=True, help='The name of the patient')

# creating a Flask app
app = Flask(__name__)

mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/health_db")
db = mongodb_client.db

def add_data(patient_data):
    patient_name = patient_data['name']
    idx = -1
    for p in patients:
        if p['name'] == patient_name:
            for d in patient_data['data']:
                cur_type = d['data_type']
                print(cur_type)
                for l in d['values']:
                    p[cur_type][0].append(l[0])
                    p[cur_type][1].append(l[1])

@app.route('/patients', methods=['GET'])
def get_patient_data():
    # load from database
    # print to page in json format
    return jsonify(patients)

@app.route('/patients', methods=['POST'])
def add_patient_data():
    if request.is_json: # check data is in correct format
        patient_data = request.get_json() 
        print(patient_data)
        if 'key' in patient_data.keys():
            key = patient_data['key']
            if key in device_keys: # check device has a key & that key is in the list of device keys
                add_data(patient_data)
                return key, 200
            else:
                return {'error': 'Unknown device'}, 403
        else:
            return {'error': 'No device key'}, 401
    else:
        return {'error':'Request must be JSON'}, 415

'''

if __name__ == '__main__': # FOR TESTING!
    app1 = Flask(__name__)
    app1.register_blueprint(device_blueprint, url_prefix='/device')

    '''# DB SETUP
    mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/health_db")
    db = mongodb_client.db
    db.chat.drop()
    chats = db.chat # chat collection in database'''''''''

    app1.run(debug=True)