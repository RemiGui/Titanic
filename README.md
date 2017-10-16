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
	<li> 
		main.py :
		<ul>
		<li> Used to execute the script </li>
		</ul>
	</li>
	<li> 
		age_prediction.py : 
		<ul>
		<li> Fills age column with an age prediction </li>
		<li> Used in treating_data.py </li>
		</ul>
	</li>
	<li> 
		argparse_func.py : 
		<ul>
		<li> Creates options to run to script with command-lines </li>
		</ul>
	</li>
	<li> 
		average_fare.py : 
		<ul>
		<li> Fills fare column with average fare </li> 
        	<li> Used in treating_data.py </li> 
		</ul>
	</li>
	<li> 
		converting_embark.py : 
		<ul>
		<li> Converts embarks string to int </li> 
        	<li> Used in treating_data.py </li> 
		</ul>
	</li>
	<li> 
		converting_gender.py :
		<ul>
		<li> Converts gender strings to int (binary, male = 1, female = 0) </li> 
		<li> Used in treating_data.py </li> 
		</ul>
	</li>
	<li> 
		decision_tree.py : 
		<ul>
		<li> Performs decision tree algorithm </li> 
        	<li> Used in performing_algorithm.py </li> 
		</ul>
	</li>
	<li> 
		input_data.py : 
		<ul>
		<li> Extracts data from csv files with pandas and converts them to numpy arrays </li> 
		</ul>
	</li>
	<li> 
		linear_regression.py : 
		<ul>
		<li> Performs linear regression algorithm </li> 
        	<li> Used in performing_algorithm.py </li> 
		</ul>
	</li>
	<li> 
		performing_algorithm.py : 
		<ul>
		<li> Performs algorithm chosen by user </li> 
		<li> Used in main.py </li> 
		</ul>
	</li>
	<li> 
		preparing_data.py :
		<ul>
		<li> Prepares the train and test data for algorithms </li> 
		<li> Used in main.py </li> 
		</ul>
	</li>
	<li> 
		SVM.py : 
		<ul>
		<li> Performs SVM algorithm </li> 
        	<li> Used in performing_algorithm.py </li> 
		</ul>
	</li>
	<li> 
		treating_data.py : 
		<ul>
		<li> Preprocessing the test and train data </li> 
		<li> Used in main.py </li> 
		</ul>
	</li>
</ul>

