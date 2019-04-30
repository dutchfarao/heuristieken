
from Classes import station
from Classes import connection
from HelperFunctions.CSVHelper import load_stations, load_connections

INPUT_CONNECTIONS = "Data/ConnectiesHolland.csv"
INPUT_STATIONS = "Data/StationsHolland.csv"

if __name__ == "__main__":
    load_stations(INPUT_STATIONS)
    load_connections(INPUT_CONNECTIONS)
    print(Haarlem)
