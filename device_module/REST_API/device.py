import requests 
import json
from flask import Flask, request, jsonify
#from helper import *
import datetime

# creating a Flask app
app = Flask(__name__)

# Eventually data will be stored in a database
patients= [{'name':'John Doe',
            'temperature':
                [['2020-03-27T19:46:21', '2020-04-27T19:46:21'],[98.6, 98.0]],
            'blood_pressure':
                [['2020-03-27T19:46:21', '2020-04-27T19:46:21'],['120/90', '115/90']],
            'weight':
                [['2020-03-27T19:46:21', '2020-04-27T19:46:21'],[180.0, 181.0]],
            'pulse':
                [['2020-03-27T19:46:21', '2020-04-27T19:46:21'],[60.0, 65.0]],
            'oximeter':
                [['2020-03-27T19:46:21', '2020-04-27T19:46:21'],[90.0, 92.0]],
            'glucometer':
                [['2020-03-27T19:46:21', '2020-04-27T19:46:21'],[200.0, 150.0]]
            },
            {'name':'Jane Doe',
            'temperature':
                [[],[]],
            'blood_pressure':
                [['2020-03-27T19:46:21','2020-04-27T19:46:21'],['120/90', '115/90']],
            'weight':
                [[],[]],
            'pulse':
                [[],[]],
            'oximeter':
                [[],[]],
            'glucometer':
                [[],[]]
            }] 

# for now, save patients/data in list of JSON objects
# later we will store it into a (relational?) database

date_format = "%Y-%m-%dT%H:%M:%S"

device_keys = ['abc', 'def', 'ghi']

json_fields = ['key', 'name', 'data']
data_obj_fields = ['data_type', 'values']
data_type_options = ['temperature','weight','blood_pressure','pulse','oximeter','glucometer']

def check_data_object_format(data):
    return_val = 200
    d_keys = data.keys()
    if set(d_keys) == set(data_obj_fields):
        if data['data_type'] in data_type_options: 
            for time in data['values'][0]:
                try:
                    datetime.datetime.strptime(time, date_format)
                except ValueError:
                    print("INCORRECT DATE STRING FORMAT")
                    return_val = 400
                    break
            if data['data_type'] == 'blood_pressure':
                if not all(isinstance(x, str) for x in data['values'][1]):
                    return_val = 400
            else: 
                if not all(isinstance(x, float) for x in data['values'][1]):
                    return_val = 400
        else:
            print("INVALID DATA_TYPE")
            return_val = 400
    else:
        return_val = 400
    return return_val  

def check_json_format(json_dic):
    # Checks whether the json provided is in the correct format:
    return_val = 200
    keys = json_dic.keys()
    if set(keys) == set(json_fields):
        for d in json_dic['data']:
            return_val = check_data_object_format(d)
            if return_val == 400:
                break
    else: 
        return_val = 400
    return return_val

def add_data(patient_data):
    patient_name = patient_data['name']
    idx = -1
    for p in patients:
        if p['name'] == patient_name:
            for d in patient_data['data']:
                cur_type = d['data_type']
                print(cur_type)
                for date in d['values'][0]:
                    p[cur_type][0].append(date)
                for value in d['values'][1]:
                    p[cur_type][1].append(value)

@app.route('/patients/<id>', methods=['GET'])
def get_single_patient_data(id):
    # load from database
    # print to page in json format
    try:
        return jsonify(patients[int(id)])
    except IndexError:
        return {'error': 'List index out of range'}, 400

@app.route('/patients/all', methods=['GET'])
def get_patient_data():
    # load from database
    # print to page in json format
    return jsonify(patients)

@app.route('/patients', methods=['POST'])
def add_patient_data():
    if request.is_json: # check data is in correct format
        patient_data = request.get_json() 
        if check_json_format(patient_data) == 200:
            print(patient_data)
            key = patient_data['key']
            if key in device_keys: # check device has a key & that key is in the list of device keys
                add_data(patient_data)
                return key, 200
            else:
                return {'error': 'Unknown device'}, 403
        else:
            return {'error': 'JSON formatting issues'}, 400
    else:
        return {'error':'Request must be JSON'}, 415

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


if __name__ == '__main__':
  
    app.run(debug = True)