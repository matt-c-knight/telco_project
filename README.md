# Telco Dataset Evaluation

## About The Project

### Goals

My goal for this project is to create a model that will predict customer churn using the telco dataset. My target variable is churn and I will evaluate a variety of independent variables to identify drivers of churn.

### Background

We are given a Sql dataset that we are importing and converting to a csv file. Then, we are using our skills in data prep to clean the data and make it possible to model. I will be using different models including logistic regression, decision tree, and random forrest. I will be looking for variable coefficients to predict possible relationships to churn.

## Data Dictionary

**customer_id**

**gender**

**senior_citizen**

**parnter**

**dependents**

**tenure**

**phone service**

**multiple_lines**

**internet_service_type_id**

**online_security**

**online_backup**

**device_protection**

**tech_support**

**streaming_tv**

**streaming_movies**

**contract_type_id**

**paperless_billing**

**payment_type_id**

**monthly_charges**

**total_charges**

**churn**

**contract_type**

**internet_service_type**

**payment_type**

## Initial Hypothesis 

Null Hypothesis- There is no correlation between churn and method of payment.

Alternative Hypothesis- There is a significant relationship between churn and method of payment.

## Project Plan: Breaking it Down

**acquire.py**

Acquire telco data from Sql and convert to a CSV file.

**prepare.py**

- Drop columns that are rendundant or not determined to be relevant for evaluation.
- Create dummy variables for non-numerical data.
- Convert columns with Yes/No into 1/0's.

**explore**

- Visualize the data 

- Test the hypothesis

**model**

- Use different algorthims looking for relationships

- Look for most relevent features

- Evaluate on train

- Select top model

- Run model on test data to verify

**conclusion**

- My baseline was 73% and the models came up with the same accuracy,
except when allowed for all variables, which produced an 80% accuracy.

- On the correlation I explored between churn and payment type, I was able to 
identify a strong relationship between churn and paying with electronic check(non-automatic payment).

- This correlation was backed up by the chi-squared hypothesis test, 
as well as the visualizations.







