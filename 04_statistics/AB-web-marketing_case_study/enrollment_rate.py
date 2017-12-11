import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
% matplotlib inline

np.random.seed(42)

df = pd.read_csv('course_page_actions.csv')
df.head()

# Get dataframe with all records from control group
control_df = df.query('group == "control"')

# Compute click through rate for control group
control_ctr = control_df.query('action == "enroll"').id.nunique() / control_df.query('action == "view"').id.nunique()

# Display click through rate
control_ctr

# Get dataframe with all records from experiment group
experiment_df = df.query('group == "experiment"')

# Compute click through rate for experiment group
experiment_ctr = experiment_df.query('action == "enroll"').id.nunique() / experiment_df.query('action == "view"').id.nunique()

# Display click through rate
experiment_ctr

# Compute the observed difference in click through rates
obs_diff = experiment_ctr - control_ctr

# Display observed difference
obs_diff

# Create a sampling distribution of the difference in proportions with bootstrapping
diffs = []
for _ in range(10000):
    b_sample = df.sample(df.shape[0], replace=True)
    b_control_df = b_sample.query('group == "control"')
    b_control_ctr = b_control_df.query('action == "enroll"').id.nunique() / b_control_df.query('action == "view"').id.nunique()
    b_experiment_df = b_sample.query('group == "experiment"')
    b_experiment_ctr = b_experiment_df.query('action == "enroll"').id.nunique() / b_experiment_df.query('action == "view"').id.nunique()
    b_obs_diff = b_experiment_ctr - b_control_ctr
    diffs.append(b_obs_diff)

# Convert to numpy array
diffs = np.array(diffs)

# Plot sampling distribution
plt.hist(diffs);

# Simulate distribution under the null hypothesis
null_vals = np.random.normal(0, diffs.std(), diffs.size)

# Plot the null distribution
plt.hist(null_vals);

# Plot observed statistic with the null distibution
plt.hist(null_vals)
plt.axvline(x=obs_diff, color='r');

# Compute p-value
(null_vals > obs_diff).mean()