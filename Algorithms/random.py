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

    d = Dienstvoering(0)

    # Specify the amount of routes
    for i in range(1):

        #create traject object
        t = Traject(i)
        MIN = 0

        #choose random departure station
        departure = random.choice(list(g.station_dict.keys()))
        print("Departure is: ")
        print(departure)
        neighbors = g.station_dict[departure].adjacent
        neighbors_keys = list(neighbors.keys())
        neighbors_items = list(neighbors.items())
        num_of_neighbors = len(neighbors)

        next_stop = random.choice(neighbors_items)
        print("First stop chosen is: ")
        MIN = int(next_stop[1])
        print(next_stop)
        print(MIN)

        while (MIN < 120):

            #get adjacent stations and save the number of adjacent Stations
            neighbors = g.station_dict[next_stop[0]].adjacent
            neighbors_keys = list(neighbors.keys())
            neighbors_items = list(neighbors.items())
            num_of_neighbors = len(neighbors)
            print(neighbors)
            #print(neighbors_keys)
            #print(neighbors_items)
            #print(num_of_neighbors)

            next_stop = random.choice(neighbors_items)
            print("Next stop chosen is: ")
            print(next_stop)
            MIN = MIN + int(next_stop[1])
            print(MIN)
