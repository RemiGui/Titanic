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
    for var_loop in range(len(matrix)):
        if pd.isnull(matrix[var_loop, column]):
            nul += 1
        else:
            sum += float(matrix[var_loop, column])

    avg = sum / (len(matrix) - nul)

    for var_loop in range(len(matrix)):
        if pd.isnull(matrix[var_loop, column]):
            matrix[var_loop, column] = np.around(avg, 1)