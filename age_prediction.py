from linear_regression import *
import pandas as pd
from decision_tree import *


def age_prediction(matrix, column):
    """
    :param matrix: Matrix
    :param column: Int
    :return: Filled age column with predicted age
    """
    train_age = []
    test_age = []
    index = []
    for line in range(len(matrix)):
        if pd.isnull(matrix[line][column]):
            test_age.append(matrix[line])
            index.append(line)
        else:
            train_age.append(matrix[line])

    test_age = np.array(test_age)
    train_age = np.array(train_age)

    X_age = np.delete(train_age, [column], 1)
    X_age = X_age.astype(np.float)
    y_age = train_age[:, column]
    y_age = y_age.astype(np.int)
    X_test_age = np.delete(test_age, [column], 1)
    X_test_age = X_test_age.astype(np.float)

    predicted_age = linear_regression(X_age, y_age, X_test_age)

    for line in range(len(predicted_age)):
        if predicted_age[line] < 0:
            predicted_age[line] = 1

    var = 0
    for line in range(len(matrix)):
        if pd.isnull(matrix[line][column]):
            matrix[line][column] = predicted_age[var]
            var += 1
