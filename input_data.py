import numpy as np
import pandas as pd
from argparse_func import *


# Extracting data from csv file
train_data = pd.read_csv(args.train)
# Converting array to Numpy array
train_data = np.array(train_data)

# Extracting data from csv file
test_data = pd.read_csv(args.test)
# Converting array to Numpy array
test_data = np.array(test_data)


# Extracting data from csv
validation = pd.read_csv(args.validation)
# Converting array to Numpy array & keeping only 2nd column
validation = np.array(validation)
validation = validation[:, 1]
validation = validation.astype(np.int)
