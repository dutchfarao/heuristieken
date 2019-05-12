import csv
import matplotlib.pyplot as plt
import numpy as np

def CategoricalPlot(scores):

    for row in scores:
        print(row)

    x = np.arange(0, 10, 0.2)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()

def GraphPlot(scores):
    pass
