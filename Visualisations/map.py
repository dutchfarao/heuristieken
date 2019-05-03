import csv
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap


def draw_stations(g, map):

    for station in g.station_dict.values():
        lon = float(station.xco)
        lat = float(station.yco)
        x,y = map(lon, lat)
        #label = stations[station].name
        #plt.text(x, y +5000, lael, fontsize = 6)
        if station.critical == True:
            map.plot(x, y, 'o', c="white", markeredgecolor="black", markersize=6)
        else:
            map.plot(x, y, 'ko', markersize=3)


def draw_connections(g, map):

    for station in g.station_dict.values():
        for neighbor in station.adjacent:
            lon = []
            lat = []
            lon.append(float(station.xco))
            lat.append(float(station.yco))
            lon.append(float(g.station_dict[neighbor].xco))
            lat.append(float(g.station_dict[neighbor].yco))
            x,y = map(lon, lat)
            map.plot(x, y, 'k-', markersize=5, linewidth=1)

def set_map(g, choiceRegion):

    if choiceRegion == "HO":
        LON_MIN = 4
        LON_MAX = 5.4
        LAT_MIN = 51.7
        LAT_MAX = 53.2
    else:
        LON_MIN = 3.3
        LON_MAX = 7.2
        LAT_MIN = 50.7
        LAT_MAX = 53.5

    map = Basemap(projection='merc', lat_0 = 52, lon_0 = 5,
              resolution = 'h', area_thresh = 0.1,
              llcrnrlon= LON_MIN, llcrnrlat= LAT_MIN,
              urcrnrlon= LON_MAX, urcrnrlat=LAT_MAX)

    draw_connections(g, map)
    draw_stations(g, map)

    map.drawcoastlines()
    map.drawcountries()
    map.fillcontinents(color = 'coral')
    map.drawmapboundary()
    return map


def draw_route(g, map, route):

    line_lon = []
    line_lat = []
    for station in route:
        lon = float(g.station_dict[station].xco)
        lat = float(g.station_dict[station].yco)
        x,y = map(lon, lat)
        #label = stations[station].name
        #plt.text(x, y +5000, label, fontsize = 6)
        if g.station_dict[station].critical == True:
            map.plot(x, y, 'o', c="yellow",markeredgecolor="red",markersize=6,zorder=10)
        else:
            map.plot(x, y, 'o', c="red",markersize=3,zorder=10)
        line_lon.append(lon)
        line_lat.append(lat)
    x,y = map(line_lon, line_lat)
    map.plot(x, y, '-', c="red", markersize=5, linewidth=1,zorder=5)


def get_map(g, choiceRegion, route):

    map = set_map(g, choiceRegion)
    draw_route(g, map, route)
    plt.show()

if __name__ == "__main__":

    set_map()
    plt.show()
