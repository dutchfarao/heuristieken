import csv
from Classes.station import Station
from Classes.connection import Connection
from Classes.graph import Graph
from Classes.dienstvoering import Dienstvoering

stations = {}
connections = {}
g = Graph()

def load_stations(file):

    """
     Loads stations from a CSV file and adds them to a graph

    Input:
        file: A string, either "Data/StationsNationaal.csv" or "Data/StationsHolland.csv"
    """

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

            g.add_station(name, xCoordinate, yCoordinate, critical)

def load_connections(file):

    """
     Loads connections from a CSV file and adds them to a graph

    Input:
        file: A string, either "Data/ConnectiesHolland.csv" or "Data/ConnectiesNationaal.csv"
    """



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

def WriteScores(results, choiceAlgorithm, mode, mapchooser):

    """
     Writes scores from an algorithm to a CSV file

    Input:
        results: A string, either "Data/ConnectiesHolland.csv" or "Data/ConnectiesNationaal.csv"
        choiceAlgorithm: A string, the name of the algorithm used
        mode: An integer, representing whether the scores are stored in a dictionary or only one score is passed
        mapchooser: An integer, representing whether the dienstvoering was made for Noord and Zuid Holland or the Netherlands
    """
    if mapchooser == 1:
        string_size = "NL"

    if mapchooser == 2:
        string_size = "NZH"

    # Location where the results will be saved (in CSV format)
    location = choiceAlgorithm + string_size + ".csv"
    csv = open(location, "w")
    columnTitleRow = "run, K\n"
    csv.write(columnTitleRow)

    if mode == 1:
        for key in results.keys():
            run = key
            K = results[key]
            row = str(run) + ',' + str(K) + '\n'
            csv.write(row)

    if mode == 3:

        run = 0
        row = str(run) + ',' + str(results) + '\n'
        csv.write(row)

def ReadScores(CSVName):

    """
     Reads scores from a CSV file and adds them to a dictionary

    Input:
        CSVName: A string, the name of the file to be scanned for scores
    Returns:
        scores_dict: A dictionary of scores, containing the run number and a score
    """

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


if __name__ == "__main__":

    load_stations(INPUT_STATIONS)
    load_connections(INPUT_CONNECTIONS)
