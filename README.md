# watch-shop
Quick Flask API Demo implementing a checkout endpoint.

## Running the Application
Install Python 3.7 or newer from https://www.python.org/downloads/

Install Flask as described at https://flask.palletsprojects.com/en/2.2.x/installation/

The application can be run locally under the Flask development server by 
running `python -m flask run` when in the watch-shop directory

## Running Tests
Most tests are implemented in Python's UnitTest framework. Run these from the top level directory with
`python -m unittest discover -v`

The API proper can be exercised by starting the application and then running `./api_test.sh`

## Design Notes
The application is structured into 3 modules, forming a dependency stack.

| Module         | Description                                                                                                                             |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| API Routing    | Only module that interacts with the Flask Framework, provides marshalling of Request and Response data for the rest of the application. |
| Business Logic | Logic for calculating the checkout result. Only module that understands how to interpret watch data.                                    |
| Data Access    | Abstraction of the data store used to provide watch data. In this implementation the data store is a CSV file                           |

Each module provides an interface to the one above implemented using built in
datatypes. Each module can only communicate with the layer above or below it in, 
simplifying dependencies. Modules should not make any assumptions about the
implementations of others.

The call flow through the modules for a checkout request is as follows.

```mermaid
sequenceDiagram 
Client->>+API Routing: JSON Request with list of Watch IDs
API Routing->>+Buisness Logic: Calculate Total Price
loop For Each Unique Watch ID
    Buisness Logic->>+Data Access: Fetch Data for Watch ID
    Data Access-->>-Buisness Logic: Watch Data   
end
Buisness Logic-->>-API Routing: Total Price
API Routing-->>-Client: JSON Reponse with Total Price
```
