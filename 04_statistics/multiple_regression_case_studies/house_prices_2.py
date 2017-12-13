import pandas as pd
import numpy as np
import seaborn as sns
from patsy import dmatrices
import statsmodels.api as sm;
from statsmodels.stats.outliers_influence import variance_inflation_factor
%matplotlib inline

df = pd.read_csv('./house_prices.csv')
df.head()

#compare variables pairwise
sns.pairplot(df[['bedrooms', 'bathrooms', 'area']]);

#linear regression model
df['intercept'] = 1
mod = sm.OLS(df['price'], df[['intercept', 'bedrooms', 'bathrooms', 'area']])
results = mod.fit()
results.summary()

#calculate VIF to determine collinearity
y, X = dmatrices('price ~ area + bedrooms + bathrooms', df, return_type='dataframe')
vif = pd.DataFrame();
vif['VIF_Factor'] = [variance_inflation_factor(X.values,i) for i in range(X.shape[1])]
vif['features'] = X.columns
vif

#modify MLR with VIF in mind (remove bathrooms from model)
mod = sm.OLS(df['price'], df[['intercept', 'area', 'bedrooms']])
results = mod.fit()
results.summary()

#VIF
y, X = dmatrices('price ~ area + bedrooms', df, return_type='dataframe')
vif = pd.DataFrame();
vif['VIF_Factor'] = [variance_inflation_factor(X.values,i) for i in range(X.shape[1])]
vif['features'] = X.columns
vif