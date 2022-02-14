import requests 
import json
from flask import Flask, request, jsonify
from helper import *

# creating a Flask app
app = Flask(__name__)

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


if __name__ == '__main__':
  
    app.run(debug = True)