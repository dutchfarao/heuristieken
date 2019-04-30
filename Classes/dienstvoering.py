# Implements a Dienstvoering object
class Dienstvoering:
    """
    Representation of a dienstvoering (7 trajects) in RAILNL
    """

    def __init__(self, dienstId):
        """
        Initializes a Station
        """
        self.dienstId = dienstId
        self.trajects = {}
        self.connections = []
        self.critical_connections = []
        self.connections = []
