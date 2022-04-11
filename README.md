# Hospital Application
Platform to monitor patients at home or in the hospitals. See the [wiki](https://github.com/sadiela/hospital-app/wiki) for detailed user stories, documentation, and unit tests/results for each module.

# Setup 
1. Set up virtual environment for project
2. Install requirements from `requirements.txt`:

# Branching Strategy
Will work on different modules in their own branches and merge to main after thorough unit testing for integration testing. 

## Modules
* **Device module**
    * Support many datatypes
    * API that 3rd party devices will use to publish data to system
    * JSON format input
* **Chat Module**
    * MP/Patient communication
* **Administrative**
    * Create users, assign roles

----- Eventually add... -----

* **Calendar Module**
    * Display all appointments for MPs
    * Display available appointment times for patients
* **Alerts Module**
    * Create alert
    * Send alerts to MPs
* **Voice Transcriber**
    * Voice -> text 
* **Data Management**
    * Store all data for other modules
* **Application Interfaces**
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
    
### VM API SETUP:

verify: `python3 app.py`

run gunicorn: `gunicorn -b 0.0.0.0:8000 app:app`

enable service: 
```sudo systemctl daemon-reload
   sudo systemctl start helloworld
   sudo systemctl enable helloworld```
