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
        self.critical_visited = {}


    def fill_critical(self, critical):
        self.critical_visited.append(critical)

    def get_critical_visited(self, a, b):
        #check if departure>adjacent is critical
        key,value = a,b
        try1 = key in self.critical_visited and value == self.critical_visited[key]
        #check if adjacent>departure is critical
        key,value = b,a
        try2 = key in self.critical_visited and value == self.critical_visited[key]
        #return True if connection is critical, else return False
        if try1 or try2 == True:
            return True
        else:
            return False

    def set_score(self, p, m, t):
        p = (20/(len(critical_visited)))
        self.score = (10000 * self.p) - (self.t * 20 + self.m / 10)

    def get_score(self):
        return self.score
