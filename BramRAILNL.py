import csv
from Bramstation import Station
from Bramconnection import Connection


INPUT_CONNECTIONS = "CSVfiles/ConnectiesHolland.csv"
INPUT_STATIONS = "CSVfiles/StationsHolland.csv"


def load_stations(file):
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)

        stations = {}
        for row in reader:
            name = row[0].split(';')[0]
            xCoordinate = row[0].split(';')[1]
            yCoordinate = row[0].split(';')[2]
            critical = row[0].split(';')[3]

            station = Station(name, xCoordinate, yCoordinate, critical)
            stations[name] = station

def load_connections(file):
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)

        id = 0
        connections = {}
        for row in reader:
            id += 1
            station1 = row[0]
            station2 = row[1]
            time = row[2]

            connection = Connection(id, station1, station2, time)
            connections[id] = connection

    print(connections[4].stat2)

if __name__ == "__main__":

    load_stations(INPUT_STATIONS)
    load_connections(INPUT_CONNECTIONS)
