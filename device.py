import requests 
import json
from flask import Flask, request, jsonify

# $env:FLASK_APP = "device.py"
# $env:FLASK_ENV="development"

app = Flask(__name__)


# Eventually data will be stored in a database
patients = [{'name':'John Doe',
              'temperature':
                  [{'2/8/2022':98.6}],
              'blood_pressure':
                  [{'2/8/2022':'120/90'}],
              'weight':
                  [{'2/8/2022':'180'}]
            }] 

# for now, save patients/data in list of JSON objects
# later we will store it into a (relational?) database

device_keys = ['abc', 'def', 'ghi']

@app.route('/patients', methods=['GET'])
def get_patient_data():
    # load from database
    # print to page in json format
    return jsonify(patients)

@app.route('/patients', methods=['POST'])
def add_patient_data():
    print("ADDING PATIENT!")
    if request.is_json: # check data is in correct format
        patient_data = request.get_json() 
        print(patient_data)
        key = patient_data['key']
        if key in device_keys: # check device has a key & that key is in the list of device keys
            patients.append(patient_data)
            return key, 200
        else:
            return {'error': 'Unknown device'}, 403
    else:
        return {'error':'Request must be JSON'}, 415

'''
# API get request
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
print(response.json())

# API post request
api_url2 = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response2 = requests.post(api_url2, json=todo)
print(response2.json(), response2.status_code)'''

## What resources will the API manage? 
# PATIENTS! --> all data uploaded has to be associated with a patient
