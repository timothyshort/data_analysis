
# coding: utf-8

# # Drawing Conclusions Using Groupby

# In[5]:


# Load `winequality_edited.csv`
import pandas as pd
df = pd.read_csv('winequality_edited.csv')
df.head()


# ### Is a certain type of wine associated with higher quality?

# In[6]:


# Find the mean quality of each wine type (red and white) with groupby
df.groupby('color')['quality'].mean()


# ### What level of acidity receives the highest average rating?

# In[7]:


# View the min, 25%, 50%, 75%, max pH values with Pandas describe
df.describe()['pH']


# In[8]:


# Bin edges that will be used to "cut" the data into groups
bin_edges = [ 2.72, 3.11, 3.21, 3.32, 4.01] # Fill in this list with five values you just found


# In[15]:


# Labels for the four acidity level groups
bin_names = [ "High", "ModeratelyHigh", "Medium", "Low"] # Name each acidity level category


# In[16]:


# Creates acidity_levels column
df['acidity_levels'] = pd.cut(df['pH'], bin_edges, labels=bin_names)

# Checks for successful creation of this column
df.head()


# In[17]:


# Find the mean quality of each acidity level with groupby
df.groupby('acidity_levels')['quality'].mean()


# In[ ]:


# Save changes for the next section
df.to_csv('winequality_edited.csv', index=False)

