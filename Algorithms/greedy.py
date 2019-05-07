from Classes.graph import *
from Classes.station import *
from Classes.dienstvoering import *
from Classes.traject import *
from HelperFunctions.CSVHelper import *
import random

# Returns a random node/station from all the stations:
def Greedy():
    d = Dienstvoering(0)
    i = 0
    for i in range(1):
        #create traject object
        t = Traject(i)
        #choose random departure station
        departure = random.choice(list(g.station_dict.keys()))
        print(departure)
        #get adjacent stations and save the number of adjacent Stations
        neighbors = g.station_dict[departure].adjacent
        neighbors_keys = list(neighbors.keys())
        neighbors_items = list(neighbors.items())
        num_of_neighbors = len(neighbors)
        print(neighbors)
        print(neighbors_keys)
        print(num_of_neighbors)
        #get the current score from the dienstvoering
        current_score = int(d.get_score())
        #create score_dict, we'll use this to temporarely save the scores of each adjacent station
        score_dict = {}
        for key in (neighbors_keys):
            current_station = g.get_station(key)
            MIN = int((neighbors.get(key)))
            if current_station.get_critical() == True:
                print(current_station.get_id(), "is een kritiek station")
                #check if critical connection is already visited
                critical_check = d.get_critical_visited(departure, current_station)
                #if not, add 500 to score
                if critical_check == False:
                    score = current_score + 500 - MIN/10
                    score_dict[key] = score
                #else, just subtract minute amount
                if critical_check == True:
                    score = current_score - MIN/10
                    score_dict[key] = score

            else:
                #if not critical, just add minute amount
                score = current_score - MIN/10
                print(score)
                score_dict[key] = score

        #wat ik nu wil gaan doen is kijken wat de hoogste score is in score_dict,
        #die selecteren en dan dat station toevoegen
        #aan stations_visited(in het traject object), critical_visited (in het dienstvoering object).
        #In het station object set_visited op True zetten. Score in dienstvoering object updaten.
