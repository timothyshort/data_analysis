
# coding: utf-8

# In[35]:


# imports and load data
import pandas as pd
get_ipython().magic('matplotlib inline')
df = pd.read_csv('store_data.csv')


# In[36]:


# explore data
#df.head()
df.describe()


# In[53]:


# sales for the last month
df.iloc[-1, 1:].plot(kind='bar', figsize=(8,5),
                     title='Store Sales for Last Month');


# In[74]:


# average sales
df.iloc[:,1:].mean().plot(kind='bar', figsize=(8,5),
                          title="Average Store Sales")


# In[92]:


# sales for the week of March 13th, 2016
df[df['week'] == '2016-03-13'].plot(kind='bar')


# In[106]:


# sales for the lastest 3-month periods
df.iloc[-1, 1:6].plot(kind='pie', figsize=(8,8),
                     title = 'Store Sales for Last 3 Months')


# In[ ]:




