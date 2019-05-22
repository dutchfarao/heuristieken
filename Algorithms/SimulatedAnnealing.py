from Classes.graph import *
from Classes.station import *
from main import *
import random
import math
import copy

scores_list = {}

def MapChoice(mapchooser):

    mapChoice_list = []

    if mapchooser == 1:
        max_duration = 180
        critical_connections = 120
        traject_amount = 20
        mapChoice_list.append(max_duration)
        mapChoice_list.append(critical_connections)
        mapChoice_list.append(traject_amount)

    if mapchooser == 2:
        max_duration = 120
        critical_connections = 40
        traject_amount = 7
        mapChoice_list.append(max_duration)
        mapChoice_list.append(critical_connections)
        mapChoice_list.append(traject_amount)

    return mapChoice_list

def SetAppendingFunctionality(dienstvoering):

    # Initializes a set used to contain the critical visited connections
    critical_visited_set = {}
    critical_visited_set = set()
    critical_visited_set.clear()

    # Loops through all the trajects in the Dienstvoering
    for traject in dienstvoering.trajects.values():

        # Loops through all the visited critical connections in the Traject and appends them to a set
        for connection in traject.critical_visited_HC:
            critical_visited_set.add(connection)

    length = len(critical_visited_set)

    return length

def MinutesCalculator(dienstvoering):

    minutes = 0

    # Loops through all the trajects in the Dienstvoering
    for traject in dienstvoering.trajects.values():

        # Loops through all the visited critical connections in the Traject and appends them to a set
        minutes = minutes + traject.Min_traject

    return minutes

def SetScoreCalculator(length, minutes, dienstvoering, critical_connections, traject_amount):

    traject_cost = traject_amount * 20

    score = 10000 * (length / critical_connections) - (traject_cost + minutes / 10)
    return score

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

def DienstvoeringCopier(dienstvoering):

    temporary_dienstvoering = Dienstvoering(8)
    temporary_dienstvoering = copy.deepcopy(dienstvoering)

    return temporary_dienstvoering

def DecisionFunctionality(temperature, score_before, score_after, dienstvoering, temporary_dienstvoering, temporary_traject, random_t):

    temperature = temperature
    print("Entering DecisionFunctionality")
    # If the score of the Traject is an improvement
    if score_after >= score_before:

        print("The score was determined to be an improvement")
        # Adds the newly visited critical connections to the dienstvoering
        for row in dienstvoering.trajects[random_t].critical_visited_HC:
            dienstvoering.critical_visited_HC.append(row)

        # Removes all the first instances of the critical connections visited by the old (now replaced) Traject
        for row in temporary_traject.critical_visited_HC:
            dienstvoering.critical_visited_HC.remove(row)

        dienstvoering.set_score(score_after)

    # If the score is not an improvement

    if score_after < score_before and temperature is not 0:
        #calculate the change of acceptance
        chance = math.exp((score_after - score_before) / temperature)

        print("Chance is:", chance, "Random is: ", random.random())

             # accept the new score
        if random.random() < chance:
            print(random.random(), "This is again random")
            print("The score was NOT determined to be an improvement, but was accepted")
            # Adds the newly visited critical connections to the dienstvoering
            for row in dienstvoering.trajects[random_t].critical_visited_HC:
                dienstvoering.critical_visited_HC.append(row)

            # Removes all the first instances of the critical connections visited by the old (now replaced) Traject
            for row in temporary_traject.critical_visited_HC:
                dienstvoering.critical_visited_HC.remove(row)

            dienstvoering.set_score(score_after)

        else:
            print("The score was NOT determined to be an improvement and was not accepted")

            # Resets the random_t Traject to its old value
            dienstvoering = temporary_dienstvoering
            dienstvoering.dienstId = temporary_dienstvoering.dienstId
            dienstvoering.score = temporary_dienstvoering.score
            dienstvoering.trajects = temporary_dienstvoering.trajects
            dienstvoering.critical_visited = temporary_dienstvoering.critical_visited
            dienstvoering.critical_visited_HC = temporary_dienstvoering.critical_visited_HC



    # do not accept new score.
    # else:
    #     print("The score was NOT determined to be an improvement and was not accepted")
    #
    #     # Resets the random_t Traject to its old value
    #     dienstvoering = temporary_dienstvoering
    #     dienstvoering.dienstId = temporary_dienstvoering.dienstId
    #     dienstvoering.score = temporary_dienstvoering.score
    #     dienstvoering.trajects = temporary_dienstvoering.trajects
    #     dienstvoering.critical_visited = temporary_dienstvoering.critical_visited
    #     dienstvoering.critical_visited_HC = temporary_dienstvoering.critical_visited_HC

    return dienstvoering

def TrajectChooser(traject_amount):

    # Randomly selects one Traject in the Dienstvoering to swap
    array_minimal = []
    for i in range(traject_amount):
        array_minimal.append(i)

    value = random.choice(list(array_minimal))
    return value

def random_tResetter(dienstvoering, random_t):

    # Resetting the random_t Traject and returning it
    dienstvoering.trajects[random_t].time = 0
    dienstvoering.trajects[random_t].connections_visited.clear()
    dienstvoering.trajects[random_t].critical_visited.clear()
    dienstvoering.trajects[random_t].critical_visited_HC.clear()
    dienstvoering.trajects[random_t].K_traject = 0
    dienstvoering.trajects[random_t].Min_traject = 0
    return dienstvoering.trajects[random_t]

def RandomRoutingFunctionality(dienstvoering, random_t, max_duration):

    # Resets the counters used in the Random pathfinding loop
    MIN = 0.0
    counter = 0

    # Resets the station visited tracker
    for station in g.station_dict:
        g.station_dict[station].visited = False

    #choose random departure station in the form of: ('station' , <Classes.station.Station object>)
    current = random.choice(list(g.station_dict.items()))

    # Puts the adjecent nodes into neighbors_items
    neighbors = g.station_dict[current[0]].adjacent
    neighbors_items = list(neighbors.items())

    # Current Station as a string 'station', sets this station as visited in the station_dict
    current_station = current[0]
    g.station_dict[current_station].set_visited()

    while (MIN < max_duration):

        # Neighbors of the current station (departure) in the form of:
        # {'Station A': '12', 'Station B': '13', 'Station C': '7'}
        neighbors = g.station_dict[current[0]].adjacent

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

        # If there are no more unvisited nodes, stops the loop
        if (len(unvisited_items) == 0):
            break

        # Picks a random neighbor from unvisited_items
        # neighbor = ('Station A', '12')
        next = random.choice(unvisited_items)

        # Gets the name of the station as a String e.g. 'Station A'
        next_station = next[0]

        # Adds the amount of minutes the extra stop will take
        # If this amount adds up to more than 120, stops the loop
        MIN = MIN + float(next[1])

        if (MIN > max_duration):
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

    dienstvoering.trajects[random_t].Min_traject = MIN
    dienstvoering.trajects[random_t].time = MIN
    #print("NEW ROUTE: ")
    #print(dienstvoering.trajects[random_t].connections_visited)
    #print("___________________________________________________")

    return dienstvoering

def cooling_function(max_temp, iteration, max_iterations):
    """
     A logistic cooling function

    Input:
        max_temp: max temperature
        iteration:the number of iterations which have been done.
        max_iterations: maximum number of max_iterations.
    Returns:
         temperature.
    """
    # the function
    function = max_iterations / (1 + math.exp(-6 * iteration / max_iterations))
    # calculation of temp.
    temperature = 2 * (max_temp - function)

    return temperature


def SimulatedAnnealing(dienstvoering, iter, mapchooser):

    max_duration, critical_connections, traject_amount = 0, 0, 0
    mapChoice_list = MapChoice(mapchooser)
    max_duration = mapChoice_list[0]
    critical_connections = mapChoice_list[1]
    traject_amount = mapChoice_list[2]
    max_iterations = iter
    iteration = 0

    # Repeats the Hillclimber algorithm the desired amount of times
    for m in range(iter):

        # Calculates the length, duration and score of the Set before changing a random traject
        length_before = SetAppendingFunctionality(dienstvoering)
        minutes_before = MinutesCalculator(dienstvoering)
        score_before = SetScoreCalculator(length_before, minutes_before, dienstvoering, critical_connections, traject_amount)

        # Randomly selects one Traject in the Dienstvoering to swap
        random_t = TrajectChooser(traject_amount)
        # print("Random_t is: ")
        # print(random_t)

        # Initializes a new, temporary Traject and Dienstvoering object to store the values
        temporary_traject = TrajectCopier(dienstvoering, random_t)
        temporary_dienstvoering = DienstvoeringCopier(dienstvoering)

        # Resetting the minimal_t Traject
        dienstvoering.trajects[random_t] = random_tResetter(dienstvoering, random_t)

        # Calls the RandomRoutingFunctionality
        dienstvoering = RandomRoutingFunctionality(dienstvoering, random_t, max_duration)

        length_after = SetAppendingFunctionality(dienstvoering)
        minutes_after = MinutesCalculator(dienstvoering)
        score_after = SetScoreCalculator(length_after, minutes_after, dienstvoering, critical_connections, traject_amount)
        temperature = cooling_function(1000, iteration, max_iterations)

        dienstvoering = DecisionFunctionality(temperature, score_before, score_after, dienstvoering, temporary_dienstvoering, temporary_traject, random_t)

        # Calculates the total score of the dienstvoering
        final_score = dienstvoering.score
        print("Final Score")
        print(final_score)
        scores_list[m] = final_score
        iteration = iteration + 1


        print("---------------------------------------------------")
        print(scores_list)
        print("---------------------------------------------------")

    return dienstvoering
