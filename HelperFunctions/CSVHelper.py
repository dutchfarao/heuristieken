import csv
from station import Station
from connection import Connection


INPUT_CONNECTIONS = "ConnectiesHolland.csv"
INPUT_STATIONS = "StationsHolland.csv"
stations = {}
connections = {}

# Function to load the CSV file 'StationsHolland' into a dictionary named 'stations'
def load_stations(file):

    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            name = row[0]
            yCoordinate = row[1]
            xCoordinate = row[2]
            critical = row[3]

            station = Station(name, yCoordinate, xCoordinate, critical)
            stations[name] = station

        #station_printer()

# Function to load the CSV file 'ConnectiesHolland' into a dictionary named connections
def load_connections(file):

    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        stripe = '>'

        id = 0
        for row in reader:
            id += 1
            station1 = row[0]
            station2 = row[1]
            time = row[2]
            name = station1 + stripe + station2

            connection = Connection(name, id, station1, station2, time)
            connections[name] = connection

            if row[3] == 'Kritiek':
                connections[name].cc = True

            AddDestination(station1, station2)
            AddDestination(station2, station1)

        #connection_printer()

# Function to write the results to a CSV file
def WriteScores(results):

    # Location where the results will be saved (in CSV format)
    save_location = "DijkstraRandomResults.csv"
    csv = open(save_location, "w")
    columnTitleRow = "run, K\n"
    csv.write(columnTitleRow)

    for key in results.keys():
        run = key
        K = results[key]
        row = str(run) + ',' + str(K) + '\n'
        csv.write(row)

# Can be called upon to check the contents of the dictionary 'stations'
def station_printer():

    for index, value in stations.items():
        print(index, value)

# Can be called upon to check the contents of the dictionary 'connections'
def connection_printer():

    for index, value in connections.items():
        print(index, value)


if __name__ == "__main__":

    load_stations(INPUT_STATIONS)
    load_connections(INPUT_CONNECTIONS)
    WriteScores(results)

    print(str(len(connections)))
