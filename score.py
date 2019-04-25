import sys

class Score:

    def __init__(self, p, m, T):

        self.p = p
        self.m = m
        self.T = T
        self.K = 0
        self.run = 0

    def get_score(self):
        return self.K

    def get_run(self):
        return self.run

    def set_run(self, run):
        self.run = run

    # The utility function, as defined in the problem description
    def set_K(self):
        K = (10000 * self.p) - (self.T * 20 + self.m / 10)
        self.K = K
