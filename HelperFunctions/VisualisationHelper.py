import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
plt.style.use('fivethirtyeight')
plt.rcParams.update({'figure.autolayout': True})

def currency(x, pos):

    """
    Used to format the values of the labels of the minor ticks in a plot

    Input:
        x: An integer
        pos: An integer

    Returns:
        s: A float

    """
    if x >= 1e6:
        s = '{:1.1f}M'.format(x*1e-6)
    else:
        s = '{:1.0f}000'.format(x*1e-3)
    return s

# Creates a histogram of the scores of a certain algorithm
def HistogramPlot(scores, name):

    """
    Plots a histogram of scores of a certain algorithm

    Input:
        scores: A dictionary, containing the values of the scores of a certain algorithm
        name: A string, the name of the algorithm which generated the scores
    """

    scores_array = []
    for row in scores.values():
        scores_array.append(row)

    maximum = max(scores_array)
    n = len(scores_array)
    total = sum(scores_array)
    average = total / n

    n_string = "n = " + str(n)

    arrayticks = [0, 100, 200, 300, 400]

    arraybins = []
    bincounter = 0
    for i in range(20):
        bincounter = bincounter + 500
        arraybins.append(bincounter)

    plt.hist(scores_array, bins=arraybins)
    plt.xlabel('Value of K')
    plt.ylabel('Amount of occurences')
    plt.yticks(arrayticks)
    plt.title(name)
    plt.text(100, 420, n_string)
    plt.axvline(average, label='average at x = {}'.format(average), linestyle='dashed', linewidth=2, color='r')
    plt.tight_layout()
    plt.legend()
    plt.show()

# Prints out the average, lowest and highest score for on scores_dict
def CategoricalPlot(scores_A, scores_B):

    """
    Creates a plot comparing the values of two dictionaries

    Input:
        scores: A dictionary, containing the values of the scores of a certain algorithm
        name: A string, the name of the algorithm which generated the scores
    """

    n_A = len(scores_A)
    n_B = len(scores_B)

    run_array = []
    for key in scores_A.keys():
        run_array.append(key)

    scores_array_A = []
    for row in scores_A.values():
        scores_array_A.append(row)

    scores_array_B = []
    for row in scores_B.values():
        scores_array_B.append(row)

    plt.plot(run_array, scores_array_A, 'r', linewidth=0.4)
    plt.plot(run_array, scores_array_B, 'b', linewidth=0.4)

    plt.xlabel('Run')
    plt.ylabel('Value')
    plt.title("A versus B")
    plt.tight_layout()
    plt.show()

# This function calculates the lowest, highest and average K of the results of each algorithm
def BarPlot(scores_random, scores_greedy, scores_HC, scores_SA):

    """
    Plots a barchart comparing the scores of all algorithms

    Input:
        scores_random: A dictionary, containing the values of the scores of Random
        scores_greedy: A dictionary, containing the values of the scores of Greedy
        scores_HC: A dictionary, containing the values of the scores of Hillclimber
        scores_SA: A dictionary, containing the values of the scores of Simulated Annealing
    """

    n_greedy = len(scores_greedy)
    n_random = len(scores_random)
    n_SA = len(scores_SA)
    n_HC = len(scores_HC)

    total_greedy = sum(scores_greedy.values())
    total_random = sum(scores_random.values())
    total_SA = sum(scores_SA.values())
    total_HC = sum(scores_HC.values())

    average_greedy = total_greedy / n_greedy
    average_random = total_random / n_random
    average_SA = total_SA / n_SA
    average_HC = total_HC / n_HC

    high_greedy = max(scores_greedy.values())
    low_greedy = min(scores_greedy.values())

    high_random = max(scores_random.values())
    low_random = min(scores_random.values())

    high_SA = max(scores_SA.values())
    low_SA = min(scores_SA.values())

    high_HC = max(scores_HC.values())
    low_HC = min(scores_HC.values())

    data = {"Random" : average_random, "Greedy" : average_greedy, "Hillclimber" : average_HC, "SA" : average_SA}
    group_data = list(data.values())
    group_names = list(data.keys())
    group_mean = np.mean(group_data)

    formatter = FuncFormatter(currency)

    fig, ax = plt.subplots()
    ax.barh(group_names, group_data)
    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=45, horizontalalignment='right')
    ax.set(xlim=[0, 10000], xlabel='Average K', ylabel='Algorithm', title='Difference in averages')
    ax.xaxis.set_major_formatter(formatter)
    ax.axvline(average_random, ls='--', color='r', linewidth=0.5)
    ax.title.set(y=1.05)


    for group in [1]:
        percentage = PercentageCalculator(average_greedy, average_random)
        ax.text(high_greedy, group, percentage, fontsize=14)

    for group in [2]:
        percentage = PercentageCalculator(average_HC, average_random)
        ax.text(high_HC, group, percentage, fontsize=14)

    for group in [3]:
        percentage = PercentageCalculator(average_SA, average_random)
        ax.text(high_SA, group, percentage, fontsize=14)

    plt.show()

def PercentageCalculator(average_algorithm, average_random):

    """
    Calculates the difference between two values in percentages

    Input:
        average_algorithm: An integer, representing the average value of the score of a certain algorithm
        average_random: An integer, representing the average value of the score of random
    Returns:
        percentage_string: A string, representing the percentage difference between two values
    """

    percentage = (average_algorithm - average_random) / average_random
    percentage_string = "{0:.3f}".format(percentage) + "%"

    return percentage_string
