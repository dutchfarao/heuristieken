import csv
from Classes.station import Station
from Classes.connection import Connection
from Classes.graph import Graph


INPUT_CONNECTIONS = "Data/ConnectiesHolland.csv"
INPUT_STATIONS = "Data/StationsHolland.csv"
stations = {}
connections = {}
g = Graph()
# Function to load the CSV file 'StationsHolland' into a dictionary named 'stations'
def load_stations(file):

    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            name = row[0]
            yCoordinate = row[1]
            xCoordinate = row[2]
            critical = row[3]

            g.add_station(name, yCoordinate, xCoordinate, critical)


        #station_printer()

# Function to load the CSV file 'ConnectiesHolland' into a dictionary named connections
def load_connections(file):

    with open(file, newline='') as csvfile:

        reader = csv.reader(csvfile)

        for row in reader:

            stationA = row[0]
            stationB = row[1]
            time = row[2]
            if row[3] == 'Kritiek':
                critical = True
            else :
                critical = False
            visited = False

            g.add_connection(stationA, stationB, time, critical, visited)

            g.station_dict[stationA].add_neighbor(stationB, time)
            g.station_dict[stationB].add_neighbor(stationA, time)

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
    #WriteScores(results)
