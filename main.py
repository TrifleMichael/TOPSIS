import numpy as np
import gui

N_FEATURES = 4
# Macierz jak w filmiku
matrix = np.array([[250, 16, 12, 5], [200, 16, 8, 3], [300, 32, 16, 4], [275, 32, 8, 4], [225, 16, 16, 2]], dtype=np.float32)
# Waga kryteriów (dowolne dodatnie wartości)
criteria_weights = [1/N_FEATURES for i in range(N_FEATURES)]
# Czy im większe kryterium tym lepsze
criteria_positive = [False, True, True, True]

def showMatrix(matrix=matrix):
    for row in matrix:
        print(row)

def normalize(matrix):
    for col in range(matrix.shape[1]):
        denominator = np.sqrt((matrix[:, col]**2).sum())
        for row in range(matrix.shape[0]):
            matrix[row, col] = matrix[row, col] / denominator

def applyWeights(matrix):
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            matrix[row, col] = matrix[row, col] * criteria_weights[col]

def idealBestAndWorst(matrix):
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

def calculate(matrix):
    normalize(matrix)
    applyWeights(matrix)
    best, worst = idealBestAndWorst(matrix)
    distToBest = distanceToBest(matrix, best)
    distToWorst = distanceToWorst(matrix, worst)
    performanceScore = calculatePerformanceScore(matrix, distToBest, distToWorst)
    return rankOptions(performanceScore)


# Wypisuje jakie pozycje w rankingu mają dane opcje z macierzy
placeName = ["Best:", "Second best:", "Third best", "Fourth best", "Worst"]

if __name__ == '__main__':
    matrix = np.zeros((1, N_FEATURES))
    app = gui.Gui(matrix, N_FEATURES)
    app.run()

