# Hospital Application
Platform to monitor patients at home or in the hospitals. See wiki for detailed user stories and documentation for each module. 

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
