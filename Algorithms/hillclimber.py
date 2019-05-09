from Classes.graph import *
from Classes.station import *
from random import *
from main import *

def Hillclimber():

    hillclimber_dienstvoeringen = {}
    lowest_score = 10000

    for i in range(3):

        for i in range(10):
            d = Random()
            if d.score < lowest_score:
            lowest_score = d.score

        if hillclimber_dienstvoeringen.value.score == lowest_score
            remove
        hillclimber_dienstvoeringen[i] = d

    print(hillclimber_dienstvoeringen.values.dienstId)
