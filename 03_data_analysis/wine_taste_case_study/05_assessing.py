
# coding: utf-8

# # Assessing
# Use the space below to explore `winequality-red.csv` and `winequality-white.csv` to answer the quiz questions below.

# In[26]:


import pandas as pd

print("RED")
df_red = pd.read_csv('winequality-red.csv', sep=';')
#df_red.head()
#df_red.info()
#sum(df_red.duplicated())
#df_red['quality'].nunique()
df_red['density'].mean()


# In[25]:


print("\nWHITE")
df_white = pd.read_csv('winequality-white.csv', sep=';')
#df_white.head()
#df_white.info()
#sum(df_white.duplicated())
df_white['quality'].nunique()


# In[ ]:




