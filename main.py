from HelperFunctions.CSVHelper import *
from Classes.dienstvoering import *

if __name__ == "__main__":

    choiceRegion = input("Dienstregeling voor heel Nederland of Noord en Zuid Holland? ")

    if choiceRegion == "Nederland":
        INPUT_CONNECTIONS = "Data/ConnectiesNationaal.csv"
        INPUT_STATIONS = "Data/StationsNationaal.csv"

    else:
        INPUT_CONNECTIONS = "Data/ConnectiesHolland.csv"
        INPUT_STATIONS = "Data/StationsHolland.csv"

    load_stations(INPUT_STATIONS)
    load_connections(INPUT_CONNECTIONS)
    station_printer()
    connection_printer()

    dienstregeling = Dienstvoering(1)
    print(dienstregeling)

    #WriteScores(results)
