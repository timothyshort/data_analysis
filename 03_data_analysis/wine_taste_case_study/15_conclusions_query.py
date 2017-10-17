
# coding: utf-8

# # Drawing Conclusions Using Query

# In[2]:


# Load `winequality_edited.csv`
import pandas as pd

df = pd.read_csv('winequality_edited.csv')
df.head()


# ### Do wines with higher alcoholic content receive better ratings?

# In[15]:


# get the median amount of alcohol content
alcohol_med = df['alcohol'].median()


# In[47]:


# select samples with alcohol content less than the median
low_alcohol = df.query('alcohol < {}'.format(alcohol_med))

# select samples with alcohol content greater than or equal to the median
high_alcohol = df.query('alcohol >= {}'.format(alcohol_med))

# ensure these queries included each sample exactly once
num_samples = df.shape[0]
num_samples == low_alcohol['quality'].count() + high_alcohol['quality'].count() # should be True


# In[48]:


# get mean quality rating for the low alcohol and high alcohol groups
print("Low Alcohol Quality:", low_alcohol['quality'].mean())
print("High Alcohol Quality:", high_alcohol['quality'].mean())


# ### Do sweeter wines receive better ratings?

# In[44]:


# get the median amount of residual sugar
rs_med = df['residual_sugar'].median()


# In[51]:


# select samples with residual sugar less than the median
low_sugar = df.query('residual_sugar < {}'.format(rs_med))

# select samples with residual sugar greater than or equal to the median
high_sugar = df.query('residual_sugar >= {}'.format(rs_med))

# ensure these queries included each sample exactly once
num_samples == low_sugar['quality'].count() + high_sugar['quality'].count() # should be True


# In[56]:


# get mean quality rating for the low sugar and high sugar groups
print("Low Sugar Quality:", low_sugar['quality'].mean())
print("High Sugar Quality:", high_sugar['quality'].mean())


# In[ ]:




