
# coding: utf-8

# # Assessing and Building Intuition
# Once you have your data loaded into dataframes, Pandas makes a quick investigation of the data really easy. Let's explore some helpful methods for assessing and building intuition about a dataset. We can use the cancer data from before to help us.

# In[1]:


import pandas as pd

df = pd.read_csv('cancer_data.csv')
df.head()


# In[2]:


# this returns a tuple of the dimensions of the dataframe
df.shape


# In[3]:


# this returns the datatypes of the columns
df.dtypes


# In[4]:


# although the datatype for diagnosis appears to be object, further
# investigation shows it's a string
type(df['diagnosis'][0])


# Pandas actually stores [pointers](https://en.wikipedia.org/wiki/Pointer_(computer_programming) to strings in dataframes and series, which is why `object` instead of `str` appears as the datatype. Understanding this is not essential for data analysis - just know that strings will appear as objects in Pandas.

# In[5]:


# this displays a concise summary of the dataframe,
# including the number of non-null values in each column
df.info()


# In[6]:


# this returns the number of unique values in each column
df.nunique()


# In[7]:


# this returns useful descriptive statistics for each column of data
df.describe()


# In[8]:


# this returns the first few lines in our dataframe
# by default, it returns the first five
df.head()


# In[9]:


# although, you can specify however many rows you'd like returned
df.head(20)


# In[10]:


# same thing applies to `.tail()` which returns the last few rows
df.tail(2)


# ## Indexing and Selecting Data in Pandas
# Let's separate this dataframe into three new dataframes - one for each metric (mean, standard error, and maximum). To get the data for each dataframe, we need to select the `id` and `diagnosis` columns, as well as the ten columns for that metric.

# In[11]:


# View the index number and label for each column
for i, v in enumerate(df.columns):
    print(i, v)


# We can select data using `loc` and `iloc`, which you can read more about [here](https://pandas.pydata.org/pandas-docs/stable/indexing.html). `loc` uses labels of rows or columns to select data, while `iloc` uses the index numbers. We'll use these to index the dataframe below.

# In[12]:


# select all the columns from 'id' to the last mean column
df_means = df.loc[:,'id':'fractal_dimension_mean']
df_means.head()


# In[13]:


# repeat the step above using index numbers
df_means = df.iloc[:,:11]
df_means.head()


# Let's save the dataframe of means for later.

# In[14]:


df_means.to_csv('cancer_data_means.csv', index=False)


# ### Selecting Multiple Ranges in Pandas
# Selecting the columns for the mean dataframe was pretty straightforward - the columns we needed to select were all together (`id`, `diagnosis`, and the mean columns). Now we run into a little issue when we try to do the same for the standard errors or maximum values. `id` and `diagnosis` are separated from the rest of the columns we need! We can't specify all of these in one range.
# 
# First, try creating the standard error dataframe on your own to see why doing this with just `loc` and `iloc` is an issue. Then, use this [stackoverflow link](https://stackoverflow.com/questions/41256648/select-multiple-ranges-of-columns-in-pandas-dataframe) to learn how to select multiple ranges in Pandas and try it below. By the way, to figure this out myself, I just found this link by googling "how to select multiple ranges df.iloc"

# In[22]:


# create the standard errors dataframe
df_se = df.loc[:,'radius_SE':'fractal_dimension_SE']

# view the first few rows to confirm this was successful
df_se.head()


# In[25]:


# create the maximum values dataframe
df_max = df.iloc[:,22:]

# view the first few rows to confirm this was successful
df_max.head()


# In[ ]:




