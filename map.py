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
    load_connections(INPUT_CONNECTIONS)

    for station in stations:
        lon = float(stations[station].yCoordinate)
        lat = float(stations[station].xCoordinate)
        x,y = map(lon, lat)
        label = stations[station].name
        #plt.text(x, y +5000, label, fontsize = 6)
        #map.plot(x, y, 'ko', markersize=6)

    for connection in connections:
        lon1 = float(stations[str(connections[connection].stat1)].yCoordinate)
        lat1 = float(stations[str(connections[connection].stat1)].xCoordinate)
        lon2 = float(stations[str(connections[connection].stat2)].yCoordinate)
        lat2 = float(stations[str(connections[connection].stat2)].xCoordinate)
        plt.plot([lat1,lat2], [lon1,lon2],marker='o', linewidth=5)

    map.drawcoastlines()
    map.drawcountries()
    map.fillcontinents(color = 'coral')
    map.drawmapboundary()

    plt.show()
