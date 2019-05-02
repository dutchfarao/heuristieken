from Classes.graph import *
from Classes.station import *
import random
from main import *

# Returns a random node/station from all the stations:
def randomizer():

    departure = random.choice(list(g.station_dict.items()))
    return departure

# Finds a specified number of random routes
def randomRouter(departure):
    # Specify the amount of routes
    for i in range(1):

        g.station_dict[departure].visited = True
        unvisited = []
        for j in g.station_dict[departure].adjacent.keys():
            print(j)
            #if g.station_dict[departure].adjecent[j].visited == False:
                #unvisited.append(g.station_dict[j])
