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
        self.critical_visited = []
        self.critical_visited_HC = []
        self.K_traject = 0
        self.Min_traject = 0

    def fill_connections(self, a, b, c):
        self.connections_visited[a] = b, c

    #input station of departure(a) and destinaton(b)
    def fill_critical(self, a, b):
        self.critical_visited.append((a, b))
        self.critical_visited.append((b, a))

    #input station of departure(a) and destinaton(b)
    def fill_critical_HC(self, a, b):
        self.critical_visited_HC.append((a, b))
        self.critical_visited_HC.append((b, a))
