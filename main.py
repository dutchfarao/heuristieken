from HelperFunctions.CSVHelper import *
from Classes.dienstvoering import *
from Classes.traject import *
from Classes.graph import Graph
from Algorithms.greedy import *
from Algorithms.random import *
from Algorithms.random2 import *
from Algorithms.hillclimber import *
from HelperFunctions.VisualisationHelper import *
import time

if __name__ == "__main__":

    scores_dict = {}
    data = {}

    choiceAction = input("Would you like to run algorithms or perform visualisations? Select 'a' or 'v'")
    if choiceAction == 'v':

            scores_dict_greedy = ReadScores("Greedy")
            scores_dict_random = ReadScores("Random")
            #scores_dict_hillclimber =
            #scores_dict_hillclimberSA =
            Calculator(scores_dict_greedy, scores_dict_random)
            choiceVisualisation = input("What kind of visualisation would you like? ")
            scores_dict = ReadScores(choiceAlgorithm)
            if choiceVisualisation == "CatPlot":
                CategoricalPlot(scores_dict)

            elif choiceVisualisation == "Graph":
                GraphPlot(scores_dict)

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

    print("Inputs are: Random, Greedy, Hillclimber or HillclimberSA.")
    choiceAlgorithm = input("Please specify which algorithm you want to use: ")

    if choiceAlgorithm == "Greedy":

        random_size = int(input("Please specify the number of times (integer) you want to run Greedy: "))
        start = time.time()
        for j in range(random_size):
            Greedy(j)
        scores_dict = scores_dict_returner_greedy()
        print(scores_dict)
        best_dienstvoering = max(scores_dict, key=scores_dict.get)
        highscore = scores_dict[best_dienstvoering]
        end = time.time()
        time = end - start
        print("id of best dienstvoering: ", best_dienstvoering, "| score: ", highscore, " | n = ", random_size, " | time elapsed (seconds) = ", time)
        WriteScores(scores_dict, choiceAlgorithm)
        ReadScores(choiceAlgorithm)


    elif choiceAlgorithm == "Random":

        random_size = int(input("Please specify the number of times (integer) you want to run Random: "))
        start = time.time()
        Random(random_size)
        scores_dict = scores_dict_returner_random()
        best_dienstvoering = max(scores_dict, key=scores_dict.get)
        highscore = scores_dict[best_dienstvoering]
        end = time.time()
        time = end - start
        print("id of best dienstvoering: ", best_dienstvoering, "| score: ", highscore, " | n = ", random_size, " | time elapsed (seconds) = ", time)
        WriteScores(scores_dict, choiceAlgorithm)
        ReadScores(choiceAlgorithm)

    elif choiceAlgorithm == "Hillclimber":
        hillclimber_size = int(input("Please specify the number of times (integer) you want to run Hillclimber: "))
        d, P, P_traject, MIN, MIN_traject = Random2(1)
        Hillclimber(d, hillclimber_size, P, P_traject, MIN, MIN_traject)
