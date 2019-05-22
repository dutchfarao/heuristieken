from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


m = Basemap(projection='mill',
            llcrnrlat = 50,
            llcrnrlon = 3,
            urcrnrlat = 54,
            urcrnrlon = 8,
            resolution='l')

m.drawcoastlines()
m.drawcountries()

m.bluemarble()

xs = []
ys = []

NYClat, NYClon = 40.7127, -74.0059
xpt, ypt = m(NYClon, NYClat)
xs.append(xpt)
ys.append(ypt)
m.plot(xpt, ypt, 'c^', markersize=15)

LAlat, LAlon = 34.05, -118.05
xpt, ypt = m(LAlon, LAlat)
xs.append(xpt)
ys.append(ypt)
m.plot(xpt, ypt, 'g^', markersize=15)

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

m.plot(xs, ys, color='r', linewidth=3, label='traject1')
plt.legend(loc=4)
plt.title("basemap")
plt.show()
