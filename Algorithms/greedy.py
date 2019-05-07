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
        #set visited True
        departure_station = g.get_station(departure)
        departure_station.set_visited()
        print("Beginstation is", departure)
        TOTAL_MIN = 0


        while (TOTAL_MIN < 120):
            #get adjacent stations and save the number of adjacent Stations
            neighbors = g.station_dict[departure].adjacent
            neighbors_keys = list(neighbors.keys())
            neighbors_items = list(neighbors.items())
            num_of_neighbors = len(neighbors)
            print("Mogelijke volgende stations zijn", neighbors)
            #get the current score from the dienstvoering
            current_score = int(d.get_score())
            #create score_dict, we'll use this to temporarely save the scores of each adjacent station
            score_dict = {}
            # check which 'neigbors have already been visited', if not, put neighbor in unvisited_items
            unvisited_items = []
            for neighbor in neighbors.keys():
                visited = g.get_station(neighbor).get_visited()
                if (visited == False):
                    unvisited_items.append(neighbor)

            if len(unvisited_items) == 0:
                break

                    #only look at the stations that are not yet visited for determination of destination
            for key in (unvisited_items):
                current_station = g.get_station(key)
                #set MIN, needed for calculation of score
                MIN = int((neighbors.get(key)))
                #check if neighbor is a critical station
                if current_station.get_critical() == True:
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
                    score_dict[key] = score
            #this is where the best destination is chosen
            destination = max(score_dict, key=score_dict.get)
            #upgrade time, but check if the new total won't exceed the maximum
            time_upgrade = int(neighbors.get(destination))
            TOTAL_MIN = TOTAL_MIN + time_upgrade
            if (TOTAL_MIN > 120):
                break
            #update station visited
            g.get_station(destination).set_visited()
            #update connections_visited in traject object
            t.fill_connections(i, departure, destination)
            #update critical_visited
            if g.get_station(destination).get_critical() or g.get_station(departure).get_critical() == True:
                #check if connection is already get_critical_visited
                critical_check = d.get_critical_visited(departure, destination)
                if critical_check == False:
                    d.fill_critical(departure, destination)
                else:
                    continue
            #set destination as new departure
            departure = destination
            #update score
            d.set_score(score)
            print("volgende station is", departure)
            print(score)
            








        print("TOTAL_MIN = ", TOTAL_MIN)
        print("Uiteindelijke score =", score )




        #wat ik nu wil gaan doen is kijken wat de hoogste score is in score_dict,
        #die selecteren en dan dat station toevoegen
        #aan stations_visited(in het traject object), critical_visited (in het dienstvoering object).
        #In het station object set_visited op True zetten. Score in dienstvoering object updaten.
