# Implements a Dienstvoering object
class Dienstvoering:
    """
    Representation of a dienstvoering (7 trajects) in RAILNL
    """

    def __init__(self, dienstId):
        """
        Initializes a Dienstvoering
        """
        self.dienstId = dienstId
        self.score = 0
        self.trajects = {}
        self.critical_visited = []

def fill_critical(self, critical):
    self.critical_visited.append(critical)

def set_score(self, p, m, t):
    p = (20/(len(critical_visited)))
    self.score = (10000 * self.p) - (self.t * 20 + self.m / 10)
