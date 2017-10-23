
# coding: utf-8

# # Exploring with Visuals
# Use `clean_08.csv` and `clean_18.csv`

# In[3]:


# load datasets
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df_08 = pd.read_csv('clean_08.csv')
df_18 = pd.read_csv('clean_18.csv')


# In[21]:


#df_18.info()


# In[4]:


plt.hist(df_08['greenhouse_gas_score'], alpha=0.7)
plt.hist(df_18['greenhouse_gas_score'], alpha=0.7)
plt.title('Distributions of Greenhouse Gas')
plt.xlabel('Greenhouse Score')
plt.ylabel('Quantity')
plt.legend(['2008', '2018']);


# In[5]:


#plt.hist(df_08['cmb_mpg'], alpha=0.7)
#plt.hist(df_18['cmb_mpg'], alpha=0.7)
plt.hist(df_18['cmb_mpg'], range=[10, 70], bins=12, alpha=0.7)
plt.hist(df_08['cmb_mpg'], range=[10, 70], bins=12, alpha=0.7)
plt.title('Distributions of Combined MPG')
plt.xlabel('Combined MPG')
plt.ylabel('Quantity');
plt.legend(['2008', '2018']);


# In[14]:


x = df_18['displ']
y = df_18['cmb_mpg']
plt.scatter(x, y)
plt.title('Displacement vs Combined MPG')
plt.xlabel('Displacement')
plt.ylabel('Combined MPG');


# In[22]:


x = df_18['greenhouse_gas_score']
y = df_18['cmb_mpg']
plt.scatter(x, y)
plt.title('Greenhouse Gas vs Combined MPG')
plt.xlabel('Greenhouse Gas')
plt.ylabel('Combined MPG');


# In[ ]:




