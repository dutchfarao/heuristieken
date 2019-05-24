import csv
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
from Classes.graph import Graph
from Classes.dienstvoering import Dienstvoering
from main import *
import networkx as nx
import edges as e

def LabelPositionChanger(pos):

    pos_changed = {}
    y_off = 0.04 # offset on the y axis

    for k, v in pos.items():
        pos_changed[k] = (v[0], v[1] + y_off)

    return pos_changed

def NodeColorSetter(color_values):

    for station in g.station_dict.values():
        if station.critical == True:
            color_values.append('#a5330c')

        if station.critical == False:
            color_values.append('#ffffff')

    return color_values

def NodeAdder(G):

    values = []
    for station in g.station_dict.values():
        id = station.id
        latitude = station.xco
        longitude = station.yco
        G.add_node("" + id, pos = (float(latitude), float(longitude)))

    return G

def StationLoader():

    for station in g.station_dict.values():

        name_string = station.id
        length = len(name_string)
        first = name_string[0]
        middle = name_string[1]
        last = name_string[2]
        name = first + middle + last
        station.afkorting = name

def EdgeAdder(G):

    elist = []

    for station in g.station_dict.values():

        for key in station.adjacent.keys():
            elist.append((station.id, key, station.adjacent[key]))

    #print(elist)

    for edge in elist:

        print(edge)
        G.add_edge(edge[0], edge[1])

    return G

def EdgeAdderTrajects(G, dienstvoering, mapchooser):

    elist = []

    if mapchooser == 2:
        colours = ['b', 'g', 'r', 'c', 'm', 'y', 'k', '#880e4f', '#af90a1']

    elif mapchooser == 1:
        colours = ['b', 'g', 'r', 'c', 'm', 'y', 'k', '#880e4f', '#af90a1', '#b2adbd', '#aafaeb', '#b813d1', '#26eda3', '#d6c902', '#8c82cb', '#49599b', '#bde3da', '#c72c20', '#48057f', '#178f4b']

    counter = 0
    size = (counter + 1) * len(dienstvoering.trajects)

    for traject in dienstvoering.trajects.values():

        elist.clear()

        for train in traject.connections_visited.values():

            # print(train)
            elist.append((train[0], train[1]))

        for edge in elist:

            G.add_edge(edge[0], edge[1], color=colours[counter], weight=(size - counter))

        counter = counter + 1
        first = elist[0][0]
        length = len(elist) - 1
        last = elist[length][1]

        # print(first)
        # print(last)

    return G

def NodeTextAdderCritical(G):

    labels_critical = {}

    for station in g.station_dict.values():
        if station.critical == True:
            name = station.afkorting
            labels_critical[station.id] = station.afkorting

    return labels_critical

def NodeTextAdderNonCritical(G):

    labels_not_critical = {}

    for station in g.station_dict.values():

        if station.critical == False:

            name = station.afkorting
            labels_not_critical[station.id] = station.afkorting

    return labels_not_critical

def TrajectsCreator(NetworkXGraph, dienstvoering, mapchooser):

    NetworkXGraph = NodeAdder(NetworkXGraph)
    NetworkXGraph = EdgeAdderTrajects(NetworkXGraph, dienstvoering, mapchooser)

    color_values = []
    color_values = NodeColorSetter(color_values)

    labelsdictcritical = NodeTextAdderCritical(NetworkXGraph)
    labelsdictnoncritical = NodeTextAdderNonCritical(NetworkXGraph)

    pos=nx.get_node_attributes(NetworkXGraph,'pos')
    edges = NetworkXGraph.edges()
    colours = [NetworkXGraph[u][v]['color'] for u,v in edges]
    weights = [NetworkXGraph[u][v]['weight'] for u,v in edges]

    pos_changed = LabelPositionChanger(pos)

    fig,ax = plt.subplots(1, figsize = (7,12))
    nx.draw(NetworkXGraph, pos, edges=edges, node_color=color_values, edge_color = colours, node_size=70, width=weights)
    nx.draw_networkx_labels(NetworkXGraph, pos_changed, labels = labelsdictcritical, font_size=14, font_color='#ffb780')
    nx.draw_networkx_labels(NetworkXGraph, pos_changed, labels = labelsdictnoncritical, font_size=12, font_color='#80916b')
    # ax.legend(edges)
    plt.show()

def OverviewCreator(NetworkXGraph):

    # img = plt.imread("kaart.png")
    NetworkXGraph = NodeAdder(NetworkXGraph)
    NetworkXGraph = EdgeAdder(NetworkXGraph)

    color_values = []
    color_values = NodeColorSetter(color_values)

    labelsdictcritical = NodeTextAdderCritical(NetworkXGraph)
    labelsdictnoncritical = NodeTextAdderNonCritical(NetworkXGraph)

    pos=nx.get_node_attributes(NetworkXGraph,'pos')
    pos_changed = LabelPositionChanger(pos)
    fig,ax = plt.subplots(1, figsize = (8,11))
    # ax.imshow(img, extent=[5, 8, 50, 54])

    nx.draw(NetworkXGraph, pos, node_color=color_values, node_size=80)
    nx.draw_networkx_labels(NetworkXGraph, pos_changed, labels = labelsdictcritical, font_size=10, font_color='#381e1e')
    nx.draw_networkx_labels(NetworkXGraph, pos_changed, labels = labelsdictnoncritical, font_size=8, font_color='#381e1e')
    plt.show()

def MapHelper(mapchooser, dienstvoering):

    NetworkXGraph = nx.DiGraph()
    # NetworkXGraph = nx.Graph()
    StationLoader()

    Stringinput = input("Choose which plot to create: Overview or Trajects. ")

    if Stringinput == "Overview":

        OverviewCreator(NetworkXGraph)


    if Stringinput == "Trajects":
        TrajectsCreator(NetworkXGraph, dienstvoering, mapchooser)
