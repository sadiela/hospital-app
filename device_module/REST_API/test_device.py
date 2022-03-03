import requests
import json


# dbdiagram.io
no_key = {  
   'name': 'John Doe',
   'data': [
            {  'data_type': 'blood_pressure',
               'values': [['2020-03-27T19:46:21'], ['120/80']]
            },
            {  'data_type': 'temperature',
               'values': [['2020-03-27T19:46:21', '2020-03-28T19:46:21'],[98.6, 99.6]]
            }
           ]
}

invalid_key = {  
   'key': 'abd',
   'name': 'John Doe',
   'data': [
            {  'data_type': 'blood_pressure',
               'values': [['2020-03-27T19:46:21'], ['120/80']]
            },
            {  'data_type': 'temperature',
               'values': [['2020-03-27T19:46:21', '2020-03-28T19:46:21'],[98.6, 99.6]]
            }
           ]
}

patient_data = {  
   'key': 'abc',
   'name': 'John Doe',
   'data': [
            {  'data_type': 'blood_pressure',
               'values': [['2020-03-27T19:46:21'], ['120/80']]
            },
            {  'data_type': 'temperature',
               'values': [['2020-03-27T19:46:21', '2020-03-28T19:46:21'],[98.6, 99.6]]
            }
           ]
}

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post('http://127.0.0.1:5000/patients', data=json.dumps(no_key), headers=headers)
r = requests.post('http://127.0.0.1:5000/patients', data=json.dumps(invalid_key), headers=headers)
r = requests.post('http://127.0.0.1:5000/patients', data=json.dumps(patient_data), headers=headers)

''' 
Test Cases:
1. JSON w/o key field
2. JSON w/ key not in device_keys list
3. Correctly-formatted JSON
'''