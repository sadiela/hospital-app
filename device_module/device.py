import requests 
import json
from flask import Flask, request, jsonify, Blueprint
from flask_pymongo import PyMongo
import pymongo
from marshmallow import Schema, fields, ValidationError
from database_module.mongo_database import mongodb_client

db = mongodb_client['healthDB']
devices = db['devices'] # --> device id, patient
health_data = db['health_data']
### DATA ###
blood_pressure = db['blood_pressure']
weight = db['weight']
temp = db['temp']
pulse = db['pulse']
oximeter = db['oximeter']
glucometer = db['glucometer']

device_blueprint = Blueprint('device_blueprint', __name__)

# Need to be able to:
#   - get patient's data (all types)
#   - post data for a patient
def insertion_index(nums):
    n = 0
    s = set(nums)
    while n in s:
        n += 1
    return n

class DataSchema(Schema):
    key = fields.String(required=True)
    patientid = fields.String(required=True)
    data_type = fields.String(required=True)
    values = fields.List(fields.Float, required=True)
    timestamps = fields.List(fields.DateTime, required=True)

# DEVICE DB FUNCTIONS
def addDevice():
    print("Added")

def modifyDevice():
    print("Modified")

def removeDevice(): 
    print("Deleted")

@device_blueprint.route('/add-data', methods=['POST', 'GET', 'PUT'])
def add_patient_data():
    print("ADDING DATA")
    if request.is_json:
        data = request.get_json()
        try:
            data = DataSchema().load(data)
        except ValidationError as err:
            print(err.messages)
            print(err.valid_data)
            return "Invalid data", 400
        if data['key'] not in devices.distinct('deviceid'):
            return "INVALID DATA KEY", 400
        for v, t in zip(data['values'], data['timestamps']):
            id_vals = health_data.distinct('chatid')
            new_id = insertion_index(id_vals)
            data_item = {'dataid':new_id, 'patientid':data['patientid'], 'data_type':data['data_type'], 'timestamp':t, 'value':v}
            health_data.insert_one(data_item)
        return "ALL DATA ADDED", 200
    return "Invalid Data", 400

@device_blueprint.route('/patients/<patientid>/<datatype>', methods=['GET'])
def get_patient_data(patientid, datatype):
    print(f"Getting all {datatype} data for patient {patientid}")
    vals = health_data.find({'patientid': patientid, 'data_type':datatype})
    res = []
    for x in vals: 
        del x['_id']
        res.append(x)
    if len(res)==0:
        print("NO DATA FOUND")
        return f"NO {datatype} DATA FOR PATIENT {patientid} FOUND", 200
    return jsonify(res), 200

@device_blueprint.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource (device) could not be found.</p>", 404

@device_blueprint.route('/')
def index():
    return "This is the device module"

if __name__ == '__main__': # FOR TESTING!
    app1 = Flask(__name__)
    app1.register_blueprint(device_blueprint, url_prefix='/device')

