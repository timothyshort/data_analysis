import numpy as np
import pandas as pd
import statsmodels.api as sm;

df = pd.read_csv('./house_prices.csv')
df.head()

df['intercept'] = 1
df_neighborhood = pd.get_dummies(df['neighborhood'])
df_style = pd.get_dummies(df['style'])
df_new = df.join(df_neighborhood)
df_new = df_new.join(df_style)
mod = sm.OLS(df['price'], df_new[['intercept', 'area', 'A', 'B', 'ranch', 'victorian']])
results = mod.fit()
results.summary()

#higher order model
df_new['area-squared'] = df_new['area'] * df_new['area']
mod = sm.OLS(df_new['price'], df_new[['intercept', 'area', 'area-squared', 'A', 'B', 'ranch', 'victorian']])
results = mod.fit()
results.summary()