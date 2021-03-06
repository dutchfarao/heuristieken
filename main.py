from HelperFunctions.CSVHelper import load_stations, load_connections, WriteScores, ReadScores
from Classes.dienstvoering import Dienstvoering
from Classes.traject import Traject
from Classes.graph import Graph
from Algorithms.greedy import Greedy, scores_dict_returner_greedy
from Algorithms.random import Random, scores_dict_returner_random
from Algorithms.HillClimber2 import Hillclimber2
from Algorithms.SimulatedAnnealing import SimulatedAnnealing
from HelperFunctions.VisualisationHelper import HistogramPlot, CategoricalPlot, BarPlot
from HelperFunctions.MapHelper import MapHelper
import time
import random

if __name__ == "__main__":

    scores_dict = {}
    data = {}
    mapchooser = 0

    # Allows the user to choose whether the Dienstregeling will be national or just for North and South Holland
    while True:
        choiceRegion = input("Dienstregeling voor heel Nederland (1) of Noord en Zuid Holland (2)? ")

        if choiceRegion not in ['1', '2']:
            print("Please enter 1 or 2.")
            continue
        else:
            break
        break

    if choiceRegion == "1":
        mapchooser = 1
        INPUT_CONNECTIONS = "Data/ConnectiesNationaal.csv"
        INPUT_STATIONS = "Data/StationsNationaal.csv"

    elif choiceRegion == "2":
        mapchooser = 2
        INPUT_CONNECTIONS = "Data/ConnectiesHolland.csv"
        INPUT_STATIONS = "Data/StationsHolland.csv"

    # Loads the data sources, after the user has selected the desired scope of the Dienstregeling
    load_stations(INPUT_STATIONS)
    load_connections(INPUT_CONNECTIONS)

    # Allows the user to choose between runnign algorithms or performing visualisations
    choiceAction = input("Would you like to run algorithms or perform visualisations? Press 'v' for visuals, otherwise just press ENTER")


    # If the user wants to perform visualisations
    if choiceAction == 'v':

        choiceAction = input("Would you like to do a Barplot, a Categoricalplot or a Histogramplot? Press 'b', 'c' or 'h'.")

        if mapchooser == 1:
            size = "NL"

        if mapchooser == 2:
            size = "NZH"

        # Reads the scores of the algortihms from the CSV file, and stores it in a dictionary
        scores_dict_random = ReadScores("Random" + size)
        scores_dict_greedy = ReadScores("Greedy" + size)
        scores_dict_hillclimber = ReadScores("Hillclimber" + size)
        scores_dict_SA = ReadScores("SimulatedAnnealing" + size)
        #temperatures = ReadScores("Temperatures" + size)

        # Runs five visualisations: A barplot compairing all algorithms, and one histogram for each algortihm seperatly
        if choiceAction == 'b':
            BarPlot(scores_dict_random, scores_dict_greedy, scores_dict_hillclimber, scores_dict_SA)

        if choiceAction == 'c':
            CategoricalPlot(scores_dict_hillclimber, scores_dict_SA)

        if choiceAction == 'h':

            HistogramPlot(scores_dict_random, "Random")
            HistogramPlot(scores_dict_greedy, "Greedy")
            HistogramPlot(scores_dict_hillclimber, "Hillclimber")
            HistogramPlot(scores_dict_SA, "Simulated Annealing")


    # Allows the user to choose which algorithm is ran
    print("Inputs are: Random (r), Greedy (g), Hillclimber(h) or Simulated Annealing (s).")

    while True:
        choiceAlgorithm = input("Please specify which algorithm you want to use: ")

        if choiceAlgorithm not in ['r', 'g', 'h', 's']:
            print("Please enter r, g, h or s.")
            continue
        else:
            break

    # If the user chooses Hillclimber
    if choiceAlgorithm == "h":

        # User has to input how many times both Random and Hillclimber are run
        while True:
            try:
                hillclimber2_size = int(input("Please specify the number of times (integer) you want to run HillClimber: "))
                break
            except ValueError:
                print("Please enter an positive integer.")
                continue
            break
        # Starts the time, for comparison purposes
        start = time.time()

        # Calls the Random algorithms the desired amount of times, and stores the results in dienstvoering_dict
        dienstvoering_dict = Random(1, mapchooser)
        dienstvoering_random = dienstvoering_dict[0]

        # Calls the HillClimber algorithm using the scores from the Random algorithm and stores the return values in scores_dictionary_HC
        dienstvoering_hillclimber = Hillclimber2(dienstvoering_random, hillclimber2_size, mapchooser)

        # Afterwards, the values of K are stored in K_dict
        K_dict = {}
        for row in dienstvoering_hillclimber.keys():
            K_dict[row] = dienstvoering_hillclimber[row].get_score()

        # Calculates the highest value of K returned from the Random algorithm
        best_dienstvoering = max(K_dict, key=K_dict.get)
        beste_dv = dienstvoering_hillclimber[best_dienstvoering]

        # Ends the timecounter and calculates running length of the algorithm
        end = time.time()
        time = end - start

        # Writes the scores from the Random algorithm called by HillClimber into a CSV file
        WriteScores(K_dict, "Hillclimber", 1, mapchooser)
        MapHelper(mapchooser, beste_dv)

    if choiceAlgorithm == "g":

        while True:
            try:
                greedy_size = int(input("Please specify the number of times (integer) you want to run Greedy: "))
                break
            except ValueError:
                print("Please enter an positive integer.")
                continue
            break

        #start timer
        start = time.time()

        #run greedy the specified amount of times
        for j in range(greedy_size):
            Greedy(j, mapchooser)

        #put scores of greedy in scores_dict
        scores_dict = scores_dict_returner_greedy()

        #choose best score
        best_dienstvoering = max(scores_dict, key=scores_dict.get)
        highscore = scores_dict[best_dienstvoering]

        #end timer and calculate time
        end = time.time()
        time = end - start

        #calculate average score
        average = sum(scores_dict.values()) / float(len(scores_dict))
        #print best score and other info
        print("id of best dienstvoering: ", best_dienstvoering, "| score: ", highscore, " | n = ", greedy_size, " | time elapsed (seconds) = ", time, " | average = ", average)

        #write scores
        WriteScores(scores_dict, "Greedy", 1, mapchooser)

    # If the user chooses the algorithm Random
    if choiceAlgorithm == "r":

        # User has to input how many times Random is run
        #random_size = int(input("Please specify the number of times (integer) you want to run Random: "))
        while True:
            try:
                random_size = int(input("Please specify the number of times (integer) you want to run Random: "))
                break
            except ValueError:
                print("Please enter an positive integer.")
                continue
            break
        # Starts the time, for comparison purposes
        start = time.time()

        # Calls the Random algorithms the desired amount of times, and stores the results in scores_dict
        scores_dict = Random(random_size, mapchooser)

        # Afterwards, the values of K are stored in K_dict
        K_dict = {}
        for row in scores_dict:
            K_dict[row] = scores_dict[row].get_score()

        # Calculates the highest value of K returned from the Random algorithm
        best_dienstvoering = max(K_dict, key=K_dict.get)
        highscore = K_dict[best_dienstvoering]
        beste_dv = scores_dict[best_dienstvoering]

        # Ends the timecounter
        end = time.time()
        time = end - start
        print("id of best dienstvoering: ", best_dienstvoering, "| score: ", highscore, " | n = ", random_size, " | time elapsed (seconds) = ", time)

        # Writes the scores from the Random algorithm into a CSV file
        WriteScores(K_dict, "Random", 1, mapchooser)

    # If the user chooses the algorithm Simulated Annealing
    if choiceAlgorithm == "s":

        # User has to input how many times both Random and Hillclimber are run
        while True:
            try:
                SA_size = int(input("Please specify the number of times (integer) you want to run Simulated Annealing: "))
                break
            except ValueError:
                print("Please enter an positive integer.")
                continue
            break

        # Starts the time, for comparison purposes
        start = time.time()

        # Calls the Random algorithms the desired amount of times, and stores the results in dienstvoering_dict
        dienstvoering_dict = Random(1, mapchooser)
        dienstvoering_random = dienstvoering_dict[0]

        # Calls the HillClimber algorithm using the scores from the Random algorithm and stores the return values in scores_dictionary_HC
        dienstvoering_SA = SimulatedAnnealing(dienstvoering_random, SA_size, mapchooser)

        # Afterwards, the values of K are stored in K_dict
        K_dict = {}
        for row in dienstvoering_SA.keys():
            K_dict[row] = dienstvoering_SA[row].get_score()

        # Calculates the highest value of K returned from the Random algorithm
        best_dienstvoering = max(K_dict, key=K_dict.get)
        beste_dv = dienstvoering_SA[best_dienstvoering]

        # Writes the scores from the Random algorithm called by HillClimber into a CSV file
        WriteScores(K_dict, "SimulatedAnnealing", 1, mapchooser)
        MapHelper(mapchooser, beste_dv)
