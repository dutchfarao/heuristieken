from Classes.graph import *
from Classes.station import *
from random import *
from main import *

def Hillclimber():

    hillclimber_dienstvoeringen = {}

    for i in range(10):
        d = Random()
        hillclimber_dienstvoeringen[i] = d

    print(hillclimber_dienstvoeringen[0].value.score)
