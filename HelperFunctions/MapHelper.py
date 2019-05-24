import csv
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
from Classes.graph import Graph
from Classes.dienstvoering import Dienstvoering
from HelperFunctions.CSVHelper import g
import networkx as nx

def LabelPositionChanger(pos):

    """
     Changes the position of labels by a certain offset

    Input:
        pos: A tuple, containing the values of a position as (x, y)

    Returns:
        pos_changed: A tuple, containing the values of a position as (x, y), now offset by a certain degree
    """

    pos_changed = {}
    y_off = 0.04

    for k, v in pos.items():
        pos_changed[k] = (v[0], v[1] + y_off)

    return pos_changed

def NodeColorSetter(color_values):

    """
     Changes the color of nodes depending on if they are critical or not

    Returns:
        color_values: A list, containing the colours of all nodes
    """

    for station in g.station_dict.values():
        if station.critical == True:
            color_values.append('#a5330c')

        if station.critical == False:
            color_values.append('#ffffff')

    return color_values

def NodeAdder(G):

    """
     Changes the position of labels by a certain offset

    Input:
        G: A DiGraph object, containing the values necessary to create a NetworkGraph
    Returns:
        G: A DiGraph object, containing the values necessary to create a NetworkGraph with values of new nodes added
    """

    values = []

    for station in g.station_dict.values():

        id = station.id
        latitude = station.xco
        longitude = station.yco
        G.add_node("" + id, pos = (float(latitude), float(longitude)))

    return G

def StationLoader():

    """
     Creates strings used for the labels on the nodes in the NetworkGraph, and adds those to the station objects

    Input:
        g: A graph object, containing (among other things) a station_dict containing all the stations used in the dienstvoering

    """

    for station in g.station_dict.values():

        name_string = station.id
        length = len(name_string)
        first = name_string[0]
        middle = name_string[1]
        last = name_string[2]
        name = first + middle + last
        station.afkorting = name

def EdgeAdder(G):

    """
     Adds edges to a NetworkGraph object

    Input:
        G: A DiGraph object, containing the values necessary to create a NetworkGraph
    Returns:
        G: A DiGraph object, containing the values necessary to create a NetworkGraph with values of new edges added
    """

    elist = []

    for station in g.station_dict.values():

        for key in station.adjacent.keys():

            elist.append((station.id, key, station.adjacent[key]))

    for edge in elist:

        G.add_edge(edge[0], edge[1])

    return G

def EdgeAdderTrajects(G, dienstvoering, mapchooser):

    """
     Adds edges to a NetworkGraph object for each traject in the dienstvoering

    Input:
        G: A DiGraph object, containing the values necessary to create a NetworkGraph
        dienstvoering: A dienstvoering object
        mapchooser: An integer, representing whether the dienstvoering was made for Noord and Zuid Holland or the Netherlands
    Returns:
        G: A DiGraph object, containing the values necessary to create a NetworkGraph with values of new edges added
    """

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

            elist.append((train[0], train[1]))

        for edge in elist:

            G.add_edge(edge[0], edge[1], color=colours[counter], weight=(size - counter))

        counter = counter + 1
        first = elist[0][0]
        length = len(elist) - 1
        last = elist[length][1]

    return G

def NodeTextAdderCritical(G):

    """
     Adds a label to a node in case the node (station) is critical

    Input:
        G: A DiGraph object, containing the values necessary to create a NetworkGraph
    Returns:
        labels_critical: A dictionary, containing the afkortingen of nodes (stations) which are critical
    """

    labels_critical = {}

    for station in g.station_dict.values():

        if station.critical == True:

            name = station.afkorting
            labels_critical[station.id] = station.afkorting

    return labels_critical

def NodeTextAdderNonCritical(G):

    """
     Adds a label to a node in case the node (station) is not critical

    Input:
        G: A DiGraph object, containing the values necessary to create a NetworkGraph
    Returns:
        labels_not_critical: A dictionary, containing the afkortingen of nodes (stations) which are not critical
    """

    labels_not_critical = {}

    for station in g.station_dict.values():

        if station.critical == False:

            name = station.afkorting
            labels_not_critical[station.id] = station.afkorting

    return labels_not_critical

def TrajectsCreator(NetworkXGraph, dienstvoering, mapchooser):

    """
     Creates a NetworkGraph which has the trajects in a dienstvoering as edges

    Input:
        NetworkXGraph: A DiGraph object, containing the values necessary to create a NetworkGraph
        dienstvoering: A dienstvoering object
        mapchooser: An integer, representing whether the dienstvoering was made for Noord and Zuid Holland or the Netherlands

    """

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

    """
     Creates a NetworkGraph

    Input:
        NetworkXGraph: A DiGraph object, containing the values necessary to create a NetworkGraph

    """

    NetworkXGraph = NodeAdder(NetworkXGraph)
    NetworkXGraph = EdgeAdder(NetworkXGraph)

    color_values = []
    color_values = NodeColorSetter(color_values)

    labelsdictcritical = NodeTextAdderCritical(NetworkXGraph)
    labelsdictnoncritical = NodeTextAdderNonCritical(NetworkXGraph)

    pos=nx.get_node_attributes(NetworkXGraph,'pos')
    pos_changed = LabelPositionChanger(pos)
    fig,ax = plt.subplots(1, figsize = (8,11))

    nx.draw(NetworkXGraph, pos, node_color=color_values, node_size=80)
    nx.draw_networkx_labels(NetworkXGraph, pos_changed, labels = labelsdictcritical, font_size=10, font_color='#381e1e')
    nx.draw_networkx_labels(NetworkXGraph, pos_changed, labels = labelsdictnoncritical, font_size=8, font_color='#381e1e')
    
    plt.show()

def MapHelper(mapchooser, dienstvoering):

    """
     Creates a NetworkGraph, of either Noord and Zuid Holland or the Netherlands. Can also use the trajects in a dienstvoering as edges

    Input:
        mapchooser: An integer, representing whether the dienstvoering was made for Noord and Zuid Holland or the Netherlands
        dienstvoering: A dienstvoering object

    """

    NetworkXGraph = nx.DiGraph()
    StationLoader()

    Stringinput = input("Choose which plot to create: Overview or Trajects. ")
    if Stringinput == "Overview":

        OverviewCreator(NetworkXGraph)

    if Stringinput == "Trajects":
        TrajectsCreator(NetworkXGraph, dienstvoering, mapchooser)
