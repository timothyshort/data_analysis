
# coding: utf-8

# # Filter, Drop Nulls, Dedupe
# Use `data_08.csv` and `data_18.csv`

# In[1]:


# load datasets
import pandas as pd

df_08 = pd.read_csv('data_08.csv')
df_18 = pd.read_csv('data_18.csv')


# In[2]:


# view dimensions of dataset
df_08.shape


# In[3]:


# view dimensions of dataset
df_18.shape


# ## Filter by Certification Region

# In[13]:


# filter datasets for rows following California standards
df_08 = df_08[df_08['cert_region'] == 'CA']
df_18 = df_18[df_18['cert_region'] == 'CA']


# In[14]:


# confirm only certification region is California
df_08['cert_region'].unique()


# In[15]:


# confirm only certification region is California
df_18['cert_region'].unique()


# In[17]:


# drop certification region columns form both datasets
df_08.drop(['cert_region'], axis=1, inplace=True)
df_18.drop(['cert_region'], axis=1, inplace=True)


# In[18]:


df_08.shape


# In[19]:


df_18.shape


# ## Drop Rows with Missing Values

# In[32]:


# view missing value count for each feature in 2008
df_08[df_08.isnull().any(axis=1)]


# In[33]:


# view missing value count for each feature in 2018
df_18[df_18.isnull().any(axis=1)]


# In[35]:


# drop rows with any null values in both datasets
df_08.dropna(axis=0, how='any', inplace=True)
df_18.dropna(axis=0, how='any', inplace=True)


# In[36]:


# checks if any of columns in 2008 have null values - should print False
df_08.isnull().sum().any()


# In[37]:


# checks if any of columns in 2018 have null values - should print False
df_18.isnull().sum().any()


# ## Dedupe Data

# In[40]:


# print number of duplicates in 2008 and 2018 datasets
sum(df_08.duplicated())
sum(df_18.duplicated())


# In[41]:


# drop duplicates in both datasets
df_08.drop_duplicates(inplace=True)
df_18.drop_duplicates(inplace=True)


# In[43]:


# print number of duplicates again to confirm dedupe - should both be 0
sum(df_08.duplicated())
sum(df_18.duplicated())


# In[44]:


# save progress for the next section
df_08.to_csv('data_08.csv', index=False)
df_18.to_csv('data_18.csv', index=False)


# In[ ]:




