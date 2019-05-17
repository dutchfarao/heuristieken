from Classes.graph import *
from Classes.station import *
from main import *
import random

def TrajectCopier(dienstvoering, random_t):

    temporary = Traject(8)
    temporary.trajectId = dienstvoering.trajects[random_t].trajectId
    temporary.time = dienstvoering.trajects[random_t].time
    temporary.connections_visited = dienstvoering.trajects[random_t].connections_visited
    temporary.critical_visited = dienstvoering.trajects[random_t].critical_visited
    temporary.critical_visited_HC = dienstvoering.trajects[random_t].critical_visited_HC
    temporary.K_traject = dienstvoering.trajects[random_t].K_traject
    temporary.Min_traject = dienstvoering.trajects[random_t].Min_traject

    return temporary

def CorrectnessChecker(dienstvoering):

    print("Scores of all trajects: ")
    for traject in dienstvoering.trajects.values():
        print(traject.K_traject)

def K_trajectSumFunctionality(dienstvoering):

    K_temporary = 0.0
    for traject in dienstvoering.trajects.values():

        #print("Value of K_traject")
        #print("Traject number:")
        #print(traject.trajectId)
        #print(traject.K_traject)
        K_temporary = K_temporary + traject.K_traject

    dienstvoering.set_score(K_temporary)

    return K_temporary

def DecisionFunctionality(score, MIN, dienstvoering, temporary, random_t, score_before):

    print("Entering DecisionFunctionality")
    # If the score of the Traject is an improvement
    if score > 0:

        #print("score_before:")
        #print(score_before)
        #print("score")
        #print(score)
        score = score
        # Sets the values of K_traject and Min_traject to their new values
        dienstvoering.trajects[random_t].K_traject = score
        dienstvoering.trajects[random_t].Min_traject = MIN

        print("The score was determined to be an improvement")
        print("The score is: ")
        print(score)

        # Adds the newly visited critical connections to the dienstvoering
        for row in dienstvoering.trajects[random_t].critical_visited_HC:
            dienstvoering.critical_visited_HC.append(row)

        # Removes all the first instances of the critical connections visited by the old (now replaced) Traject
        for row in temporary.critical_visited_HC:
            dienstvoering.critical_visited_HC.remove(row)


    # If the score is not an improvement
    else:

        score = score
        print("The score was NOT determined to be an improvement")
        print("The score is: ")
        print(score)

        # Resets the random_t Traject to its old values
        dienstvoering.trajects[random_t] = temporary
        print("Score of the temporary traject placeholder: ")
        print(temporary.K_traject)

    return dienstvoering

def TrajectChooser():

    # Randomly selects one Traject in the Dienstvoering to swap
    array_minimal = [0, 1, 2, 3, 4, 5, 6]
    value = random.choice(list(array_minimal))
    return value

def DuplicateRemover(input):

    # Removes all duplicate critical connections visited in the Dienstvoering's critical_visited_HC
    Before_Duplicate_removal = input
    Before_Critical_Visited_No_Duplicates = list(dict.fromkeys(Before_Duplicate_removal))
    #print("Duplicateremover")
    #print(value)
    return Before_Critical_Visited_No_Duplicates

def random_tResetter(dienstvoering, random_t):

    # Resetting the random_t Traject and returning it
    dienstvoering.trajects[random_t].time = 0
    dienstvoering.trajects[random_t].connections_visited.clear()
    dienstvoering.trajects[random_t].critical_visited.clear()
    dienstvoering.trajects[random_t].critical_visited_HC.clear()
    dienstvoering.trajects[random_t].K_traject = 0
    dienstvoering.trajects[random_t].Min_traject = 0
    return dienstvoering.trajects[random_t]

def RandomRoutingFunctionality(dienstvoering, random_t):

    # Resets the counters used in the Random pathfinding loop
    MIN = 0.0
    counter = 0

    # Resets the station visited tracker
    for station in g.station_dict:
        g.station_dict[station].visited = False

    #choose random departure station in the form of: ('station' , <Classes.station.Station object>)
    current = random.choice(list(g.station_dict.items()))
    print("Current: ")
    print(current)

    # Puts the adjecent nodes into neighbors_items
    neighbors = g.station_dict[current[0]].adjacent
    neighbors_items = list(neighbors.items())
    print("neighbors_items")
    print(neighbors_items)

    # Current Station as a string 'station', sets this station as visited in the station_dict
    current_station = current[0]
    g.station_dict[current_station].set_visited()

    while (MIN < 120):

        # Neighbors of the current station (departure) in the form of:
        # {'Station A': '12', 'Station B': '13', 'Station C': '7'}
        neighbors = g.station_dict[current[0]].adjacent
        print("neighbors")
        print(neighbors)

        # Declare a list of unisited stations
        unvisited_items = []

        # For each object in neighbors
        for neighbor in neighbors.items():

            # Returns True or False on the current object from neighbors
            visited = g.station_dict[neighbor[0]].get_visited()

            # If visited equals False, adds that neighbor to unvisited stations in the form
            # neighbor = ('Station A', '12')
            if (visited == False):
                unvisited_items.append(neighbor)

        print("unvisited_items")
        print(unvisited_items)

        # If there are no more unvisited nodes, stops the loop
        if (len(unvisited_items) == 0):
            break

        # Picks a random neighbor from unvisited_items
        # neighbor = ('Station A', '12')
        next = random.choice(unvisited_items)

        # Gets the name of the station as a String e.g. 'Station A'
        next_station = next[0]

        print("next_station")
        print(next_station)

        # Adds the amount of minutes the extra stop will take
        # If this amount adds up to more than 120, stops the loop
        MIN = MIN + float(next[1])
        print("MIN")
        print(MIN)

        if (MIN > 120):
            break

        # Sets the new station as the current station e.g. 'Station A'
        current_station = current[0]

        # Adds the new connection to the traject dictionary in dienstvoering
        # E.g. {0: ('Station A', 'Station B'), 1: ('Station B', Station C')}
        dienstvoering.trajects[random_t].fill_connections(counter, current_station, next_station)
        counter = counter + 1

        # If either current_station or next_station is a critical Station
        # Calls the dienstvoering method fill_critical
        if (g.station_dict[current_station].critical == True or g.station_dict[next_station].critical == True):
            dienstvoering.fill_critical_HC(current_station, next_station)
            dienstvoering.trajects[random_t].fill_critical_HC(current_station, next_station)

        # Sets the new station as the current station e.g. ('Station A', '12')
        current = next

        # Sets the current stations' visited status to true in station_dict
        g.station_dict[current[0]].set_visited()

    dienstvoering.trajects[random_t].time = MIN
    print("NEW ROUTE: ")
    print(dienstvoering.trajects[random_t].connections_visited)
    print("___________________________________________________")

    return dienstvoering

def Hillclimber2(dienstvoering, iter):

    # Initializes a dictionary to store the increases in K of each Traject
    K_dict = {}

    # Repeats the Hillclimber algorithm the desired amount of times
    for m in range(iter):

        CorrectnessChecker(dienstvoering)

        # Initializes a dictionary to store the increases in K of each Traject
        K_dict.clear()

        # For each Traject in the dienstvoering:
        for traject in dienstvoering.trajects.values():

            # Adds all changes of each Traject in K to K_dict
            K_dict[traject.trajectId] = traject.K_traject

        # Randomly selects one Traject in the Dienstvoering to swap
        random_t = TrajectChooser()
        print(random_t)
        print("OLD ROUTE: ")
        print(dienstvoering.trajects[random_t].connections_visited)
        print("____________________________________________")
        #print("-------------------------------------------------")
        #print("The score of the chosen traject is: ")
        #print(dienstvoering.trajects[random_t].K_traject)
        #print("-------------------------------------------------")

        #This is a list containing all of the visited critical connections (including duplicates) in the Dienstvoering
        temporary_dienstvoering_before = dienstvoering.critical_visited_HC
        print("Dienstvoering.critical_visited_HC")
        print(len(dienstvoering.critical_visited_HC))
        print(dienstvoering.critical_visited_HC)
        print("_______________________________________________")
        print("temporary_dienstvoering_before")
        print(len(temporary_dienstvoering_before))
        print(temporary_dienstvoering_before)
        print("_______________________________________________")

        print("dienstvoering.trajects[random_t].critical_visited_HC")
        print(len(dienstvoering.trajects[random_t].critical_visited_HC))
        print(dienstvoering.trajects[random_t].critical_visited_HC)
        print("_______________________________________________")


        # Removes all the first instances of the critical connections visited by the random_t Traject
        for row in dienstvoering.trajects[random_t].critical_visited_HC:
            temporary_dienstvoering_before.remove(row)

        print("temporary_dienstvoering_before after removing first instances")
        print(len(temporary_dienstvoering_before))
        print(temporary_dienstvoering_before)
        print("_______________________________________________")

        # Calls DuplicateRemover
        temporary_dienstvoering_before = DuplicateRemover(temporary_dienstvoering_before)
        length_before = len(temporary_dienstvoering_before)

        print("temporary_dienstvoering_before after removing duplicates")
        print(len(temporary_dienstvoering_before))
        print(temporary_dienstvoering_before)
        print("_______________________________________________")

        # Initializes a new, temporary Traject object to store the values of the randomly chosen Traject
        temporary = TrajectCopier(dienstvoering, random_t)

        # Stores the amount of minutes the random_t Traject took
        min_before = dienstvoering.trajects[random_t].Min_traject
        score_before = dienstvoering.trajects[random_t].K_traject

        # Resetting the minimal_t Traject
        dienstvoering.trajects[random_t] = random_tResetter(dienstvoering, random_t)

        # Calls the RandomRoutingFunctionality
        dienstvoering = RandomRoutingFunctionality(dienstvoering, random_t)
        temporary_dienstvoering_after = dienstvoering.critical_visited_HC
        print("temporary_dienstvoering_after after running RandomRoutingFunctionality")
        print(len(temporary_dienstvoering_after))
        print(temporary_dienstvoering_after)
        print("_______________________________________________")

        # Calls DuplicateRemover and looks up the new duration of the new traject
        temporary_dienstvoering_after = DuplicateRemover(temporary_dienstvoering_after)
        print("temporary_dienstvoering_after after running RandomRoutingFunctionality and after removing duplicates")
        print(len(temporary_dienstvoering_after))
        print(temporary_dienstvoering_after)
        print("_______________________________________________")

        length_after = len(temporary_dienstvoering_after)
        minutes_after = dienstvoering.trajects[random_t].time

        # Calculates the new values of P and Min
        difference_P = length_after - length_before
        difference_min = min_before - minutes_after
        print("difference_P")
        print(difference_P)

        # Calculates the new potential score and calls DecisionFunctionality with this score
        score_t = 10000 * (difference_P / 40) - (difference_min / 10)
        dienstvoering = DecisionFunctionality(score_t, minutes_after, dienstvoering, temporary, random_t, score_before)

        # Calculates the total score of the dienstvoering
        final_score = K_trajectSumFunctionality(dienstvoering)

    return dienstvoering
