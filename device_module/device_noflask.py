import sys
sys.path.append('..')
from device_module.helper import *
#from helper import *
import json

# implement as separate function or 
def format_checking(patient_data):
  return True

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

def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True

def add_patient_data(json_obj):
    if is_json(json_obj): # check data is in correct format
        patient_data = json.loads(json_obj) 
        print(patient_data)
        if 'key' in patient_data.keys():
            key = patient_data['key']
            if key in device_keys: # check device has a key & that key is in the list of device keys
                returnval, code = add_data(patient_data) # could have more errors in adding the data
                return returnval, code #key, 200
            else:
                return {'error': 'Unknown device'}, 403
        else:
            return {'error': 'No device key'}, 401
    else:
        return {'error':'Request must be JSON'}, 415
