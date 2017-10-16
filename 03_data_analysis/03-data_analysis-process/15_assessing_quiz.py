
# coding: utf-8

# # Assessing and Building Intuition Quiz
# Use the space below to explore `census_income_data.csv` to answer the quiz questions below.

# In[9]:


# Import pandas
import pandas as pd

# Load census income data
df_census = pd.read_csv('census_income_data.csv')
df_census.head()


# In[11]:


# Work to answer the quiz questions

df_census.info()
df_census.describe()
df_census.nunique()


# In[ ]:




