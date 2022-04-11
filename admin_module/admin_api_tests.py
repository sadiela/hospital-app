from requests import put, get
import pymongo 
import json


### TEST CASES ### 
# Add user
    # Add doctor
    # Add patient
    # Add admin
    # Try to add invalid data
# List all patients
# List all doctors
# List doctors for given patient
# List patients for given doctor
# Delete user

patient1 = {
    'userid':0,
    'username':'JohnDoe',
    'role':0,
    'devices':['abc'],
    'doctors':[2],
}

patient2 = {
    'userid':1,
    'username':'JaneDoe',
    'role':0,
    'devices':['def'],
    'doctors':[2]
}

doctor1 = {
    'userid':2,
    'username':'BobSmith',
    'role':1,
    'patients':[0, 1]
}

admin1 = {
    'userid':3,
    'username':'NancyBrown',
    'role':2
}

invalid_user = {
    'userid':0,
    'username':4,
    'role':0
}

### ADD USER TESTS ###
## CONNECT TO DB ##
#filepath = r'C:\Users\sadie\Documents\BU\spring_2022\ec530\hospital-app\cert\X509-cert-1835095331508356146.pem'
filepath = r'/Users/sadiela/Documents/courses_spring_2022/ec530/cert/X509-cert-1835095331508356146.pem'
uri  = r"mongodb+srv://cluster0.ipuos.mongodb.net/healthDB?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
mongodb_client = pymongo.MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile=filepath)

db = mongodb_client['healthDB']
user_collection = db['people']
device_collection = db['devices']
user_count = user_collection.count_documents({})
device_count = device_collection.count_documents({})

print(user_count, device_count)

## CLEAR DBS BEFORE TESTING ##
user_delete = user_collection.delete_many({})
device_delete = device_collection.delete_many({})
print(user_delete.deleted_count, "documents deleted")
print(device_delete.deleted_count, "documents deleted")

## PERFORM ADD TESTS (THREE VALID, TWO INVALID)
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
res1 = put('http://127.0.0.1:5000/admin/add_user', data=json.dumps(patient1), headers=headers)#.json()
print(res1,res1.content.decode())
res2 = put('http://127.0.0.1:5000/admin/add_user', data=json.dumps(patient2), headers=headers)#.json()
print(res1,res1.content.decode())
res3 = put('http://127.0.0.1:5000/admin/add_user', data=json.dumps(doctor1), headers=headers)#.json()
print(res1,res1.content.decode())
res4 = put('http://127.0.0.1:5000/admin/add_user', data=json.dumps(admin1), headers=headers)#.json()
print(res1,res1.content.decode())
res5 = put('http://127.0.0.1:5000/admin/add_user', data=json.dumps(invalid_user), headers=headers)#.json()
print(res1,res1.content.decode())

### LIST DEVICES TEST ###
res6 = get('http://127.0.0.1:5000/admin/devices')
print(res6, res6.content.decode())

### LIST PATIENTS TEST ###
res7 = get('http://127.0.0.1:5000/admin/people/0')
print(res7, res7.content.decode())
res8 = get('http://127.0.0.1:5000/admin/patients/2')
print(res8, res8.content.decode())

### LIST DOCTORS TEST ###
res9 = get('http://127.0.0.1:5000/admin/people/1')
print(res9, res9.content.decode())

res10 = get('http://127.0.0.1:5000/admin/doctors/0')
print(res10, res10.content.decode())

### LIST ADMINS TEST ###
res11 = get('http://127.0.0.1:5000/admin/people/2')
print(res11, res11.content.decode())

### DELETE USERS TESTS ###
res12 = put('http://127.0.0.1:5000/admin/remove_user/0')
print(res12, res12.content.decode())


print(user_collection.distinct('username'))


