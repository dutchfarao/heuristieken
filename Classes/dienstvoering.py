
class Dienstvoering:
    """
    Representation of a dienstvoering object in RAILNL
    """
    def __init__(self, dienstId):
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

    #input station of departure(a) and destinaton(b)
    def get_critical_visited(self, a, b):
        if ((a , b) in self.critical_visited):
            return True
        elif ((b, a) in self.critical_visited):
            return True
        else:
            return False

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score
