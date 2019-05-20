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
        self.critical_visited_HC = []
        self.minutes = 0

    #input station of departure(a) and destinaton(b)
    def fill_critical(self, a, b):
        self.critical_visited.append((a, b))
        self.critical_visited.append((b, a))

    #input station of departure(a) and destinaton(b)
    def fill_critical_HC(self, a, b):
        self.critical_visited_HC.append((a, b))
        self.critical_visited_HC.append((b, a))

    def get_critical_visited(self, a, b):
        if ((a , b) in self.critical_visited):
            return True
        elif ((b, a) in self.critical_visited):
            return True
        else:
            return False

    def set_score(self, score):
        #p = (20/(len(critical_visited)))
        #self.score = (10000 * self.p) - (self.t * 20 + self.m / 10)
        self.score = score

    def get_score(self):
        return self.score
