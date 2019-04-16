
# Implements a station object
class Station:
    """
    Representation of a station in RAILNL
    """

    def __init__(self, name, xCoordinate, yCoordinate, critical):
        """
        Initializes a Station
        """
        self.name = name
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate
        self.critical = critical
        self.connections = []
