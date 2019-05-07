class Traject:
    """
    Representation of a traject
    """

    def __init__(self, trajectId):
        """
        Initializes a Dienstvoering
        """
        self.trajectId = trajectId
        self.time = 0
        self.connections_visited = {}

    def fill_connections(self, a, b, c):
        self.connections_visited[a] = b, c
