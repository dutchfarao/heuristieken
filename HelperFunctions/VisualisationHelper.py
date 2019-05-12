import csv
import matplotlib.pyplot as plt
import numpy as np

# Prints out the average, lowest and highest score for on scores_dict
def CategoricalPlot(scores):

    n = len(scores)
    high = max(scores.values())
    low = min(scores.values())
    total = sum(scores.values())
    average = total / n

    names = ['low', 'average', 'high']
    values = [low, average, high]

    plt.figure(1, figsize=(9, 3))

    plt.subplot(131)
    plt.bar(names, values)
    plt.subplot(132)
    plt.scatter(names, values)
    plt.subplot(133)
    plt.plot(names, values)
    plt.suptitle('Categorical Plotting')
    plt.show()

def GraphPlot(scores):
    pass
