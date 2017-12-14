import numpy as np
import pandas as pd
import statsmodels.api as sm


df = pd.read_csv('./fraud_dataset.csv')
df.head()

df[['weekday', 'weekend']] = pd.get_dummies(df['day'])
df[['not_fraud', 'is_fraud']] = pd.get_dummies(df['fraud'])
df.head()

#proportion of fraudulent transactions
df[df['is_fraud'] == 1 ].count()[0] / df.count()[0]

#average duration for fraudulant transactions
df.query('not_fraud == 0')['duration'].mean()

#porpotion of weekend transactions
df['weekday'].mean()

#average duration of non-fraudulant transactions
df.query('fraud == False')['duration'].mean()