from Classes.graph import *
from Classes.station import *
from main import *
import random

def Hillclimber(d, size, P, P_traject, MIN, MIN_traject):

    #print("Score oud:", d.score)
    #print("MIN_traject", MIN_traject)
    traject_array = [0,1,2,3,4,5,6]
    for i in range(size):
        #d2 = Dienstvoering(1)
        d2 = d
        change = random.choice(traject_array)
        #print("change:", change)

        #create traject object
        t = Traject(8)
        P_new = 0
        MIN_new = 0

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

        while (MIN_new < 120):

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
            MIN_new = MIN_new + int(next[1])
            if (MIN_new > 120):
                MIN_new = MIN_new - int(next[1])
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
                    P_new = P_new + 0.05
                #print(d.critical_visited)

            # Sets the new station as the current station e.g. ('Station A', '12')
            current = next

            # Sets the current stations' visited status to true in station_dict
            g.station_dict[current[0]].set_visited()



        # Prints all connections in the current traject
        #print("All stations visited: ")
        #print(t.connections_visited)
        #print("All critical connections: ")
        #print(d.critical_visited)
        #print("Number of critical connections visited: ")
        #print(len(d.critical_visited))
        MIN2 = MIN - MIN_traject[change] + MIN_new
        #print(MIN)
        #print(MIN2)
        P2 = P - P_traject[change] + P_new
        d2.trajects[change] = t
        score2 = (10000 * P2) - (7 * 20 + MIN2 / 10)
        print("score_rand:", d.score)
        print("score_hill:", score2)
        #print(d.trajects[change].connections_visited)
        #print(d2.trajects[change].connections_visited)
        print(t.connections_visited)
        if score2 > d.score:
            d = d2
            d.score = score2
        print("new score", d.score)
        return d
