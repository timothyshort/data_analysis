import numpy as np
import pandas as pd
import statsmodels.api as sm

df = pd.read_csv("./admissions.csv")
df.head()

#get dummies for prestige
df['prestige'].value_counts()
df[['p_1', 'p_2', 'p_3', 'p_4']] = pd.get_dummies(df['prestige'])
df.head()

#multiple logistic regression model
df['intercept'] = 1
mod = sm.Logit(df['admit'], df[['intercept', 'gre', 'gpa', 'p_2', 'p_3', 'p_4']])
results = mod.fit()
results.summary()

#interpreations of results
1/np.exp(-1.5534)
1/np.exp(-1.3387)
1/np.exp(-.6801)
np.exp(.7793)