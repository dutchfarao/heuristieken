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
    y_off = 0.025 # offset on the y axis

    for k, v in pos.items():
        pos_changed[k] = (v[0], v[1] + y_off)

    return pos_changed

def NodeColorSetter(color_values):

    for station in g.station_dict.values():
        if station.critical == True:
            color_values.append('k')

        if station.critical == False:
            color_values.append('#808080')

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

def EdgeAdderHolland(G, dienstvoering):


    for traject in dienstvoering.trajects:

        for train in traject.connections_visited:

            print(train)
        # for key in station.adjacent.keys():
        #     elist.append((station.id, key, station.adjacent[key]))

    #print(elist)
    #
    # for edge in elist:
    #
    #     print(edge)
    #     G.add_edge(edge[0], edge[1])

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

def Nederland():
    NetworkXGraph = NodeAdder(NetworkXGraph)
    NetworkXGraph = EdgeAdder(NetworkXGraph)
    color_values = []
    color_values = NodeColorSetter(color_values)
    labelsdictcritical = NodeTextAdderCritical(NetworkXGraph)
    labelsdictnoncritical = NodeTextAdderNonCritical(NetworkXGraph)
    pos=nx.get_node_attributes(NetworkXGraph,'pos')
    pos_changed = LabelPositionChanger(pos)
    fig,ax = plt.subplots(1, figsize = (7,12))
    nx.draw(NetworkXGraph, pos, node_color=color_values, node_size=70)
    nx.draw_networkx_labels(NetworkXGraph, pos_changed, labels = labelsdictcritical, font_size=14, font_color='#ffb780')
    nx.draw_networkx_labels(NetworkXGraph, pos_changed, labels = labelsdictnoncritical, font_size=12, font_color='#80916b')
    plt.show()

def Holland(NetworkXGraph, dienstvoering):

    NetworkXGraph = NodeAdder(NetworkXGraph)
    NetworkXGraph = EdgeAdderHolland(NetworkXGraph, dienstvoering)

    color_values = []
    color_values = NodeColorSetter(color_values)

    labelsdictcritical = NodeTextAdderCritical(NetworkXGraph)
    labelsdictnoncritical = NodeTextAdderNonCritical(NetworkXGraph)

    pos=nx.get_node_attributes(NetworkXGraph,'pos')
    pos_changed = LabelPositionChanger(pos)

    fig,ax = plt.subplots(1, figsize = (7,12))
    nx.draw(NetworkXGraph, pos, node_color=color_values, node_size=70)
    nx.draw_networkx_labels(NetworkXGraph, pos_changed, labels = labelsdictcritical, font_size=14, font_color='#ffb780')
    nx.draw_networkx_labels(NetworkXGraph, pos_changed, labels = labelsdictnoncritical, font_size=12, font_color='#80916b')
    plt.show()

def OverviewCreator(NetworkXGraph):

    NetworkXGraph = NodeAdder(NetworkXGraph)
    NetworkXGraph = EdgeAdder(NetworkXGraph)
    color_values = []
    color_values = NodeColorSetter(color_values)
    labelsdictcritical = NodeTextAdderCritical(NetworkXGraph)
    labelsdictnoncritical = NodeTextAdderNonCritical(NetworkXGraph)
    pos=nx.get_node_attributes(NetworkXGraph,'pos')
    pos_changed = LabelPositionChanger(pos)
    fig,ax = plt.subplots(1, figsize = (7,12))
    nx.draw(NetworkXGraph, pos, node_color=color_values, node_size=70)
    nx.draw_networkx_labels(NetworkXGraph, pos_changed, labels = labelsdictcritical, font_size=14, font_color='#ffb780')
    nx.draw_networkx_labels(NetworkXGraph, pos_changed, labels = labelsdictnoncritical, font_size=12, font_color='#80916b')
    plt.show()

def MapHelper(mapchooser, dienstvoering):

    NetworkXGraph = nx.Graph()
    StationLoader()
    # NetworkXGraph = NodeAdder(NetworkXGraph)
    # NetworkXGraph = EdgeAdder(NetworkXGraph)

    input("Choose which plot to create: Overview, Nederland or Holland.")
    if input == "Overview":
        OverviewCreator(NetworkXGraph)

    if input == "Holland":
        Holland(NetworkXGraph)

    else:
        OverviewCreator(NetworkXGraph)import csv
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
    y_off = 0.025 # offset on the y axis

    for k, v in pos.items():
        pos_changed[k] = (v[0], v[1] + y_off)

    return pos_changed

def NodeColorSetter(color_values):

    for station in g.station_dict.values():
        if station.critical == True:
            color_values.append('k')

        if station.critical == False:
            color_values.append('#808080')

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

def EdgeAdderHolland(G, dienstvoering):


    for traject in dienstvoering.trajects:

        for train in traject.connections_visited:

            print(train)
        # for key in station.adjacent.keys():
        #     elist.append((station.id, key, station.adjacent[key]))

    #print(elist)
    #
    # for edge in elist:
    #
    #     print(edge)
    #     G.add_edge(edge[0], edge[1])

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

def Nederland():
    NetworkXGraph = NodeAdder(NetworkXGraph)
    NetworkXGraph = EdgeAdder(NetworkXGraph)
    color_values = []
    color_values = NodeColorSetter(color_values)
    labelsdictcritical = NodeTextAdderCritical(NetworkXGraph)
    labelsdictnoncritical = NodeTextAdderNonCritical(NetworkXGraph)
    pos=nx.get_node_attributes(NetworkXGraph,'pos')
    pos_changed = LabelPositionChanger(pos)
    fig,ax = plt.subplots(1, figsize = (7,12))
    nx.draw(NetworkXGraph, pos, node_color=color_values, node_size=70)
    nx.draw_networkx_labels(NetworkXGraph, pos_changed, labels = labelsdictcritical, font_size=14, font_color='#ffb780')
    nx.draw_networkx_labels(NetworkXGraph, pos_changed, labels = labelsdictnoncritical, font_size=12, font_color='#80916b')
    plt.show()

def Holland(NetworkXGraph, dienstvoering):

    NetworkXGraph = NodeAdder(NetworkXGraph)
    NetworkXGraph = EdgeAdderHolland(NetworkXGraph, dienstvoering)

    color_values = []
    color_values = NodeColorSetter(color_values)

    labelsdictcritical = NodeTextAdderCritical(NetworkXGraph)
    labelsdictnoncritical = NodeTextAdderNonCritical(NetworkXGraph)

    pos=nx.get_node_attributes(NetworkXGraph,'pos')
    pos_changed = LabelPositionChanger(pos)

    fig,ax = plt.subplots(1, figsize = (7,12))
    nx.draw(NetworkXGraph, pos, node_color=color_values, node_size=70)
    nx.draw_networkx_labels(NetworkXGraph, pos_changed, labels = labelsdictcritical, font_size=14, font_color='#ffb780')
    nx.draw_networkx_labels(NetworkXGraph, pos_changed, labels = labelsdictnoncritical, font_size=12, font_color='#80916b')
    plt.show()

def OverviewCreator(NetworkXGraph):

    NetworkXGraph = NodeAdder(NetworkXGraph)
    NetworkXGraph = EdgeAdder(NetworkXGraph)
    color_values = []
    color_values = NodeColorSetter(color_values)
    labelsdictcritical = NodeTextAdderCritical(NetworkXGraph)
    labelsdictnoncritical = NodeTextAdderNonCritical(NetworkXGraph)
    pos=nx.get_node_attributes(NetworkXGraph,'pos')
    pos_changed = LabelPositionChanger(pos)
    fig,ax = plt.subplots(1, figsize = (7,12))
    nx.draw(NetworkXGraph, pos, node_color=color_values, node_size=70)
    nx.draw_networkx_labels(NetworkXGraph, pos_changed, labels = labelsdictcritical, font_size=14, font_color='#ffb780')
    nx.draw_networkx_labels(NetworkXGraph, pos_changed, labels = labelsdictnoncritical, font_size=12, font_color='#80916b')
    plt.show()

def MapHelper(mapchooser, dienstvoering):

    NetworkXGraph = nx.Graph()
    StationLoader()
    # NetworkXGraph = NodeAdder(NetworkXGraph)
    # NetworkXGraph = EdgeAdder(NetworkXGraph)

    input("Choose which plot to create: Overview, Nederland or Holland.")
    if input == "Overview":
        OverviewCreator(NetworkXGraph)

    if input == "Holland":
        Holland(NetworkXGraph)

    else:
        OverviewCreator(NetworkXGraph)
