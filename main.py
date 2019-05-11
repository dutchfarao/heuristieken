from HelperFunctions.CSVHelper import *
from Classes.dienstvoering import *
from Classes.traject import *
from Classes.graph import Graph
from Algorithms.greedy import *
from Algorithms.random import *
import time
#from Algorithms.hillclimber import *

if __name__ == "__main__":

    scores_dict = {}
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

        random_size = int(input("Please specify the number of times (integer) you want to run Greedy: "))
        start = time.time()
        for j in range(random_size):
            Greedy(j)
        scores_dict = scores_dict_returner()
        best_dienstvoering = max(scores_dict, key=scores_dict.get)
        highscore = scores_dict[best_dienstvoering]
        end = time.time()
        time = end - start
        print("id of best dienstvoering: ", best_dienstvoering, "| score: ", highscore, " | n = ", random_size, " | time elapsed (seconds) = ", time)
        WriteScores(scores_dict, choiceAlgorithm)


    elif choiceAlgorithm == "Random":

        random_size = int(input("Please specify the number of times (integer) you want to run Random: "))
        start = time.time()
        Random(random_size)
        scores_dict = scores_dict_returner()
        best_dienstvoering = max(scores_dict, key=scores_dict.get)
        highscore = scores_dict[best_dienstvoering]
        end = time.time()
        time = end - start
        print("id of best dienstvoering: ", best_dienstvoering, "| score: ", highscore, " | n = ", random_size, " | time elapsed (seconds) = ", time)
        WriteScores(scores_dict, choiceAlgorithm)


    elif choiceAlgorithm == "Hillclimber":
        Hillclimber()

    #elif choiceAlgorithm == "Depth-first":
    #    pass

    #elif choiceAlgorithm == "Random":
    #    pass

    #else:
    #    for i in range(1):
    #        departure = randomizer()
    #        randomRouter(departure[0])
