from Helperfunctions/CSVHelper import load_stations, load_connections
from station import Station
from connection import connection

if __name__ == "__main__":
    load_stations(INPUT_STATIONS)
    load_connections(INPUT_CONNECTIONS)
    print(Haarlem)
