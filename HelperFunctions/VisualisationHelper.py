import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
plt.style.use('fivethirtyeight')
plt.rcParams.update({'figure.autolayout': True})

def currency(x, pos):
    """The two args are the value and tick position"""
    if x >= 1e6:
        s = '{:1.1f}M'.format(x*1e-6)
    else:
        s = '{:1.0f}000'.format(x*1e-3)
    return s

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

# This function calculates the lowest, highest and average K of the results of each algorithm
def Calculator(scores_greedy, scores_random):

    n_greedy = len(scores_greedy)
    n_random = len(scores_random)

    total_greedy = sum(scores_greedy.values())
    total_random = sum(scores_random.values())

    average_greedy = total_greedy / n_greedy
    average_random = total_random / n_random
    #print(average_greedy)
    #print(average_random)

    high_greedy = max(scores_greedy.values())
    low_greedy = min(scores_greedy.values())

    high_random = max(scores_random.values())
    low_random = min(scores_random.values())

    data = {"Greedy" : average_greedy, "Random" : average_random, "Hillclimber" : 3235, "Hillclimber SA" : 3604, "Random + Dijkstra" : 2834}
    group_data = list(data.values())
    group_names = list(data.keys())
    group_mean = np.mean(group_data)

    formatter = FuncFormatter(currency)

    fig, ax = plt.subplots()
    ax.barh(group_names, group_data)
    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=45, horizontalalignment='right')
    ax.set(xlim=[0, 6000], xlabel='Average K', ylabel='Algorithm', title='Difference in averages')
    ax.xaxis.set_major_formatter(formatter)
    ax.axvline(average_random, ls='--', color='r')
    ax.title.set(y=1.05)

    # Annotate new companies
    for group in [0]:
        ax.text(5000, group, "-1%", fontsize=10,
                verticalalignment="center")

    for group in [2]:
        ax.text(5000, group, "+3%", fontsize=10,
                verticalalignment="center")

    for group in [3]:
        ax.text(5000, group, "+12%", fontsize=10,
                verticalalignment="center")

    for group in [4]:
        ax.text(5000, group, "-6%", fontsize=10,
                verticalalignment="center")

    plt.show()

    # Uncomment this line to save the figure.
    # fig.savefig('sales.png', transparent=False, dpi=80, bbox_inches="tight")

    pass
