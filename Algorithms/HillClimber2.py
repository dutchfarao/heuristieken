from Classes.graph import *
from Classes.station import *
from main import *
import random

def Hillclimber2(dienstvoering_dict_HC):

    # First, checks the length of dienstvoering_dict
    length = len(dienstvoering_dict_HC)
    #print("Dict:::")
    #print(dienstvoering_dict)
    dict_counter = 0

    #print("Before: ")
    #for row in dienstvoering_dict_HC:
        #print(dienstvoering_dict_HC[row].get_score())

    # For each dienstvoering:
    for dienstvoering in dienstvoering_dict_HC.values():

        #print("Dienstvoering: ")
        #print(dienstvoering)

        # Initializes a dictionary to store the increases in K of each Traject
        K_dict = {}

        # For each Traject in the dienstvoering:
        for traject in dienstvoering.trajects.values():

            # Adds all changes of each Traject in K to K_dict
            #print("Traject: ")
            #print(traject.K_traject)
            K_dict[traject.trajectId] = traject.K_traject

        # Checks which of the Trajects in K_dict is the lowest
        #print(K_dict)
        minimal_t = min(K_dict, key=K_dict.get)
        #print(minimal_t)

        # This is the dictionary containing all of the visited critical connections in the Dienstvoering
        #print("Before: ")
        #print(len(dienstvoering.critical_visited_HC))

        # This is the dictionary containing all of the visited critical connections in the Traject
        #print("Visited in minimal_t: ")
        #print(len(dienstvoering.trajects[minimal_t].critical_visited_HC))

        #print("Length after removing duplicates")
        Before_Critical_Visited_No_Duplicates = list(dict.fromkeys(dienstvoering.critical_visited_HC))
        length_before = len(Before_Critical_Visited_No_Duplicates)
        #print(length_before)

        # Removes all the first instances of the critical connections visited by the minimal_t Traject
        for row in dienstvoering.trajects[minimal_t].critical_visited_HC:
            dienstvoering.critical_visited_HC.remove(row)

        # Checks how many critical visited connections are left after removing those visited in minimal_t
        #print("After: ")
        #print(len(dienstvoering.critical_visited_HC))

        temporary = Traject(8)
        temporary = dienstvoering.trajects[minimal_t]
        # Calling the random function again for minimal_t
        # Resets the station visited tracker
        for station in g.station_dict:
            g.station_dict[station].visited = False

        min_before = dienstvoering.trajects[minimal_t].Min_traject

        # Resetting the minimal_t Traject
        dienstvoering.trajects[minimal_t].time = 0
        dienstvoering.trajects[minimal_t].connections_visited.clear()
        dienstvoering.trajects[minimal_t].critical_visited.clear()
        dienstvoering.trajects[minimal_t].critical_visited_HC.clear()
        dienstvoering.trajects[minimal_t].K_traject = 0
        dienstvoering.trajects[minimal_t].Min_traject = 0

        MIN = 0.0
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
            dienstvoering.trajects[minimal_t].fill_connections(counter, current_station, next_station)

            # If either current_station or next_station is a critical Station
            # Calls the dienstvoering method fill_critical
            #print(current_station)
            #print(next_station)

            if (g.station_dict[current_station].critical == True or g.station_dict[next_station].critical == True):
                dienstvoering.fill_critical_HC(current_station, next_station)
                dienstvoering.trajects[minimal_t].fill_critical_HC(current_station, next_station)

                # If the connection is not yet present in the Dienstvoering object
                #if (dienstvoering.get_critical_visited(current_station, next_station) == False):
                    #dienstvoering.fill_critical(current_station, next_station)
                    #dienstvoering.trajects[minimal_t].fill_critical(current_station, next_station)
                    #P = P + 0.05
                    #print("P Updated!")
                    #print(P)

            # Sets the new station as the current station e.g. ('Station A', '12')
            current = next

            # Sets the current stations' visited status to true in station_dict
            g.station_dict[current[0]].set_visited()

            # Increases the counter for the traject dictionary in dienstvoering
            counter = counter + 1

            #print("New Route: ")
            #print(dienstvoering.trajects[minimal_t].connections_visited)

        #print("Length of critical_visited_HC after: ")
        #print(len(dienstvoering.critical_visited_HC))
        #print(MIN)

        #print("Length after removing duplicates and adding new traject")
        After_Critical_Visited_No_Duplicates = list(dict.fromkeys(dienstvoering.critical_visited_HC))
        length_after = len(After_Critical_Visited_No_Duplicates)
        #print(length_after)
        difference_P = length_after - length_before
        difference_min = MIN - min_before
        #print(difference_P)
        #print(difference_min)
        score = difference_P * 250 - (difference_min / 10)
        #print("Score: ")
        #print(score)
        #print(dienstvoering_dict_HC[dict_counter].get_score())

        if score > 0:
            dienstvoering_dict_HC[dict_counter].trajects[minimal_t].K_traject = score
            dienstvoering_dict_HC[dict_counter].trajects[minimal_t].Min_traject = MIN
            dict_counter = dict_counter + 1

        else:
            dienstvoering_dict_HC[dict_counter].trajects[minimal_t] = temporary
            dict_counter = dict_counter + 1


    #print("After: ")
    for dv in dienstvoering_dict_HC:

        #print("Score from dienstvoering before adding up K")
        #print(dienstvoering_dict_HC[dv].get_score())

        #print("Scores by adding up K")
        Score_test = 0.0
        for tc in dienstvoering_dict_HC[dv].trajects:
            #score_test = Score_test + float(dienstvoering_dict_HC[dv].trajects[tc].K_traject)
            #print(dienstvoering_dict_HC[dv].trajects[tc].K_traject)
            Score_test = Score_test + dienstvoering_dict_HC[dv].trajects[tc].K_traject
            #print("Score test: ")
            #print(Score_test)

        dienstvoering_dict_HC[dv].set_score(Score_test)
        #print("Score from dienstvoering after adding up K")
        #print(dienstvoering_dict_HC[dv].get_score())

    return dienstvoering_dict_HC
