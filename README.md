# Hospital Application
Platform to monitor patients at home or in the hospitals.

Users: 
* Patients
* Medical professionals (nurses/doctors)
* Administrators
* Developers
    * Application developers
    * Device integrators
    * ML Scientists
 
## User Stories
**Administrators**:
* Add users to system
* Assign and change user roles (note that one user can have multiple roles)
    * Patient
    * Nurse
    * Doctor
    * Family member
    * Admin
* Provide interfaces to third party medical device makers to have their device feed data to the system
    * Thermometer
    * Pulse
    * Blood pressure
    * Glucometer
    * Weight
* Disable/enable device makers or app developers

**Medical Professionals**:
* Browse patients
* Assign a medical device to a patient
* Assign alert and scheduling for medical measurement
    * Patient measures blood pressure daily; MP receives alert if not done
    * Temperature higher/lower than particular value; MP gets alert if measurement outside acceptable range
* Input data for patient (what kind of data?)
* Chat w/ patients using text, voice, video
* Read transcripts of patient uploaded videos/messages
* Search for keywords in messages/chats
* Calendar to show open time slots for appointments 
* See all appointments booked at any time

**Patients**
* Enter measurements
* Write text/upload video or voice message to MP
* Book an appointment with MP
* View measurements 

## Modules
**Device module**
* Support many datatypes
* API that 3rd party devices will use to publish data to system
* JSON format input
**Calendar Module**
* Display all appointments for MPs
* Display available appointment times for patients
**Alerts Module**
* Create alert
* Send alerts to MPs
**Chat Module**
* MP/Patient communication
**Voice Transcriber**
* Voice -> text 
**Administrative**
* Create users, assign roles
**Data Management**
* Store all data for other modules
**Application Interfaces**
* How users interact with system

## Phases
### Phase 0 (DUE 2/13/2021)
1. Set up Agile environment
2. Set up branching strategy (when to add main?)
### Phase 1 (DUE 2/13/2021)
1. Define interface for devices to send data to system
    * Data fields (including knowing how to attribute data to a patient)
    * Error conditions
    * Pull or push mechanisms?
    * Include the following data types:
        i. Temperature
        ii. Blood pressure
        iii. Pulse
        iv. Oximeter
        v. weight
        vi. Glucometer 
    * Implement shell of device interface
    * Implement unit tests for the module
    * Implement a simulation to send data via an example program to help users of your system
    * DOCUMENT INTERFACE WELL
    
FOR NOW: HARD CODE DEVICE KEYS

## Device Interface Documentation
ASSUMPTIONS:
* Each device only associated with a single patient

Third party devices will push data to the system via HTTP POST requests. The data must be pushed in JSON format and have the following syntax/fields:

```css
{  
   'key': DEVICE_KEY,
   'name': USER_NAME,
   'data': [
            {  'data_type': DATA_TYPE1,
               'values': [[DATETIME_STRING1, VALUE1],[DATETIME_STRING2, VALUE2],....[DATETIME_STRINGN, VALUEN]]
            }
            {  'data_type': DATA_TYPE2,
               'values': [[DATETIME_STRING1, VALUE1],[DATETIME_STRING2, VALUE2],....[DATETIME_STRINGN, VALUEN]]
            }
           ]
}
```

* `DEVICE_KEY`: The device must have a key and that key must match the list of authorized keys in the device database
* `USER_NAME`: Provide unique identifier for device user which must match the user assigned to the device in the device database
* `DATA_TYPE`: The type of data the following values correspond to
* `'values'`: List of tuples with the first element being the time a measurement was taken and the second element being the measurement value
   * `DATETIME_STRING`: Date/time when measurement was taken must be in the following format: "2020-03-27T19:46:21" --> `%Y-%m-%dT%H:%M:%S`. Assumed to be EST.
   * `VALUE`: Measurement value at the given time


Possible values for `DATA_TYPE`:
* temperature
* weight
* blood_pressure
* pulse
* oximeter
* glucometer

Eventually, this data will be stored in a database. For now, we add it to our "patients" JSON object under the proper patient. 

## DATABASE SCHEMA
### **User** Database
* Rows represent system users
* Columns: 
   * Unique ID
   * First name
   * Last name
   * Address
   * DOB
   * Sex
   * Role
   * PCP (if patient) 
### Health Measurements Database(s)
* One of these for each data type (bp, weight, height, temp, etc.)
* Rows represent readings
* Each row has the following columns:
   * **User** ID
   * Temperature
   * Time
### Device Database
* Device Name
* MAC Address(?)
* Device Key
* Assigned **user**
* Data types supported
### Roles Database
* Row for each role
* Columns represent permissions for different actions (binary entries) for given users
   * Create new user
   * Make appointment
   * View own data
   * View others' data 
### MP Database
* 
