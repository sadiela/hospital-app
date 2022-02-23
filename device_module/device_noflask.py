import sys
sys.path.append('..')
from device_module.helper import *
#from helper import *
import json
from jsonschema import validate

patient_data = {  
   'key': 'abc',
   'name': 'John Doe',
   'data': [
            {  'data_type': 'blood_pressure',
               'values': [['2020-03-27T19:46:21', '120/80']]
            },
            {  'data_type': 'temperature',
               'values': [['2020-03-27T19:46:21', 98.6],['2020-03-28T19:46:21', 99.6]]
            }
           ]
    }

patient_data_schema = {
  "type":"object",
  "properties": {
    "key":{"type":"string"},
    "name":{"type":"string"},
    "data":{"type":"list"}
  }

}


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
                add_data(patient_data)
                return key, 200
            else:
                return {'error': 'Unknown device'}, 403
        else:
            return {'error': 'No device key'}, 401
    else:
        return {'error':'Request must be JSON'}, 415

print(is_json('NOT:A:JSON'))

try:
    validate(instance=patient_data, schema=[patient_data_schema])
except jsonschema.exceptions.ValidationError as err:
    print("EXCEPTION")
print("VALID")