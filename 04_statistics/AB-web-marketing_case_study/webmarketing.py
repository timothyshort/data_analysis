import pandas as pd

df = pd.read_csv('homepage_actions.csv')
df.head()

# total number of actions
df.count()[0]

# number of unique users
df['id'].nunique()

# size of control group and experiment group
df.groupby('group')['id'].nunique()

# duration of this experiment
from datetime import datetime
end_date = datetime.strptime(df['timestamp'].iloc[-1], "%Y-%m-%d %H:%M:%S.%f")
start_date = datetime.strptime(df['timestamp'].iloc[0], "%Y-%m-%d %H:%M:%S.%f")
test_duration = end_date - start_date
print("Duration: {}".format(test_duration))

# action types in this experiment
df.groupby('action').nunique()