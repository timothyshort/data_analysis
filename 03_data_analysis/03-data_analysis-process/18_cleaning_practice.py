
# coding: utf-8

# # Cleaning Practice
# Let's first practice handling missing values and duplicate data with `cancer_data_means.csv`.

# In[15]:


# import pandas and load cancer data
import pandas as pd
df = pd.read_csv("cancer_data_means.csv")

# check which columns have missing values with info()
df.info()


# In[18]:


# use means to fill in missing values
texture_mean = df['texture_mean'].mean()
smoothness_mean = df['smoothness_mean'].mean()
symmetry_mean = df['symmetry_mean'].mean()
print(texture_mean, smoothness_mean, symmetry_mean)

df['texture_mean'] = df['texture_mean'].fillna(texture_mean)
df['smoothness_mean'] = df['smoothness_mean'].fillna(smoothness_mean)
df['symmetry_mean'] = df['symmetry_mean'].fillna(symmetry_mean)

# confirm your correction with info()
df.info()


# In[23]:


# check for duplicates in the data
sum(df.duplicated())


# In[29]:


# drop duplicates
df.drop_duplicates(inplace=True)


# In[30]:


# confirm correction by rechecking for duplicates in the data
sum(df.duplicated())


# ## Renaming Columns
# Since we also previously changed our dataset to only include means of tumor features, the "_mean" at the end of each feature seems unnecessary. It just takes extra time to type in our analysis later. Let's come up with a list of new labels to assign to our columns.

# In[31]:


# remove "_mean" from column names
new_labels = []
for col in df.columns:
    if '_mean' in col:
        new_labels.append(col[:-5])  # exclude last 6 characters
    else:
        new_labels.append(col)

# new labels for our columns
new_labels


# In[32]:


# assign new labels to columns in dataframe
df.columns = new_labels

# display first few rows of dataframe to confirm changes
df.head()


# In[33]:


# save this for later
df.to_csv('cancer_data_edited.csv', index=False)


# In[ ]:




