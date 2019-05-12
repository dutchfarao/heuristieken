import csv
from Classes.station import Station
from Classes.connection import Connection
from Classes.graph import Graph
from Classes.dienstvoering import Dienstvoering
from HelperFunctions.VisualisationHelper import *


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
            if len(row) == 4 and row[3] == "Kritiek":
                critical = True
            else:
                critical = False

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
            if len(row) == 4:
                critical = True
            else:
                critical = False
            visited = False

            g.add_connection(stationA, stationB, time, critical, visited)

            #g.station_dict[stationA].add_neighbor(stationB, time)
            #g.station_dict[stationB].add_neighbor(stationA, time)

        #connection_printer()

# Function to write the results to a CSV file
def WriteScores(results, choiceAlgorithm):

    # Location where the results will be saved (in CSV format)
    location = choiceAlgorithm + ".csv"
    csv = open(location, "w")
    columnTitleRow = "run, K\n"
    csv.write(columnTitleRow)

    for key in results.keys():
        run = key
        K = results[key]
        row = str(run) + ',' + str(K) + '\n'
        csv.write(row)

def ReadScores(CSVName):

    scores_dict = {}
    location = CSVName + ".csv"
    with open(location, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        for row in reader:
            d = Dienstvoering(int(float(row[0])))
            d.set_score(int(float(row[1])))
            scores_dict[d.dienstId] = int(float(row[1]))

        return(scores_dict)

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
