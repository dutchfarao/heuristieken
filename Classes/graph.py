from station import Station
import sys

# Represents a grid of nodes/stations composed of nodes and edges
class Graph:
    def __init__(self):
        self.station_dict = {}
        self.num_stations = 0

    def __iter__(self):
        return iter(self.station_dict.values())

    def add_station(self, name, xCoordinate, yCoordinate, critical):
        self.num_stations = self.num_stations + 1
        new_station = Station(name, xCoordinate, yCoordinate, critical)
        self.station_dict[name] = new_station
        return new_station

    def get_station(self, n):
        if n in self.station_dict:
            return self.station_dict[n]
        else:
            return None

    def add_connection(self, frm, to, cost = 0, critical = False):
        if frm not in self.station_dict:
            self.add_station(frm)
        if to not in self.station_dict:
            self.add_station(to)

        self.station_dict[frm].add_neighbor(self.station_dict[to], cost)
        self.station_dict[to].add_neighbor(self.station_dict[frm], cost)

    def get_stations(self):
        return self.station_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous
