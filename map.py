import csv
import matplotlib.pyplot as plt
import numpy as np
from mainActivity import Station, Connection, connections, stations, load_stations, load_connections, INPUT_STATIONS, INPUT_CONNECTIONS
from mpl_toolkits.basemap import Basemap

INPUT_STATIONS = "StationsHolland.csv"
INPUT_CONNECTIONS = "ConnectiesHolland.csv"

def load_map():

    map = Basemap(projection='merc', lat_0 = 52, lon_0 = 5,
                  resolution = 'h', area_thresh = 0.1,
                  llcrnrlon=4, llcrnrlat=51.7,
                  urcrnrlon=5.4, urcrnrlat=53.2)
    map.drawcoastlines()
    map.drawcountries()
    map.fillcontinents(color = 'coral')
    map.drawmapboundary()

def draw_stations(stations):

    for station in stations:
        lon = float(stations[station].yCoordinate)
        lat = float(stations[station].xCoordinate)
        x,y = map(lon, lat)
        label = stations[station].name
        plt.text(x, y +5000, label, fontsize = 6)
        map.plot(x, y, 'ko', markersize=6)

def draw_connections(stations, connections):

    for connection in connections:
        lon = []
        lat = []
        lon.append(float(stations[str(connections[connection].stat1)].yCoordinate))
        lat.append(float(stations[str(connections[connection].stat1)].xCoordinate))
        lon.append(float(stations[str(connections[connection].stat2)].yCoordinate))
        lat.append(float(stations[str(connections[connection].stat2)].xCoordinate))
        x,y = map(lon, lat)
        map.plot(x, y, 'k-', markersize=5, linewidth=1)

if __name__ == "__main__":

    load_map()
    load_stations(INPUT_STATIONS)
    load_connections(INPUT_CONNECTIONS)

    draw_stations(stations)
    draw_connections(stations, connections)

    plt.show()
