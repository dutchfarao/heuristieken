from Classes.graph import *
from Classes.station import *
import random
from main import *

# Dictionary where all the scores will be saved
scores_dict = {}

# Finds a specified number of random routes
def Random(amount):
    
    # Specify the amount of runs
    for runs in range(amount):

        # Initializes a Dienstvoering object to store the 7 trajects
        d = Dienstvoering(runs)
        MIN = 0
        P = 0
        T = 0

        # Specify the amount of routes
        for i in range(7):

            #create traject object
            t = Traject(i)

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

                    #print(visited)
                    #print(neighbor)

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
                MIN = MIN + int(next[1])
                if (MIN > 120):
                    break

                # Sets the new station as the current station e.g. 'Station A'
                current_station = current[0]

                # Adds the new connection to the traject dictionary in dienstvoering
                # E.g. {0: ('Station A', 'Station B'), 1: ('Station B', Station C')}
                t.fill_connections(counter, current_station, next_station)

                # If either current_station or next_station is a critical Station
                # Calls the dienstvoering method fill_critical
                if (g.station_dict[current_station].critical == True or g.station_dict[next_station].critical == True):

                    if (d.get_critical_visited(current_station, next_station) == False):
                        d.fill_critical(current_station, next_station)
                        P = P + 0.05
                        #print(d.critical_visited)

                # Sets the new station as the current station e.g. ('Station A', '12')
                current = next

                # Sets the current stations' visited status to true in station_dict
                g.station_dict[current[0]].set_visited()

                # Increases the counter for the traject dictionary in dienstvoering
                counter = counter + 1

            # Prints all connections in the current traject
            #print("All stations visited: ")
            #print(t.connections_visited)
            #print("All critical connections: ")
            #print(d.critical_visited)
            #print("Number of critical connections visited: ")
            #print(len(d.critical_visited))
            d.trajects[i] = t
            T = T + 1

        #print("Trajects: ")
        #print(d.trajects)
        score = (10000 * P) - (T * 20 + MIN / 10)
        d.set_score(score)
        scores_dict[d.dienstId] = score

        print("scores_dict[d.dienstId]")
        print(scores_dict[d.dienstId])
        print("score")
        print(score)

    print(scores_dict)

def scores_dict_returner_random():
    return scores_dict
