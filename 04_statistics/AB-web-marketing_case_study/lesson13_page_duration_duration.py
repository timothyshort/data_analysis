import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
% matplotlib inline

np.random.seed(42)

df = pd.read_csv('classroom_actions.csv')
df.head()

# get the average classroom time for control group
control_mean = df.query('group == "control"')['total_days'].mean()

# get the average classroom time for experiment group
experiment_mean = df.query('group == "experiment"')['total_days'].mean()

# display average classroom time for each group
control_mean, experiment_mean

# compute observed difference in classroom time
obs_diff = experiment_mean - control_mean

# display observed difference
obs_diff

# create sampling distribution of difference in average classroom times with boostrapping
diffs = []
for _ in range(10000):
    b_sample = df.sample(df.shape[0], replace=True)
    b_control_mean = b_sample.query('group == "control"')['total_days'].mean()
    b_experiment_mean = b_sample.query('group == "experiment"')['total_days'].mean()
    diffs.append(b_experiment_mean - b_control_mean)

# convert to numpy array
diffs = np.array(diffs)

# simulate distribution under the null hypothesis
null_vals = np.random.normal(0, diffs.std(), diffs.size)

# plot null distribution
plt.hist(null_vals)

# plot line for observed statistic
plt.axvline(x=obs_diff, color='r')

# compute p value
(null_vals > obs_diff).mean()