from input_data import *
from performing_algorithm import *
from preparing_data import *
from treating_data import *
from sklearn.metrics import accuracy_score

# Preprocessing data
train_data, test_data = data_treatment(train_data, test_data)

# Preparing features and labels for algorithm
X, y, X_test = preparing_data(train_data, test_data)

# Performing chosen algorithm
prediction = performing_algorithm(X, y, X_test)

# Displaying accuracy of prediction
print "Accuracy of algorithm"
print accuracy_score(prediction, validation)
