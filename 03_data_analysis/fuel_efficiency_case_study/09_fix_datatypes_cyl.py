
# coding: utf-8

# # Fixing `cyl` Data Type
# - 2008: extract int from string
# - 2018: convert float to int

# In[15]:


# load datasets
import pandas as pd
df_08 = pd.read_csv('data_08.csv')
df_18 = pd.read_csv('data_18.csv')


# In[16]:


# check value counts for the 2008 cyl column
df_08['cyl'].value_counts()


# Read [this](https://stackoverflow.com/questions/35376387/extract-int-from-string-in-pandas) to help you extract ints from strings in Pandas for the next step.

# In[17]:


# Extract int from strings in the 2008 cyl column
df_08['cyl'] = df_08['cyl'].str.extract('(\d+)').astype(int)


# In[18]:


# Check value counts for 2008 cyl column again to confirm the change
df_08['cyl'].value_counts()


# In[19]:


# convert 2018 cyl column to int
df_18['cyl'] = df_18['cyl'].astype(int)


# In[20]:


df_18['cyl'].value_counts()


# In[21]:


df_08.to_csv('data_08.csv', index=False)
df_18.to_csv('data_18.csv', index=False)


# In[ ]:




