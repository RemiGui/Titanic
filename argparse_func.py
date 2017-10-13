import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-T', '--train',
                    metavar='', required=True, type=str,
                    help="The train data file name")
parser.add_argument('-t', '--test',
                    metavar='', required=True, type=str,
                    help="The test data file name")
parser.add_argument('-v', '--validation',
                    metavar='', required=True, type=str,
                    help="The validation set file name")
parser.add_argument('-a', '--algorithm',
                    metavar='', required=True, type=str,
                    help="Algorithm used, linear_regression or decision_tree. If type error : decision "
                         "tree is used")
args = parser.parse_args()


