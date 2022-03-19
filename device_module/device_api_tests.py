import sys
sys.path.append('..')
from helper import *
#from helper import *
import json
import requests
#from jsonschema import validate
import pymongo

#temperature data
'''data_example = {
  'dataid':0,
  'patientid':0,
  'data_type':'temperature',
  'timestamp':'2020-03-27T19:46:21',
  'value':98.9,
}'''

data_to_push = {
  'key': 'abc',
  'patientid': 'JohnDoe',
  'data_type': 'weight',
  'values': [170, 175, 172],
  'timestamps': ['2020-03-27T19:46:21', '2020-03-28T19:46:21', '2020-03-28T19:56:21']
}

data_to_push2 = {
  'key': 'def',
  'patientid': 'JaneDoe',
  'data_type': 'pulse',
  'values': [60, 115, 72],
  'timestamps': ['2020-03-27T19:46:21', '2020-03-28T19:46:21', '2020-03-28T19:56:21']
}

invalid_data_to_push = {
  'key': 'def',
  'patientid': 'JaneDoe',
  #'data_type': 'blood_pressure',
  'values': [170, 175, 172],
  'timestamps': ['2020-03-27T19:46:21', '2020-03-28T19:46:21', '2020-03-28T19:56:21']
}

invalid_key_data = {
  'key': 'ghi',
  'patientid': 'JaneDoe',
  'data_type': 'weight',
  'values': [170, 175, 172],
  'timestamps': ['2020-03-27T19:46:21', '2020-03-28T19:46:21', '2020-03-28T19:56:21']
}


## CONNECT TO DB ##
filepath = r'C:\Users\sadie\Documents\BU\spring_2022\ec530\hospital-app\cert\X509-cert-1835095331508356146.pem'

uri  = r"mongodb+srv://cluster0.ipuos.mongodb.net/healthDB?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
mongodb_client = pymongo.MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile=filepath)

db = mongodb_client['healthDB']
health_data = db['health_data']
devices = db['devices']
doc_count = health_data.count_documents({})
print(doc_count)

### CLEAR OUT DB COLLECTIONS ###
x = health_data.delete_many({})
print(x.deleted_count, "documents deleted")
x2 = devices.delete_many({})
print(x2.deleted_count, "documents deleted")

# Add some devices to device DB:
device1 = {'deviceid':'abc'}
device2 = {'deviceid':'def'}
devices.insert_one(device1)
devices.insert_one(device2)

# TEST ADDING DATA
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post('http://127.0.0.1:5000/device/add-data', data=json.dumps(data_to_push), headers=headers)
print(r)
r = requests.post('http://127.0.0.1:5000/device/add-data', data=json.dumps(data_to_push2), headers=headers)
print(r)
r = requests.post('http://127.0.0.1:5000/device/add-data', data=json.dumps(invalid_data_to_push), headers=headers)
print(r)
r = requests.post('http://127.0.0.1:5000/device/add-data', data=json.dumps(invalid_key_data), headers=headers)
print(r)

# TEST GETTING DATA # 
print(requests.get('http://127.0.0.1:5000/device/patients/JohnDoe/weight'))
print(requests.get('http://127.0.0.1:5000/device/patients/JaneDoe/pulse'))
print(requests.get('http://127.0.0.1:5000/device/patients/JaneDoe/blood_pressure'))
print(requests.get('http://127.0.0.1:5000/device/patients/JanetDoe/pulse'))



''' 
Test Cases:
1. JSON w/o key field
2. JSON w/ key not in device_keys list
3. Correctly-formatted JSON
'''