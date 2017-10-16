
# coding: utf-8

# # Drawing Conclusions Quiz
# Use the space below to explore `store_data.csv` to answer the quiz questions below.

# In[47]:


# imports and load data
import pandas as pd
get_ipython().magic('matplotlib inline')

df = pd.read_csv('store_data.csv')


# In[151]:


# explore data
df.head()
#df.info()
#df.describe()


# In[140]:


# total sales for the last month
df_total_sales = df.loc[:,'storeA' : 'storeE']
print(sum(df_total_sales.sum()))


# In[148]:


# average sales
df_average_sales = df.loc[:,'storeA' : 'storeE']
print(df_average_sales.mean().mean())


# In[142]:


# sales on march 13, 2016
df[df['week'] == '2016-03-13']


# In[143]:


# worst week for store C
storeC_min = df['storeC'].min()
df[df['storeC'] == storeC_min]


# In[145]:


# total sales during most recent 3 month period
recent_sales = df.tail(3)
sales = recent_sales.loc[:,"storeA" : "storeE"]
print(sales)
print(sum(sales.sum()))


# In[157]:


#Question 1
last_month_sales = df.tail(1)
last_month_sales.loc[:,"storeA" : "storeE"]

#Question 2
df.describe()

#Question 3
df[df['week'] == '2016-03-13']

#Question 5
recent_sales.sum()


# In[ ]:




