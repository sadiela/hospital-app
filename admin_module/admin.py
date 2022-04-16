# This file contains functions that can only be performed by admins
# Only Admins can modify the USER and DEVICE databases
# KIWI
#from xml.dom import ValidationErr
import requests 
import json
from flask import Flask, request, jsonify, Blueprint
#from helper import *
from flask_pymongo import PyMongo
import pymongo
from marshmallow import Schema, fields, ValidationError
from database_module.mongo_database import mongodb_client

db = mongodb_client['healthDB']
devices = db['devices'] # --> device id, patient
people = db['people']
#people.create_index([("userid", pymongo.ASCENDING)], unique=True)
#devices.create_index([("userid", pymongo.ASCENDING)], unique=True)

admin_blueprint = Blueprint('admin_blueprint', __name__)

#### PUSHED TO ADMIN MODULE ####
#   - get device list
#   - get patient list
#   - add user
#   - assign device to user

role_key = {
   'patient': 0, 
   'doctor': 1,
   'administrator':2
}

def insertion_index(nums):
    n = 0 
    s = set(nums)
    if len(s)==0:
        return 0
    #while n in s:
    #    n += 1
    return max(s) + 1

class UserSchema(Schema):
    userid = fields.Int(required=True)
    username = fields.String(required=True)
    email = fields.Email()
    role = fields.Int(required=True)
    devices = fields.List(fields.String)
    doctors = fields.List(fields.Int()) # list of userids
    patients = fields.List(fields.Int()) # list of userids

def custom_find(coll, key=None, value=None):
    res = []
    if value is not None and key is not None:
        vals = coll.find({key:value}, projection={'_id': False})
    else: 
        vals = coll.find(projection={'_id': False})
    for x in vals:
        res.append(x)
    return res

def addDevice(device_name):
    device_data = {'deviceid': device_name}
    res = devices.insert_one(device_data)

@admin_blueprint.route('/devices', methods=['GET'])
def get_device_list():
    device_list = custom_find(devices)
    if len(device_list)==0:
        print("NO DEVICES FOUND")
        return "NO DEVICES FOUND", 200
    return jsonify(device_list), 200

@admin_blueprint.route('/assign_device/<deviceid>/<patientid>', methods=['GET', 'POST', 'PUT'])
def assign_device(deviceid, patientid):
    # assign the given device to the given patient
    if deviceid in devices.distinct('deviceid'):
        print("device exists")
        devicelist = people.find_one({'userid':patientid}, projection=['devices'])
        print("DEVICE LIST:", devicelist)
        if devicelist is None:
            devicelist = [deviceid]
        elif deviceid not in devicelist:
            devicelist.append(deviceid)
        else:
            return f"device with id {deviceid} already assigned to user {patientid}", 200
        newvalues = {"$set": {"devices":devicelist}}
        people.update_one({'userid':patientid}, newvalues)
    else:
        return f"No device with id {deviceid} exists", 400
    return f"added device {deviceid} to user {patientid}"

@admin_blueprint.route('/doctors/<patientid>', methods=['GET'])
def get_doctor_list(patientid): # get all patients, doctors, or admins
    doctor_ids = people.find_one({'userid':int(patientid)}, projection=['doctors'])
    # check if all these people are still in the DB
    del doctor_ids['_id']
    print("DOCTOR IDS:", doctor_ids)
    return jsonify(doctor_ids), 200

@admin_blueprint.route('/patients/<doctorid>', methods=['GET'])
def get_patient_list(doctorid): # get all patients, doctors, or admins
    patient_ids = people.find_one({'userid':int(doctorid)}, projection=['patients'])
    # check if all these people are still in the DB
    del patient_ids['_id']
    print("PATIENTIDS:", patient_ids)
    return jsonify(patient_ids), 200

@admin_blueprint.route('/people/<roleid>', methods=['GET'])
def get_role_list(roleid): # get all patients, doctors, or admins
    #desired_role = role_key[role]
    person_list = custom_find(people, 'role', int(roleid))
    if len(person_list)==0:
        print("NO PEOPLE WITH ROLE {role} FOUND")
        return "NO PEOPLE WITH ROLE {role} FOUND", 200
    return jsonify(person_list), 200


@admin_blueprint.route('/people', methods=['GET'])
def get_user_list(): # get all patients, doctors, or admins
    #desired_role = role_key[role]
    person_list = custom_find(people)
    if len(person_list)==0:
        print("NO PEOPLEFOUND")
        return "NO PEOPLE FOUND", 200
    return jsonify(person_list), 200

@admin_blueprint.route('/add_user', methods=['GET', 'POST', 'PUT'])
def add_chat():
    print("ADDING USER")
    if request.is_json: # check data is in correct format
        user_data = request.get_json() 
        try:
            user_data = UserSchema().load(user_data)
        except ValidationError as err:
            print(err.messages)
            print(err.valid_data)
            print("INVALID USER DATA")
            return "Invalid data", 400
        id_vals = people.distinct('userid')
        new_id = insertion_index(id_vals)
        user_data['userid'] = new_id
        # add all devices linked to user
        if 'devices' in user_data.keys():
            for d in user_data['devices']:
                if d not in devices.distinct('deviceid'):
                    addDevice(d)
        res = people.insert_one(user_data)
        print("USER ADDED")
        return str(res.acknowledged)
    print("INVALID REQUEST DATA")
    return "INVALID REQUEST DATA", 400

@admin_blueprint.route('/remove_user/<userid>', methods=['GET', 'POST', 'PUT'])
def remove_user(userid):
    print("ID", userid)
    # check if userid is in database
    res = people.delete_one({ "userid": int(userid)})
    print(res, people.distinct('userid'))
    print("DELETE RESULT:", str(res.acknowledged))
    return f"deleted user {userid} from user database"

'''
@admin_blueprint.route('/assign_doctor/<doctorid>', methods=['GET'])
def assign_doctor(doctorid):

    return "Assigning doctor to patient(s)"

@admin_blueprint.route('/assign_patient/<patientid>', methods=['GET'])
def assign_patient(patientid):

    return "Assigning patients to doctor(s)"'''

@admin_blueprint.route('/')
def index():
    return "This is the admin module"

device_blueprint = Blueprint('device_blueprint', __name__)
