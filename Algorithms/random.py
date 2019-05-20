from Classes.graph import *
from Classes.station import *
import random
from main import *

# Dictionary where all the scores will be saved
scores_dict = {}
minutes = []

def TrajectSetter(d, traject, K_traject, Min_traject):

    d.trajects[traject].K_traject = K_traject
    d.trajects[traject].Min_traject = Min_traject
    return d.trajects[traject]

def LengthChecker(visited_hc):

    temporary_critical_visited = visited_hc
    length = len(temporary_critical_visited)
    return length

def K_trajectCalculator(length_before, length_after, MIN):

    difference_length = length_after - length_before
    K = 10000 * (difference_length / 40) - (20 + MIN / 10)

    #print("MIN: ")
    #print(MIN)
    print("K:")
    print(K)
    return K

def K_trajectSumFunctionality(dienstvoering):

    K_temporary = 0.0
    for traject in dienstvoering.trajects.values():

        K_temporary = K_temporary + traject.K_traject

    return K_temporary

def MinutesCalculator(dienstvoering):

    minutes = 0

    # Loops through all the trajects in the Dienstvoering
    for traject in dienstvoering.trajects.values():

        # Loops through all the visited critical connections in the Traject and appends them to a set
        minutes = minutes + traject.Min_traject

    return minutes

def DuplicateRemover(input):

    # Removes all duplicate critical connections visited in the Dienstvoering's critical_visited_HC
    Before_Duplicate_removal = input
    Before_Critical_Visited_No_Duplicates = list(dict.fromkeys(Before_Duplicate_removal))
    #print("Duplicateremover")
    #print(value)
    return Before_Critical_Visited_No_Duplicates

# Finds a specified number of random routes
def Random(amount):

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
        for traject in range(7):

            temporary = d.critical_visited_HC
            remove_duplicates = DuplicateRemover(temporary)
            length_before = LengthChecker(remove_duplicates)

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

            while (MIN < 120):

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

                if (MIN + float(next[1]) > 120):
                    break

                # Gets the name of the station as a String e.g. 'Station A'
                next_station = next[0]

                # Adds the amount of minutes the extra stop will take
                # If this amount adds up to more than 120, stops the loop
                MIN = MIN + float(next[1])
                if (MIN > 120):
                    break

                # Sets the new station as the current station e.g. 'Station A'
                current_station = current[0]

                # Adds the new connection to the traject dictionary in dienstvoering
                # E.g. {0: ('Station A', 'Station B'), 1: ('Station B', Station C')}
                t.fill_connections(counter, current_station, next_station)

                # If either current_station or next_station is a critical Station
                # Calls the dienstvoering method fill_critical
                #print(current_station)
                #print(next_station)

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
            length_after = LengthChecker(remove_duplicates)

            K_traject = K_trajectCalculator(length_before, length_after, MIN)
            min_traject = MIN

            t = TrajectSetter(d, traject, K_traject, min_traject)
            #print("Route taken: ")
            #print(t.connections_visited)

            d.trajects[traject] = t
            T = T + 1
            minutes.append(MIN)
            MIN = 0

        print("K dienstvoering")
        score = K_trajectSumFunctionality(d)
        d.set_score(score)
        d.minutes = MinutesCalculator(d)
        scores_dict[d.dienstId] = d
        print(score)

    print(scores_dict)
    return scores_dict

def scores_dict_returner_random():
    return scores_dict
