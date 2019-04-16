from train import Train
from mainActivity import Station, Connection, connections, stations, load_stations, load_connections, INPUT_STATIONS, INPUT_CONNECTIONS
from pprint import pprint
from graph import Graph
from vertex import Vertex
import heapq
import sys
import random

minutes = 0
criticalConnections = []

def utilityFunction(p, T, m):

    K = 10000 * (p / 20) - (T * 20 + m / 10)
    return K

def randomizer():
    departure = str(random.choice(criticalConnections))
    return departure

# Makes the shortest path from v.previous
def shortest(v, path):
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

# Actual pathfinding algorithm
def dijkstra(aGraph, start, target):
    print('Dijkstras shortest path')
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
                #print('updated : current = ' + current.get_id() + ' next = ' + next.get_id() + ' new_dist = ' + str(next.get_distance()))

            #else:
                #print('not updated : current = ' + current.get_id() + ' next = ' + next.get_id() + ' new_dist = ' + str(next.get_distance()))

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)

def randomRouter():
    T = 0
    p = 0
    m = 0

    # The amount of searches
    for i in range(10):

        for j in range(7):

            g = Graph()
            for index in stations:
                g.add_vertex(stations[index].name)

            # Adds edges for all the connections in the dictionary 'connections'
            for counter in connections:
                g.add_edge(connections[counter].stat1, connections[counter].stat2, int(connections[counter].time))

                # If the connection is critical, adds it to the list 'criticalConnections'
                if connections[counter].cc == True:
                    criticalConnections.append(connections[counter].stat1)

            start = randomizer()
            end = randomizer()

            if start == end:
                end = randomizer()

            dijkstra(g, g.get_vertex(start), g.get_vertex(end))
            target = g.get_vertex(end)
            path = [target.get_id()]
            shortest(target, path)
            print('The shortest path :' + str((path[::-1])))

            m = m + int(target.get_distance())
            T = T + 1
            print('T is: ' + str(T))
            print('m is: ' + str(m))

        K = utilityFunction(p, T, m)
        print('Value of K is: ' + str(K))
        print('----------------------------------')
        print('This is the: ' + str(i) + 'th run.')
        print('----------------------------------')
        p = 0
        T = 0
        m = 0

if __name__ == "__main__":

    # Calling the CSV loading functions in mainActivity
    # These functions will also instantiate station and connections objects
    load_stations(INPUT_STATIONS)
    load_connections(INPUT_CONNECTIONS)

    randomRouter()

    # User input for the start and end of the route
    #startstation = input("Van: ")
    #eindstation = input("Naar: ")
