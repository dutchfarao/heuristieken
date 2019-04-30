import csv
import matplotlib.pyplot as plt
import numpy as np
from mainActivity import Station, Connection, connections, stations, load_stations, load_connections, INPUT_STATIONS, INPUT_CONNECTIONS
from mpl_toolkits.basemap import Basemap


def draw_stations(map, stations):

    for station in stations:
        lon = float(stations[station].yCoordinate)
        lat = float(stations[station].xCoordinate)
        x,y = map(lon, lat)
        #label = stations[station].name
        #plt.text(x, y +5000, lael, fontsize = 6)
        if stations[station].critical == "Kritiek":
            map.plot(x, y, 'o', c="white", markeredgecolor="black", markersize=6)
        else:
            map.plot(x, y, 'ko', markersize=3)


def draw_connections(map, stations, connections):

    for connection in connections:
        lon = []
        lat = []
        lon.append(float(stations[str(connections[connection].stat1)].yCoordinate))
        lat.append(float(stations[str(connections[connection].stat1)].xCoordinate))
        lon.append(float(stations[str(connections[connection].stat2)].yCoordinate))
        lat.append(float(stations[str(connections[connection].stat2)].xCoordinate))
        x,y = map(lon, lat)
        map.plot(x, y, 'k-', markersize=5, linewidth=1)

def set_map():

    load_stations(INPUT_STATIONS)
    load_connections(INPUT_CONNECTIONS)

    map = Basemap(projection='merc', lat_0 = 52, lon_0 = 5,
              resolution = 'h', area_thresh = 0.1,
              llcrnrlon=4, llcrnrlat=51.7,
              urcrnrlon=5.4, urcrnrlat=53.2)

    draw_connections(map, stations, connections)
    draw_stations(map, stations)

    map.drawcoastlines()
    map.drawcountries()
    map.fillcontinents(color = 'coral')
    map.drawmapboundary()
    return stations, map


def draw_route(map, stations, route):

    line_lon = []
    line_lat = []
    for station in route:
        lon = float(stations[station].yCoordinate)
        lat = float(stations[station].xCoordinate)
        x,y = map(lon, lat)
        #label = stations[station].name
        #plt.text(x, y +5000, label, fontsize = 6)
        if stations[station].critical == "Kritiek":
            map.plot(x, y, 'o', c="yellow",markeredgecolor="red",markersize=6,zorder=10)
        else:
            map.plot(x, y, 'o', c="red",markersize=3,zorder=10)
        line_lon.append(lon)
        line_lat.append(lat)
    x,y = map(line_lon, line_lat)
    map.plot(x, y, '-', c="red", markersize=5, linewidth=1,zorder=5)


def get_map(route):

    stations, map = set_map()
    draw_route(map, stations, route)
    plt.show()

if __name__ == "__main__":

    set_map()
    plt.show()
