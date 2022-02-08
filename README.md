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
    * Family memober
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
2. Set up branching strategy
    a. When to add main?
### Phase 1 (DUE 2/13/2021)
1. Define interface for devices to send data to system
    a. Data fields (including knowing how to attribute data to a patient)
    b. Error conditions
    c. Pull or push mechanisms?
    d. Include the following data types:
        i. Temperature
        ii. Blood pressure
        iii. Pulse
        iv. Oximeter
        v. weight
        vi. Glucometer 
    e. Implement shell of device interface
    f. Implement unit tests for the module
    g. Implement a simulation to send data via an example program to help users of your system
    h. DOCUMENT INTERFACE WELL
    
FOR NOW: HARD CODE DEVICE KEYS
I think I want pull mechanisms, then I can choose how often to read... seems harder though


## Device Interface Documentation


