
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