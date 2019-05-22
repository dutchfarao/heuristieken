from HelperFunctions.CSVHelper import *
from Classes.dienstvoering import *
from Classes.traject import *
from Classes.graph import Graph
from Algorithms.greedy import *
from Algorithms.random import *
from Algorithms.random2 import *
from Algorithms.hillclimber import *
from Algorithms.HillClimber2 import *
from Algorithms.SimulatedAnnealing import *
from HelperFunctions.VisualisationHelper import *
import time

if __name__ == "__main__":

    scores_dict = {}
    data = {}
    mapchooser = 0

    # Allows the user to choose between runnign algorithms or performing visualisations
    choiceAction = input("Would you like to run algorithms or perform visualisations? Press 'v' for visuals.")

    # If the user wants to perform visualisations
    if choiceAction == 'v':

            # Reads the scores of the algortihms from the CSV file, and stores it in a dictionary
            scores_dict_greedy = ReadScores("Greedy")
            scores_dict_random = ReadScores("Random")
            scores_dict_hillclimber_random = ReadScores("RandomHillClimber")
            scores_dict_hillclimber = ReadScores("RandomAfterHillClimber")

            # Runs five visualisations: A barplot compairing all algorithms, and one histogram for each algortihm seperatly
            BarPlot(scores_dict_greedy, scores_dict_random, scores_dict_hillclimber_random, scores_dict_hillclimber)
            HistogramPlot(scores_dict_random, "Random")
            HistogramPlot(scores_dict_greedy, "Greedy")
            HistogramPlot(scores_dict_hillclimber_random, "Hillclimber Random")
            HistogramPlot(scores_dict_hillclimber, "Hillclimber")

    # Allows the user to choose whether the Dienstregeling will be national or just for North and South Holland
    choiceRegion = input("Dienstregeling voor heel Nederland of Noord en Zuid Holland? ")

    if choiceRegion == "Nederland":
        mapchooser = 1
        INPUT_CONNECTIONS = "Data/ConnectiesNationaal.csv"
        INPUT_STATIONS = "Data/StationsNationaal.csv"

    else:
        mapchooser = 2
        INPUT_CONNECTIONS = "Data/ConnectiesHolland.csv"
        INPUT_STATIONS = "Data/StationsHolland.csv"

    # Loads the data sources, after the user has selected the desired scope of the Dienstregeling
    load_stations(INPUT_STATIONS)
    load_connections(INPUT_CONNECTIONS)

    # Allows the user to choose which algorithm is ran
    print("Inputs are: Random, Greedy, Hillclimber or Simulated Annealing (SA).")
    choiceAlgorithm = input("Please specify which algorithm you want to use: ")

    # If the user chooses Hillclimber
    if choiceAlgorithm == "Hillclimber":

        # User has to input how many times both Random and Hillclimber are run
        hillclimber2_size = int(input("Please specify the number of iterations (integer) you want to run HillClimber: "))

        # Starts the time, for comparison purposes
        start = time.time()

        # Calls the Random algorithms the desired amount of times, and stores the results in dienstvoering_dict
        dienstvoering_dict = Random(1, mapchooser)
        dienstvoering_random = dienstvoering_dict[0]

        # Calculates the highest value of K returned from the Random algorithm
        highscore = dienstvoering_random.get_score()
        print("Random score: ")
        print(highscore)

        # Writes the scores from the Random algorithm called by HillClimber into a CSV file
        WriteScores(dienstvoering_dict, "RandomHillClimber", 2)

        # Calls the HillClimber algorithm using the scores from the Random algorithm and stores the return values in scores_dictionary_HC
        dienstvoering_hillclimber = Hillclimber2(dienstvoering_random, hillclimber2_size, mapchooser)

        # Ends the timecounter and calculates running length of the algorithm
        end = time.time()
        time = end - start

        # Calculates the highest value of K returned from the HillClimber algorithm
        highscore = dienstvoering_hillclimber.get_score()
        print("Score after HC: ")
        print(highscore)

        # Writes the scores from the Random algorithm called by HillClimber into a CSV file
        WriteScores(highscore, "RandomAfterHillClimber", 3)

    if choiceAlgorithm == "Greedy":

        random_size = int(input("Please specify the number of times (integer) you want to run Greedy: "))
        start = time.time()
        for j in range(random_size):
            Greedy(j, mapchooser)
        scores_dict = scores_dict_returner_greedy()
        print(scores_dict)
        best_dienstvoering = max(scores_dict, key=scores_dict.get)
        highscore = scores_dict[best_dienstvoering]
        end = time.time()
        time = end - start
        average = sum(scores_dict.values()) / float(len(scores_dict))
        print("id of best dienstvoering: ", best_dienstvoering, "| score: ", highscore, " | n = ", random_size, " | time elapsed (seconds) = ", time, " | average = ", average)
        WriteScores(scores_dict, choiceAlgorithm, 1)
        ReadScores(choiceAlgorithm)


    # If the user chooses the algorithm Random
    if choiceAlgorithm == "Random":

        # User has to input how many times Random is run
        random_size = int(input("Please specify the number of times (integer) you want to run Random: "))

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

        # Ends the timecounter
        end = time.time()
        time = end - start
        print("id of best dienstvoering: ", best_dienstvoering, "| score: ", highscore, " | n = ", random_size, " | time elapsed (seconds) = ", time)

        # Writes the scores from the Random algorithm into a CSV file
        WriteScores(scores_dict, choiceAlgorithm, 2)
        ReadScores(choiceAlgorithm)


    if choiceAlgorithm == "SA" or "Simulated Annealing":

        # User has to input how many times both Random and Hillclimber are run
        SA_size = int(input("Please specify the number of iterations (integer) you want to run Simulated Annealing: "))

        # Starts the time, for comparison purposes
        start = time.time()

        # Calls the Random algorithms the desired amount of times, and stores the results in dienstvoering_dict
        dienstvoering_dict = Random(1, mapchooser)
        dienstvoering_random = dienstvoering_dict[0]

        # Calculates the highest value of K returned from the Random algorithm
        highscore = dienstvoering_random.get_score()
        print("Random score: ")
        print(highscore)

        # Writes the scores from the Random algorithm called by HillClimber into a CSV file
        WriteScores(dienstvoering_dict, "SimulatedAnnealing", 2)

        # Calls the HillClimber algorithm using the scores from the Random algorithm and stores the return values in scores_dictionary_HC
        dienstvoering_SA = SimulatedAnnealing(dienstvoering_random, SA_size, mapchooser)

        # Ends the timecounter and calculates running length of the algorithm
        end = time.time()
        time = end - start

        # Calculates the highest value of K returned from the HillClimber algorithm
        highscore = dienstvoering_SA.get_score()
        print("Score after Simulated Annealing: ")
        print(highscore)
