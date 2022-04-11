import sys
sys.path.append('..')
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
#filepath = r'/Users/sadiela/Documents/courses_spring_2022/ec530/cert/X509-cert-1835095331508356146.pem'

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
device3 = {'device!':'ghi'}
#devices.insert_one(device1)
#devices.insert_one(device2)

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

# TEST ADDING DEVICES
r0 = requests.post('http://127.0.0.1:5000/device/add-device', data=json.dumps(device1), headers=headers)
print(r0,r0.content.decode())
r01 = requests.post('http://127.0.0.1:5000/device/add-device', data=json.dumps(device2), headers=headers)
print(r01,r01.content.decode())
r02 = requests.post('http://127.0.0.1:5000/device/add-device', data=json.dumps(device3), headers=headers)
print(r02,r02.content.decode())

# TEST ADDING DATA
r1 = requests.post('http://127.0.0.1:5000/device/add-data', data=json.dumps(data_to_push), headers=headers)
print(r1,r1.content.decode())
r2 = requests.post('http://127.0.0.1:5000/device/add-data', data=json.dumps(data_to_push2), headers=headers)
print(r2,r2.content.decode())
r3 = requests.post('http://127.0.0.1:5000/device/add-data', data=json.dumps(invalid_data_to_push), headers=headers)
print(r3,r3.content.decode())
r4 = requests.post('http://127.0.0.1:5000/device/add-data', data=json.dumps(invalid_key_data), headers=headers)
print(r4,r4.content.decode())


# TEST GETTING DATA # 
r5 = requests.get('http://127.0.0.1:5000/device/patients/JohnDoe/weight')
print(r5,r5.content.decode())
r6 = requests.get('http://127.0.0.1:5000/device/patients/JaneDoe/pulse')
print(r6,r6.content.decode())
r7 = requests.get('http://127.0.0.1:5000/device/patients/JaneDoe/blood_pres')
print(r7,r7.content.decode())
r8 = requests.get('http://127.0.0.1:5000/device/patients/JanetDoe/pulse')
print(r8,r8.content.decode())

# TEST DELETING DATA #
r9 = requests.get('http://127.0.0.1:5000/device/delete-data/def')
print(r9,r9.content.decode())
print(health_data.distinct('source_device'))

# TEST DELETING DEVICES #
r10 = requests.get('http://127.0.0.1:5000/device/delete-device/def')
print(r10,r10.content.decode())
print(devices.distinct('deviceid'))


''' 
Test Cases:
1. JSON w/o key field
2. JSON w/ key not in device_keys list
3. Correctly-formatted JSON
'''