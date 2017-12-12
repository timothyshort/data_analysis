import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
%matplotlib inline

df = pd.read_csv('./carats.csv', header= None)
df.columns = ['carats', 'price']
df.head()

df['intercept'] = 1
mod = sm.OLS(df['price'], df[['intercept', 'carats']])
results = mod.fit()
results.summary()

plt.scatter(df['carats'], df['price']) 