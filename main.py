from HelperFunctions.CSVHelper import *
from Classes.dienstvoering import *
from Classes.traject import *
from Classes.graph import Graph
from Algorithms.greedy import *
from Algorithms.random import *

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
    #print(g.station_dict["Alkmaar"].adjacent)

    print("Inputs are: Random, Greedy, Hillclimber or Depth-first.")
    choiceAlgorithm = input("Please specify which algorithm you want to use: ")

    if choiceAlgorithm == "Greedy":
        Greedy()

    elif choiceAlgorithm == "Random":
        Random()    


    #elif choiceAlgorithm == "Hillclimber":
    #    pass

    #elif choiceAlgorithm == "Depth-first":
    #    pass

    #elif choiceAlgorithm == "Random":
    #    pass

    #else:
    #    for i in range(1):
    #        departure = randomizer()
    #        randomRouter(departure[0])
