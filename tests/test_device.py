import sys
from pathlib import Path
sys.path.append('.')
import json
from device_module.helper import *
from device_module.device_noflask import * 

homeDirectory = Path('.')

# dbdiagram.io
no_key = {  
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

invalid_key = {  
   'key': 'abd',
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

valid_data = {  
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

#print(patients)
#print(add_patient_data(json.dumps(no_key)))
#print(add_patient_data(json.dumps(invalid_key)))
#print(add_patient_data(json.dumps(patient_data)))
#print(add_patient_data('HELLO!'))

#print(patients)

def test_not_json():
    assert add_patient_data(json.dumps('NOT:A:"JS"ON')) == ({'error':'Request must be JSON'}, 415)

def test_no_key():
    assert add_patient_data(json.dumps(no_key)) == ({'error':'No device key'}, 401)

def test_invalid_key():
    assert add_patient_data(json.dumps(invalid_key)) == ({'error':'Unknown device'}, 403)

def test_valid_json():
    print("START")
    assert add_patient_data(json.dumps(valid_data)) == ('abc', 200)
