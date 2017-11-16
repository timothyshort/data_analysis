# load dataset
import pandas as pd
import numpy as np
df = pd.read_csv('cancer_test_data.csv')
df.head()
df.info()

# number of patients
patients = df.count()[0]
df_cancer = df.query('has_cancer == True')
df_no_cancer = df.query('has_cancer == False')

# proportion of patients with / without cancer
df_cancer['has_cancer'].count() / patients
df_no_cancer['has_cancer'].count() / patients

# propotion of test results and cancer condition
df_cancer.query('test_result == "Positive"')['test_result'].count() / df_cancer.count()[0]
df_cancer.query('test_result == "Negative"')['test_result'].count() / df_cancer.count()[0]
df_no_cancer.query('test_result == "Positive"')['test_result'].count() / df_no_cancer.count()[0]
df_no_cancer.query('test_result == "Negative"')['test_result'].count() / df_no_cancer.count()[0]

# using baye's rule

# What proportion of patients who tested positive has cancer?
df1 = df.query('test_result == "Positive"')
df1.query('has_cancer == True').count()[0] / df1.count()[0]

# What proportion of patients who tested positive doesn't have cancer?
df1 = df.query('test_result == "Positive"')
df1.query('has_cancer == False').count()[0] / df1.count()[0]

# What proportion of patients who tested negative has cancer?
df1 = df.query('test_result == "Negative"')
df1.query('has_cancer == True').count()[0] / df1.count()[0]

# What proportion of patients who tested negative doesn't have cancer?
df1 = df.query('test_result == "Negative"')
df1.query('has_cancer == False').count()[0] / df1.count()[0]