class Connection:

    def __init__(self, name, stationA, stationB, time):
        """
        Representation of a connection in RAILNL
        """
        self.name = name
        self.stationA = stationA
        self.stationB = stationB
        self.time = time
        self.critical = False
        self.visited = False
