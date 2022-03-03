import sys
sys.path.append('..')
from helper import *
#from helper import *
import json
#from jsonschema import validate

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

data_value_schema = {
  "type":"object",
  "properties": {
    "data_type":{"type":"string"},
    "values":{
        "type":"array",
        "items":{
          "type":"array"
          }
        }
  }
}

'''
# implement as separate function or 
def format_checking(patient_data):
  try:
    validate(instance=patient_data, schema=[patient_data_schema])
    for data_object in patient_data["data"]:
      validate(instance=data_object, schema=[data_value_schema])
  except jsonschema.exceptions.ValidationError as err:
    print("err")
  return True'''


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

def is_json(text):
  print("IS JSON?", text)
  try:
      return json.loads(text)
  except ValueError as e:
      print('invalid json: %s' % e)
      return False # or: raise

def add_patient_data(json_obj):
    if is_json(json_obj): # check data is in correct format
      print("IS A JSON")
      patient_data = json.loads(json_obj) 
      print(patient_data, type(patient_data))
      input("Continue...")
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

#print(is_json('NOT:A:JSON'))
#print(patients)
if __name__ == '__main__':
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

  patient_data = str(patient_data)

  add_patient_data(patient_data)