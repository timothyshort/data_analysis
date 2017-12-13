import numpy as np
import pandas as pd
import statsmodels.api as sm;

df = pd.read_csv('./house_prices.csv')
df.head()

df['intercept']=1

#simple linear regression models
lm = sm.OLS(df['price'], df[['intercept', 'area']])
results = lm.fit()
results.summary()

#multiple linear regression model
mlr = sm.OLS(df['price'], df[['intercept', 'bathrooms', 'bedrooms', 'area']])
results = mlr.fit()
results.summary()

#using dummy variables for neighborhood categorical variables
df_neighborhood = pd.get_dummies(df['neighborhood'])
df_new = df.join(df_neighborhood)
df_new['intercept'] = 1
df_new.head()

#mlr with neighborhood categorical transformation
mod = sm.OLS(df_new['price'], df_new[['intercept', 'B', 'C']])
results = mod.fit()
results.summary()

#plot histograms of home values by neighborhood
plt.hist(df_new.query("C == 1")['price'], alpha = 0.3, label = 'C');
plt.hist(df_new.query("A == 1")['price'], alpha = 0.3, label = 'A');
plt.hist(df_new.query("A == 1")['price'], alpha = 0.3, label = 'B');
plt.legend();

#add dummy variables for house style categorial variables
df_style = pd.get_dummies(df['style'])
df_new = df_new.join(df_style)
df_new.head()

#mlr for neighborhood and style categorical variables
mod = sm.OLS(df_new['price'], df_new[['intercept', 'lodge', 'victorian', 'A', 'B', 'C', 'bathrooms', 'bedrooms']])
results = mod.fit()
results.summary()