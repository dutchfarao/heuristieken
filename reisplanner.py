from train import Train
from mainActivity import Station, Connection, connections, stations, load_stations, load_connections, INPUT_STATIONS, INPUT_CONNECTIONS
from pprint import pprint
from graph import Graph
from vertex import Vertex
import heapq
import sys

#fftesten

minutes = 0

# Makes the shortest path from v.previous
def shortest(v, path):
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

def dijkstra(aGraph, start, target):
    #print('Dijkstras shortest path')
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

        #return reistijd

if __name__ == "__main__":

    # Calling the CSV loading functions in mainActivity
    # These functions will also instantiate station and connections objects
    load_stations(INPUT_STATIONS)
    load_connections(INPUT_CONNECTIONS)

    g = Graph()

    for index in stations:
        g.add_vertex(stations[index].name)

    for counter in connections:
        g.add_edge(connections[counter].stat1, connections[counter].stat2, int(connections[counter].time))

    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            #print( vid, wid, v.get_weight(w))

    while True:
        startstation = input("Van: ").title()
        eindstation = input("Naar: ").title()
        if startstation not in stations:
            print(startstation, "is geen bestaand station")
            print("Bedoel je", startstation, "Centraal/Centrum?")
        elif eindstation not in stations:
            print(eindstation, "is geen bestaand station")
            print("Bedoel je", eindstation, "Centraal/Centrum?")
        else:
            break

    dijkstra(g, g.get_vertex(startstation), g.get_vertex(eindstation))

    target = g.get_vertex(eindstation)
    path = [target.get_id()]
    reistijd = int(target.get_distance())
    uren = 0
    shortest(target, path)
    print('Reisadvies: ' + str((path[::-1])))
    if reistijd > 60:
        print('Reistijd:',reistijd//60,'uur en',reistijd%60,'minuten')
    else:
        print('Reistijd:',reistijd,'minuten')
