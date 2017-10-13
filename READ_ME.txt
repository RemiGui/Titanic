READ ME :


To run the script, in terminal :

python main.py -T train.csv -t test.csv -v gender_submission.csv -a decision tree

It will run the best accuracy (around 92%)



You can also do the -h command in terminal :

python main.py -h

You will have the description of each option



Functions description :

main.py : Used to execute the script

age_prediction.py : Fills age column with an age prediction
		        Used in treating_data.py

argparse_func.py : Creates options to run to script with command-lines

average_fare.py : Fills fare column with average fare
                             Used in treating_data.py

converting_embark.py : Converts embarks string to int
                                       Used in treating_data.py

converting_gender.py : Converts gender strings to int (binary, male = 1, female = 0)

decision_tree.py : Performs decision tree algorithm
                              Used in performing_algorithm.py

input_data.py : extracts data from csv files with pandas and converts them to numpy arrays

linear_regression.py : Performs linear regression algorithm
                                   Used in performing_algorithm.py

performing_algorithm.py : Performs algorithm chosen by user
			        Used in main.py

preparing_data.py : Prepares the train and test data for algorithms
		        Used in main.py

treating_data.py : Preprocessing the test and train data
		     used in main.py



