# Titanic


<h3> To run the script, in terminal : </h3>

<p> python main.py -T train.csv -t test.csv -v gender_submission.csv -a decision tree </p>

<p> It will run the best accuracy (around 92%) </p>



<h3> You can also do the -h command in terminal : </h3>

<p> python main.py -h </p>

<p> You will have the description of each option </p>

<h3> Used Libraries : </h3>
<ul>
<li> Pandas </li>
<li> Numpy </li>
<li> Argparse </li>
<li> Sklearn </li>
</ul>

<h3> Functions description : </h3>
<ul>
<li> main.py : Used to execute the script </li>

<li> age_prediction.py : Fills age column with an age prediction
		        Used in treating_data.py </li>

<li> argparse_func.py : Creates options to run to script with command-lines </li>

<li> average_fare.py : Fills fare column with average fare
                             Used in treating_data.py </li>

<li> converting_embark.py : Converts embarks string to int
                                       Used in treating_data.py </li>

<li> converting_gender.py : Converts gender strings to int (binary, male = 1, female = 0) </li>

<li> decision_tree.py : Performs decision tree algorithm
                              Used in performing_algorithm.py </li>

<li> input_data.py : extracts data from csv files with pandas and converts them to numpy arrays </li>

<li> linear_regression.py : Performs linear regression algorithm
                                   Used in performing_algorithm.py </li>

<li> performing_algorithm.py : Performs algorithm chosen by user
			        Used in main.py </li>

<li> preparing_data.py : Prepares the train and test data for algorithms
		        Used in main.py </li>

<li> treating_data.py : Preprocessing the test and train data
		     used in main.py </li>
</ul>

