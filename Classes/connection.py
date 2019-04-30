"""
Representation of a connection in RAILNL
"""

class Connection:

    def __init__(self, name, stationA, stationB, time):

        """
        Initializes a Connection
        """
        self.name = name
        self.stationA = stationA
        self.stationB = stationB
        self.time = time
        self.critical = False
        self.visited = False
