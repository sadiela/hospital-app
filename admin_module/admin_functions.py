# This file contains functions that can only be performed by admins
# Only Admins can modify the USER and DEVICE databases
# KIWI
from xml.dom import ValidationErr
import requests 
import json
from flask import Flask, request, jsonify, Blueprint
#from helper import *
from flask_pymongo import PyMongo
import pymongo
from marshmallow import Schema, fields
from database_module.mongo_database import mongodb_client

db = mongodb_client['healthDB']
devices = db['devices'] # --> device id, patient
people = db['people']

admin_blueprint = Blueprint('admin_blueprint', __name__)

#### PUSHED TO ADMIN MODULE ####
#   - get device list
#   - get patient list

def addUser():
    print("Added")

def modifyUser(): 
    print("Modified")

def removeUser():
    print("Removed")

# DEVICE DB FUNCTIONS
def addDevice():
    print("Added")

def modifyDevice():
    print("Modified")

def removeDevice(): 
    print("Deleted")

@admin_blueprint.route('/devices', methods=['GET'])
def get_device_list():
    return "Returning list of device IDs"

@admin_blueprint.route('/patients/all', methods=['GET'])
def get_patient_list():
    return "Returning list of patient names"

device_blueprint = Blueprint('device_blueprint', __name__)
