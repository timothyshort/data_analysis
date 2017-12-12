import numpy as np
import pandas as pd
import statsmodels.api as sm;

df = pd.read_csv('./house_price_area_only.csv')
df.head()

df['intercept'] = 1

lm = sm.OLS(df['price'], df[['intercept', 'area']])
mod = lm.fit()
mod.summary()