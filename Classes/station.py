import sys
class Station:
    """
    Representation of a Station object in RAILNL
    
    """
    def __init__(self, name, xCoordinate, yCoordinate, critical):
        self.id = name
        self.afkorting = None
        self.adjacent = {}
        self.xco = xCoordinate
        self.yco = yCoordinate
        self.critical = critical
        # Set distance to infinity for all nodes
        self.distance = sys.maxsize
        # Mark all nodes unvisited
        self.visited = False
        # Predecessor
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def get_visited(self):
        return self.visited

    def get_critical(self):
        return self.critical

    def _lt_(self, other):
        return self.id < other.id
