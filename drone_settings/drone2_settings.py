import os

## Using sqlite as database
global DB_URL
db_path = os.path.join(os.path.dirname(__file__), 'database.db')
DB_URL = 'sqlite:///{}'.format(db_path)


global HYDRUS_SERVER_URL, PORT, API_NAME
HYDRUS_SERVER_URL = "http://localhost:8082/"
PORT = 8082
API_NAME = "api"


## Drone configuration
global CENTRAL_SERVER_NAMESPACE, DRONE_NAMESPACE
CENTRAL_SERVER_NAMESPACE = "http://localhost:8080/api/vocab#"
DRONE_NAMESPACE = "http://localhost:8082/api/vocab#"

global DRONE_URL, CENTRAL_SERVER_URL
DRONE_URL = "http://localhost:8082"
CENTRAL_SERVER_URL = "http://localhost:8080"

global IRI_CS, IRI_DRONE
IRI_CS = "http://localhost:8080/api"
IRI_DRONE = "http://localhost:8082/api"

# Default drone object with DroneID -1000 for initialization.
# Speed and MaxSpeeds are in Km/h"""
DRONE_DEFAULT = {
    "@type": "Drone",
    "DroneID": "-1000",
    "name": "Drone 2",
    "model": "xyz",
    "MaxSpeed": "250",
    "Sensor": "Temperature",
    "State": {
        "@type": "State",
        "Speed": "90",
        "Position": "0,0",
        "Battery": "100",
        "Direction": "E",
        "Status": "Active",
    }
}
