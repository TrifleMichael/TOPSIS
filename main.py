import numpy as np
import gui

def readLabels():
    labels = []
    f = open("labels.txt", 'r')
    for line in f:
        if line[-1] == '\n':
            labels.append(line[:-1])
        else:
            labels.append(line)
    f.close()
    return labels

LABELS = readLabels()

def normalize(matrix):
    for col in range(matrix.shape[1]):
        denominator = np.sqrt((matrix[:, col]**2).sum())
        for row in range(matrix.shape[0]):
            matrix[row, col] = matrix[row, col] / denominator

def applyWeights(matrix, criteria_weights):
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            matrix[row, col] = matrix[row, col] * criteria_weights[col]

def idealBestAndWorst(matrix, criteria_positive):
    best = []
    worst = []
    for col in range(matrix.shape[1]):
        if criteria_positive[col]:
            best.append(max(matrix[:, col]))
            worst.append(min(matrix[:, col]))
        else:
            best.append(min(matrix[:, col]))
            worst.append(max(matrix[:, col]))
    return best, worst

def distanceToBest(matrix, best):
    dBest = []
    for row in range(matrix.shape[0]):
        dBest.append(np.sqrt(((matrix[row, :] - best)**2).sum()))
    return dBest

def distanceToWorst(matrix, worst):
    dWorst = []
    for row in range(matrix.shape[0]):
        dWorst.append(np.sqrt(((matrix[row, :] - worst)**2).sum()))
    return dWorst

def calculatePerformanceScore(matrix, distToBest, distToWorst):
    performanceScore = []
    for row in range(matrix.shape[0]):
        performanceScore.append( distToWorst[row] / (distToBest[row] + distToWorst[row]) )
    return performanceScore

def rankOptions(performanceScore):
    # Returns an array with indexes of options (rows in matrix), starting with the best and ending with last
    rank = []
    scoreCopy = np.copy(performanceScore)
    for i in range(len(performanceScore)):
        nextBest = np.argmax(scoreCopy)
        rank.append(nextBest)
        scoreCopy[nextBest] = -float("inf")
    return rank

def calculate(matrix, criteria_weights, criteria_positive):
    normalize(matrix)
    applyWeights(matrix, criteria_weights)
    best, worst = idealBestAndWorst(matrix, criteria_positive)
    distToBest = distanceToBest(matrix, best)
    distToWorst = distanceToWorst(matrix, worst)
    performanceScore = calculatePerformanceScore(matrix, distToBest, distToWorst)
    return rankOptions(performanceScore)


# Wypisuje jakie pozycje w rankingu mają dane opcje z macierzy
placeName = ["Best:", "Second best:", "Third best", "Fourth best", "Worst"]

if __name__ == '__main__':
    with open('items.txt', 'r') as file:
        items = file.readlines()
    items = list(map(lambda x: x[:-1], items))
    matrix = np.zeros((1, len(LABELS)))
    app = gui.Gui(matrix, len(LABELS), LABELS, items)
    app.run()

