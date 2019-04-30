# Implements a station object
class Station:
    """
    Representation of a station in RAILNL
    """

    def __init__(self, name, yCoordinate, xCoordinate, critical):
        """
        Initializes a Station
        """
        self.name = name
        self.yco = yCoordinate
        self.xco = xCoordinate
        self.critical = critical
        self.destinations = []

    def __str__(self):
        return self.name

    def AddDestination(self, dest):
        self.destinations.append(dest)
