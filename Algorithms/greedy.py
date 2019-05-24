from Classes.graph import Graph
from Classes.station import Station
from Classes.dienstvoering import Dienstvoering
from Classes.traject import Traject
from HelperFunctions.CSVHelper import g
import random

scores_dict = {}

def MapChoice(mapchooser):
    """
     A function that sets the map chosen

    Input:
        mapchooser: an integer, NL is 1, N/Z Holland is 2
    Returns:
         mapChoice_list: a list that sets variables later used for calculation of score
    """
    #create empty list
    mapChoice_list = []

    if mapchooser == 1:
        max_duration = 180
        critical_connections = 120
        traject_amount = 20
        #fill list
        mapChoice_list.append(max_duration)
        mapChoice_list.append(critical_connections)
        mapChoice_list.append(traject_amount)

    if mapchooser == 2:
        max_duration = 120
        critical_connections = 40
        traject_amount = 7
        #fill list
        mapChoice_list.append(max_duration)
        mapChoice_list.append(critical_connections)
        mapChoice_list.append(traject_amount)

    return mapChoice_list

# Returns a random node/station from all the stations:
def Greedy(id, mapchooser):

    """
 The Greedy algorithm
    Input:
        mapchooser: an integer, NL is 1, N/Z Holland is 2
        id: an integer ranging from 0 to chosen number of iterations
        """
    max_duration, critical_connections, traject_amount = 0, 0, 0
    #mapchoser: Nederland = 1, nood/zuid holland = 2
    mapChoice_list = MapChoice(mapchooser)
    max_duration = mapChoice_list[0]
    critical_connections = mapChoice_list[1]
    traject_amount = mapChoice_list[2]

    #create dienstvoering, set minutes and i to 0
    d = Dienstvoering(id)
    Dienstvoering_MIN = 0
    i = 0

    for i in range(traject_amount):
        #create traject object
        t = Traject(i)
        #set all 'visited' at at the beginning of each new traject False
        for station in list(g.station_dict.keys()):
            station_reset = g.get_station(station)
            station_reset.visited = False


        #choose random departure station
        departure = random.choice(list(g.station_dict.keys()))
        departure_station = g.get_station(departure)

        while departure_station.critical == True:
            departure = random.choice(list(g.station_dict.keys()))
            departure_station = g.get_station(departure)
            if departure_station.critical == False:
                break



        #print(departure)
        #set visited True
        departure_station = g.get_station(departure)
        departure_station.set_visited()
        #print("Beginstation is", departure)
        TOTAL_MIN = 0


        while (TOTAL_MIN < max_duration):
            #get adjacent stations and save the number of adjacent Stations
            neighbors = g.station_dict[departure].adjacent
            neighbors_keys = list(neighbors.keys())
            neighbors_items = list(neighbors.items())
            num_of_neighbors = len(neighbors)

            #get the current score from the dienstvoering
            current_score = int(d.get_score())
            #create score_dict, we'll use this to temporarely save the scores of each adjacent station
            score_dict = {}
            score_dict1 = {}

            # check which 'neigbors have already been visited', if not, put neighbor in unvisited_items
            unvisited_items = []
            for neighbor in neighbors.keys():
                visited = g.get_station(neighbor).get_visited()
                if (visited == False):
                    unvisited_items.append(neighbor)
            #remove stations that are to far from options.
            for neighbor in unvisited_items:
                time_upgrade = float(neighbors.get(neighbor))
                if (TOTAL_MIN + time_upgrade) > max_duration:
                    unvisited_items.remove(neighbor)

            #stop the traject if there are no more options
            if len(unvisited_items) == 0:
                break

            #only look at the stations that are not yet visited and not too far for determination of destination
            for key in (unvisited_items):
                current_station = g.get_station(key)
                #set MIN, needed for calculation of score
                MIN = float((neighbors.get(key)))

                #do this for noord/zuid holland
                if max_duration == 120:
                    #check if neighbor or current_station is a critical station
                    departure_station = g.get_station(departure)
                    if current_station.get_critical() or departure_station.get_critical() == True:
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

                if max_duration == 180:
                    #check if neighbor or current_station is a critical station
                    departure_station = g.get_station(departure)
                    if current_station.get_critical() or departure_station.get_critical() == True:
                        #check if critical connection is already visited
                        critical_check = d.get_critical_visited(departure, current_station)
                        #if not, add 500 to score
                        if critical_check == False:
                            score = (current_score + 166.67) - MIN/10
                            score_dict1[key] = score
                            #else, just subtract minute amount
                        if critical_check == True:
                            score = current_score - MIN/10
                            score_dict1[key] = score

                    else:
                        #if not critical, just add minute amount
                        score = current_score - MIN/10
                        score_dict1[key] = score


                    #this is where the best destination is chosen
                    destination = max(score_dict1, key=score_dict1.get)


            #upgrade time, but check if the new total won't exceed the maximum
            time_upgrade = float(neighbors.get(destination))
            #print(time_upgrade)
            TOTAL_MIN = TOTAL_MIN + time_upgrade

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
            i + 1
            Dienstvoering_MIN = Dienstvoering_MIN + TOTAL_MIN

    #compensate for T, this is 7*20 for noord/zuid holland and 7*20 for Nederland
    if mapchooser == 2:
        score = score - 120
    if mapchooser == 1:
        score = score - 400
    
    #add score to scores_dict
    scores_dict[d.dienstId] = score
    print("---------------------------------------------------")
    print(scores_dict)
    print("---------------------------------------------------")


def scores_dict_returner_greedy():
    """
     A simple method that to return score_dict in main

    Returns:
         scores_dict: a dict of scores produced by greedy.
    """
    return scores_dict
