import csv
import matplotlib.pyplot as plt
import numpy as np
from mainActivity import Station, Connection, connections, stations, load_stations, load_connections, INPUT_STATIONS, INPUT_CONNECTIONS
from mpl_toolkits.basemap import Basemap

INPUT_CSV = "StationsHolland.csv"

if __name__ == "__main__":

    map = Basemap(projection='merc', lat_0 = 52, lon_0 = 5,
                  resolution = 'h', area_thresh = 0.1,
                  llcrnrlon=4, llcrnrlat=51.7,
                  urcrnrlon=5.4, urcrnrlat=53.2)

    load_stations(INPUT_STATIONS)

    for station in stations:
        lon = float(stations[station].yCoordinate)
        lat = float(stations[station].xCoordinate)
        x,y = map(lon, lat)
        label = stations[station].name
        plt.text(x, y +5000, label, fontsize = 6)
        map.plot(x, y, 'ko', markersize=6)

    map.drawcoastlines()
    map.drawcountries()
    map.fillcontinents(color = 'coral')
    map.drawmapboundary()

    plt.show()
