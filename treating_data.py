from converting_gender import *
from average_fare import *
from age_prediction import *
from converting_embark import *


def data_treatment(train_data, test_data):
    """
    :param train_data: Matrix
    :param test_data: Matrix
    :return: Preprocessed test data & train data
    """

    # Deleting useless data
    train_data = np.delete(train_data, [0, 3, 8, 10], 1)
    test_data = np.delete(test_data, [0, 2, 7, 9], 1)

    # Converting gender : Male = 1, female = 0
    gender_conversion(train_data, 2)
    gender_conversion(test_data, 1)

    # Gives data with no fare average of other fares
    average_fare(test_data, 5)

    # Converting embark : C = 0, S = 1, Q = 2
    embark_conversion(test_data, 6)
    embark_conversion(train_data, 7)

    # Using linear regression to give data with no age a predicted age
    age_prediction(train_data, 3)
    age_prediction(test_data, 2)

    return train_data, test_data
