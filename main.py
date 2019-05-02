from HelperFunctions.CSVHelper import *
from Classes.dienstvoering import *
from Classes.graph import Graph

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
    #print(g.station_dict)
    print(g.station_dict["Alkmaar"].adjacent)

    choiceAlgorithm = input("Please specify which algorithm you want to use. ")
    #if choiceAlgorithm == "random":
