import numpy as np
import pandas as pd


def average_fare(matrix, column):
    """
    :param matrix: Matrix
    :param column: Int
    :return: Filled fare column with average of other fares
    """
    sum = 0
    nul = 0
    for line in range(len(matrix)):
        if pd.isnull(matrix[line, column]):
            nul += 1
        else:
            sum += float(matrix[line, column])

    avg = sum / (len(matrix) - nul)

    for line in range(len(matrix)):
        if pd.isnull(matrix[line, column]):
            matrix[line, column] = np.around(avg, 1)
