from Classes.graph import Graph
from Classes.station import Station
from Classes.dienstvoering import Dienstvoering
from Classes.traject import Traject
from HelperFunctions.CSVHelper import g
import random


# Dictionary where all the scores will be saved
scores_dict = {}
minutes = []

def TrajectSetter(d, traject, K_traject, Min_traject):

    """
     Sets the values of a traject object to certain values

    Input:
        d: A dienstvoering object, the current dienstvoering
        traject: The current traject object
        K_traject: A float, the value of K for the current traject
        Min_traject: A float, the length in minutes of the current traject
    Returns:
         d.trajects[traject]: A traject object, with updated values for K and Minutes
    """

    d.trajects[traject].K_traject = K_traject
    d.trajects[traject].Min_traject = Min_traject
    return d.trajects[traject]

def K_trajectCalculator(length_before, length_after, MIN, critical_connections):

    """
     Calculates the value of K for a certain traject

    Input:
        length_before: An integer, representing the length of the list containing all the visited critical connections in the dienstvoering
        length_after: An integer, representing the length of the list containing all the visited critical connections in the dienstvoering after the new traject has been made
        MIN: A float, the amount of minutes the traject takes to complete
        critical_connections: An integer, the maximum amount of critical connections that can be visited in the dienstvoering
    Returns:
         K: An integer, representing the score of a certain traject
    """

    difference_length = length_after - length_before
    K = 10000 * (difference_length / critical_connections) - (20 + MIN / 10)

    return K

def K_trajectSumFunctionality(dienstvoering):

    """
    Adds all the values of K of each traject in a dienstvoering together

    Input:
        dienstvoering: A dienstvoering object
    Returns:
         K_temporary: An integer, representing the score of all trajects in a dienstvoering added together
    """

    K_temporary = 0.0
    for traject in dienstvoering.trajects.values():

        K_temporary = K_temporary + traject.K_traject

    return K_temporary

def MinutesCalculator(dienstvoering):

    """
    Caulculates the total amount of minutes all trajects in a dienstvoering take

    Input:
        A dienstvoering object
    Returns:
         minutes: An integer representing the length of the dienstvoering in minutes
    """

    minutes = 0

    # Loops through all the trajects in the Dienstvoering
    for traject in dienstvoering.trajects.values():

        # Loops through all the visited critical connections in the Traject and appends them to a set
        minutes = minutes + traject.Min_traject

    return minutes

def DuplicateRemover(input):

    """
    Removes all the duplicates in a list

    Input:
        input: A list of visited critical connections containing duplicates
    Returns:
         Before_Critical_Visited_No_Duplicates: A list of visited critical connections, containing no duplicates
    """

    # Removes all duplicate critical connections visited in the Dienstvoering's critical_visited_HC
    Before_Duplicate_removal = input
    Before_Critical_Visited_No_Duplicates = list(dict.fromkeys(Before_Duplicate_removal))

    return Before_Critical_Visited_No_Duplicates

def MapChoice(mapchooser):

    """
     Sets variables based on which map is chosen by the user

    Input:
        mapchooser: An integer, 1 (for the Netherlands) or a 2 (for North and South Holland)
    Returns:
         mapChoice_list: A list containing the max_duration (180 / 120), the amount of critical_connections (120 / 40) and the maximum amount of trajects (7 / 20)
    """

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



# Finds a specified number of random routes
def Random(amount, mapchooser):

    """
    Finds a route between nodes (stations) subject to certain constraints
    Input:
        amount: An integer, representing the amount of Dienstvoeringen random will create
        mapchooser: An integer, 1 (for the Netherlands) or a 2 (for North and South Holland)
    Returns:
         scores_dict: A dictionary containing dienstvoering objects
    """

    max_duration, critical_connections, traject_amount = 0, 0, 0
    mapChoice_list = MapChoice(mapchooser)
    max_duration = mapChoice_list[0]
    critical_connections = mapChoice_list[1]
    traject_amount = mapChoice_list[2]

    # Specify the amount of runs
    for dienstvoering in range(amount):

        # Initializes a Dienstvoering object to store the 7 trajects
        d = Dienstvoering(dienstvoering)
        MIN_Traject = {}
        P_Traject = {}
        totalMinutes = 0.0
        MIN = 0.0
        P = 0.0
        T = 0
        P_old = 0.0
        minutes.clear()

        # Specify the amount of routes
        for traject in range(traject_amount):

            # print("_________")
            # print("Traject number: ")
            # print(traject)
            # print("_________")
            temporary = d.critical_visited_HC
            remove_duplicates = DuplicateRemover(temporary)
            length_before = len(remove_duplicates)

            #print("length_before after removing duplicates: ")
            #print(length_before)

            P_old = P
            #create traject object
            t = Traject(traject)
            d.trajects[traject] = t

            # Resets the station visited tracker
            for station in g.station_dict:
                g.station_dict[station].visited = False

            # Sets the minute and amount of stops in one traject counter to zero
            counter = 0

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
                #print(neighbors)

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

                if (MIN + float(next[1]) > max_duration):
                    break

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
                t.fill_connections(counter, current_station, next_station)

                # If either current_station or next_station is a critical Station
                # Calls the dienstvoering method fill_critical
                # print(current_station)
                # print(next_station)

                if (g.station_dict[current_station].critical == True or g.station_dict[next_station].critical == True):
                    d.fill_critical_HC(current_station, next_station)
                    t.fill_critical_HC(current_station, next_station)

                # Sets the new station as the current station e.g. ('Station A', '12')
                current = next

                # Sets the current stations' visited status to true in station_dict
                g.station_dict[current[0]].set_visited()

                # Increases the counter for the traject dictionary in dienstvoering
                counter = counter + 1

            temporary = d.critical_visited_HC
            remove_duplicates = DuplicateRemover(temporary)
            length_after = len(remove_duplicates)

            K_traject = K_trajectCalculator(length_before, length_after, MIN, critical_connections)
            min_traject = MIN

            t = TrajectSetter(d, traject, K_traject, min_traject)
            # print("Route taken: ")
            # print(t.connections_visited)
            # print("_________")
            # print("Minutes taken by traject: ")
            # print(min_traject)
            # print("_________")

            d.trajects[traject] = t
            T = T + 1
            minutes.append(MIN)
            MIN = 0

        # print("K dienstvoering")
        score = K_trajectSumFunctionality(d)
        d.set_score(score)
        d.minutes = MinutesCalculator(d)
        scores_dict[d.dienstId] = d
        # print(score)

    # print(scores_dict)
    return scores_dict

def scores_dict_returner_random():
    return scores_dict
