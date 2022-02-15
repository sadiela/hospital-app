
# Eventually data will be stored in a database
patients= [{'name':'John Doe',
            'temperature':
                [['2/8/2022', '2/9/2022'],[98.6, 98.0]],
            'blood_pressure':
                [['2/8/2022', '2/9/2022'],['120/90', '115/90']],
            'weight':
                [['2/8/2022', '2/9/2022'],[180, 181]],
            'pulse':
                [['2/8/2022', '2/9/2022'],[60, 65]],
            'oximeter':
                [['2/8/2022', '2/9/2022'],[90, 92]],
            'glucometer':
                [['2/8/2022', '2/9/2022'],[200, 150]]
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

device_keys = ['abc', 'def', 'ghi']

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

if __name__ == '__main__':

    print(patients)
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

    add_data(patient_data)

    print(patients)