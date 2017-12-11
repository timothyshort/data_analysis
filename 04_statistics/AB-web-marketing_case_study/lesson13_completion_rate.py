import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
% matplotlib inline

np.random.seed(42)

df = pd.read_csv('classroom_actions.csv')
df.head()

# Create dataframe with all control records
control_df = df[df['group'] == "control"]

# Compute completion rate
control_ctr = control_df[control_df['completed'] == True].id.nunique() / control_df.id.nunique()

# Display completion rate
control_ctr

# Create dataframe with all experiment records
experiment_df = df[df['group'] == "experiment"]

# Compute completion rate
experiment_ctr = experiment_df[experiment_df['completed'] == True].id.nunique() / experiment_df.id.nunique()

# Display completion rate
experiment_ctr

# Compute observed difference in completion rates
obs_diff = experiment_ctr - control_ctr

# Display observed difference in completion rates
obs_diff

# Create sampling distribution for difference in completion rates with boostrapping
diffs = []
for _ in range(10000):
    b_sample = df.sample(df.shape[0], replace=True)
    b_control_df = b_sample[b_sample['group'] == "control"]
    b_experiment_df = b_sample[b_sample['group'] == "experiment"]
    b_control_ctr = b_control_df[b_control_df['completed'] == True].id.nunique() / b_experiment_df.id.nunique()
    b_experiment_ctr = b_experiment_df[b_experiment_df['completed'] == True].id.nunique() / b_experiment_df.id.nunique()
    diffs.append(b_experiment_ctr - b_control_ctr)

# convert to numpy array
diffs = np.array(diffs)

# plot distribution
plt.hist(diffs)

# create distribution under the null hypothesis
null_vals = np.random.normal(0, diffs.std(), diffs.size)

# plot null distribution
plt.hist(null_vals);

# plot line for observed statistic
plt.axvline(x=obs_diff, color='r');