class Station(object):
    """
    Representation of a station in RAILNL
    """

    def __init__(self, name, xCoordinate, yCoordinate, critical):
        """
        Initializes a Station
        """
        self.name = name
        self.xco = xCoordinate
        self.yco = yCoordinate
        self.critical = critical
        self.connections = []
