class Connection(object):
    """
    Representation of a connection in RAILNL
    """

    def __init__(self, id, station1, station2, time):
        """
        Initializes a Connection
        """
        self.id = id
        self.stat1 = station1
        self.stat2 = station2
        self.time = time
