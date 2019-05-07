from Classes.graph import *
from Classes.station import *
import random
from main import *

# Returns a random node/station from all the stations:
def randomizer():

    departure = random.choice(list(g.station_dict.items()))
    return departure

# Finds a specified number of random routes
def Random():

    # Specify the amount of runs
    for runs in range(1):


        # Initializes a Dienstvoering object to store the 7 trajects
        d = Dienstvoering(runs)

        # Specify the amount of routes
        for i in range(1):

            #create traject object
            t = Traject(i)
            MIN = 0
            counter = 0

            #choose random departure station
            current = random.choice(list(g.station_dict.items()))
            print("Departure: ")
            print(current)

            neighbors = g.station_dict[current[0]].adjacent
            neighbors_items = list(neighbors.items())
            current_station = current[0]
            g.station_dict[current_station].set_visited()
            print("The first: " + current_station)

            while (MIN < 120):

                neighbors = g.station_dict[current[0]].adjacent
                print(neighbors)
                unvisited_items = []

                for neighbor in neighbors.items():

                    visited = g.station_dict[neighbor[0]].get_visited()
                    print(visited)
                    print(neighbor)
                    if (visited == False):
                        unvisited_items.append(neighbor)

                if (len(unvisited_items) == 0):
                    break

                next = random.choice(unvisited_items)
                next_station = next[0]
                print(neighbors_items)
                print("Next stop: " + next_station)

                MIN = MIN + int(next[1])
                if (MIN > 120):
                    break

                current_station = current[0]
                t.fill_connections(counter, current_station, next_station)

                current = next
                g.station_dict[current[0]].set_visited()
                counter = counter + 1

            print(t.connections_visited)
