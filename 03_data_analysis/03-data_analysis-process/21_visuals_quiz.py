
# coding: utf-8

# # Exploring Data with Visuals Quiz
# Use the space below to explore `powerplant_data_edited.csv` to answer the quiz questions below.

# In[4]:


# imports and load data
import pandas as pd
get_ipython().magic('matplotlib inline')

df = pd.read_csv('powerplant_data_edited.csv')
df.head()


# In[7]:


# plot relationship between temperature and electrical output
df.plot(x='Atmospheric Temperature in C', y='Power Output', kind='scatter');


# In[9]:


# plot distribution of humidity
df.hist('Relative Humidity');


# In[32]:


# plot box plots for each variable
df['Atmospheric Temperature in C'].plot(kind='box');


# In[33]:


df['Exhaust Vacuum Speed'].plot(kind='box');


# In[34]:


df['Atmospheric Pressure'].plot(kind='box');


# In[35]:


df['Relative Humidity'].plot(kind='box');


# In[36]:


df['Power Output'].plot(kind='box');


# In[ ]:




