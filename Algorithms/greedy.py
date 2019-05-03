from Classes.graph import *
from Classes.station import *
from Classes.dienstvoering import *
from HelperFunctions.CSVHelper import *
import random

# Returns a random node/station from all the stations:
def Greedy():

    i = 0
    d = Dienstvoering(i)
    for i in (7):
        # create dientvoering object

        #choose random departure station
        departure = random.choice(list(g.station_dict.keys()))
        print(departure)
