from train import Train
from mainActivity import Station, Connection, connections, stations, load_stations, load_connections, INPUT_STATIONS, INPUT_CONNECTIONS
from pprint import pprint
from Dijkstra_graph import Graph
from Dijkstra_vertex import Vertex
from score import Score
import heapq
import sys
import random

# A program which when ran, will call on mainActivity.py to load two CSV files containing stations and connections.
# It will then, i amount of times, randomly select, seven times, a starting and ending station. It will use Dijkstra's algorithm
# to calculate the fastest route between these two stations. It will, i amount of times, calculate K, which is a value used to express
# how 'good' a particular set of seven routes is. For each i, it will write the total K after seven runs, and the number i, to a CSV file.


minutes = 0
Connections = []
ccStartEnd = []
visitedCriticalConnections = []
results = {}

# Returns a random node/station from all the stations
def randomizer():

    departure = str(random.choice(Connections))
    return departure

# Loads all critical connections into a list, in order to check if a connections from the randomRouter is critical
def criticalConnectionLoader():

    for counter in connections:
        if connections[counter].cc == True:
            cc = str(connections[counter].stat1) + str(connections[counter].stat2)
            reversedcc = str(connections[counter].stat2) + str(connections[counter].stat1)
            ccStartEnd.append(cc)
            ccStartEnd.append(reversedcc)

# Makes the shortest path from v.previous
def shortest(v, path):

    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

# Calls the resultsWriter function, which writes the results (run, K) to the location specified earlier
def resultsWriter(results):

    for key in results.keys():
        run = key
        K = results[key]
        row = str(run) + ',' + str(K) + '\n'
        csv.write(row)

# Actual pathfinding algorithm
def dijkstra(aGraph, start, target):

    # Set the distance for the start node to zero
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        #for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)

            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)

# Implements the randomRouter function, which will write j amount of times a collections of 7 routes between
# two random nodes. The function will then return the K associated with each particular collection of routes
# and will write it to a CSV file
def randomRouter():

    # Sets all the variables used in the calculation of K to zero
    T = 0
    p = 0
    m = 0
    minutelist = {}

    # for each connection, adds both nodes to the list 'Connections'
    for counter in connections:
        Connections.append(connections[counter].stat1)
        Connections.append(connections[counter].stat2)

    # The amount of times a K will be calculated (by creating a colleciton of 7 random routes)
    for i in range(400):

        # Specify the maximum amount of 'Trains' / 'Schedules'
        criticalConnectionLoader()
        for j in range(7):

            # Initialize a new Graph object
            g = Graph()

            # Adds nodes for all stations
            for index in stations:
                g.add_vertex(stations[index].name)

            # Adds edges for all the connections in the dictionary 'connections'
            for counter in connections:
                g.add_edge(connections[counter].stat1, connections[counter].stat2, int(connections[counter].time))

            # Calls the randomizer function to generate a random start and endpoint
            start = randomizer()
            end = randomizer()

            # If the start and the endpoint are equal, calls randomizer again
            if start == end:
                end = randomizer()

            # Calls Dijkstra's algortihm using the start and endpoint
            dijkstra(g, g.get_vertex(start), g.get_vertex(end))
            target = g.get_vertex(end)
            path = [target.get_id()]
            shortest(target, path)

            # Reverses the dijkstra's shortest path, so that it is displayed from start to finish
            path.reverse()

            # For each node in the chosen route (except the final station)
            for k in range(len(path) - 1):

                # Assigns the start and end of a connection k to first and second
                l = k + 1
                first = path[k]
                second = path[l]

                # Creates two variables which contain both directions of the connection
                route = first + second
                routeReversed = second + first

                # For every entry in ccStartEnd
                for z in range(len(ccStartEnd)):

                    # if the connection k is contained in ccStartEnd (i.e. if the connection k is critical)
                    if route == ccStartEnd[z]:

                        # Adds both directions of the connection to visitedCriticalConnections
                        visitedCriticalConnections.append(route)
                        visitedCriticalConnections.append(routeReversed)

            # Used to remove duplicates from visitedCriticalConnections
            lister = set(visitedCriticalConnections)
            result = list(lister)
            number = len(result)

            # Used to calculate the variables used for calculating K
            m = m + int(target.get_distance())
            minutelist[j] = int(target.get_distance())
            T = T + 1
            p = ((number / 2) / 20)

        # Prints the total utility (K) of this particular set of schedules
        # Adds this score K, along with the 'run number (i)' to the dictionary
        # Resets the utility functions' parameters
        score = Score(p, m, T)
        score.set_K()
        K = score.get_score()
        print(K)
        results[i] = K

        # Deletes the i'th entry in the dictionary if any of the routes in that entry are longer than 120 minutes
        for index in minutelist.keys():
            if minutelist[index] > 120:
                print("One route in this collection is longer than 120 minutes.")
                del results[i]

        print('This is the: ' + str(i) + 'th run.')
        print('----------------------------------')
        p = 0
        T = 0
        m = 0
        visitedCriticalConnections.clear()
        criticalConnectionLoader()

    # Calls on the resultWriter functionality to write the i results to a CSV file
    resultsWriter(results)

if __name__ == "__main__":

    # Calling the CSV loading functions in mainActivity
    # These functions will also instantiate station and connections objects
    load_stations(INPUT_STATIONS)
    load_connections(INPUT_CONNECTIONS)

    # Location where the results will be saved (in CSV format)
    save_location = "DijkstraRandomResults.csv"
    csv = open(save_location, "w")
    columnTitleRow = "run, K\n"
    csv.write(columnTitleRow)

    # Calls the randomRouter function
    randomRouter()
