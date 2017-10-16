
# coding: utf-8

# # Reading CSV Files
# Let's practice reading csv files with this toy dataset on student scores. As you've seen a few times already, `read_csv()` is used to load data from csv files into a Pandas dataframe. We just need to specify the filepath of our data. I stored `student_scores.csv` in the same directory as this Jupyter notebook, so we just need to provide the name of the file.
# 
# Run each cell as you go through this Jupyter notebook.

# In[1]:


import pandas as pd

df = pd.read_csv('student_scores.csv')


# `head()` is a useful function you can call on your dataframe to display the first few rows. Let's use it to see what this data looks like.

# In[6]:


df.head(2)


# Remember, CSV stands for comma separated values - but they can actually be separated by different characters, tabs, white space, etc. If your file is separated by a colon, let's say, you can still use `read_csv()` with the `sep` parameter.

# In[8]:


df = pd.read_csv('student_scores.csv', sep=',')
df.head()


# This obviously didn't work because there our CSV file is separated by commas. Because there are no colons, nothing was separated and everything was read into one column!

# ## Headers
# Another thing you can do with `read_csv` is specify which line of the file is the header, which specifies the column labels. It's usually the first line, but sometimes we'll want to specify a later line if there is extra meta information at the top of the file. We can do that like this.

# In[10]:


df = pd.read_csv('student_scores.csv', header=1)
df.head()


# Here, row 2 was used as the the header and everything above that was cut off. By default, `read_csv` uses header=0, which uses the first line for column labels.

# If columns labels are not included in your file, you can use `header=None` to prevent your first line of data from being misinterpreted as column labels.

# In[11]:


df = pd.read_csv('student_scores.csv', header=None)
df.head()


# You can also specify your own column labels like this.

# In[12]:


labels = ['id', 'name', 'attendance', 'hw', 'test1', 'project1', 'test2', 'project2', 'final']
df = pd.read_csv('student_scores.csv', names=labels)
df.head()


# If you want to tell pandas that there was a header line that you are replacing, you can specify the row of that line like this.

# In[13]:


labels = ['id', 'name', 'attendance', 'hw', 'test1', 'project1', 'test2', 'project2', 'final']
df = pd.read_csv('student_scores.csv', header=0, names=labels)
df.head()


# ## Index
# Instead of using the default index (integers incrementing by 1 from 0), you can specify one or more of your columns to be the index of your dataframe.

# In[14]:


df = pd.read_csv('student_scores.csv', index_col='Name')
df.head()


# In[15]:


df = pd.read_csv('student_scores.csv', index_col=['Name', 'ID'])
df.head()


# There are many other things you can do with this function alone, such as parsing dates, filling null values, skipping rows, etc. A lot of these can be done in different steps after `read_csv()`. We're going to modify our data in other ways, but you can always look up how to do some steps with this function [here](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html).

# ## Quiz #1
# Use `read_csv()` to read in `cancer_data.csv` and use an appropriate column as the index. Then, use `.head()` on your dataframe to see if you've done this correctly. *Hint: First call `read_csv()` without parameters to see what the data looks like.*

# In[20]:


df_cancer = pd.read_csv("cancer_data.csv", index_col="id")
df_cancer.head()


# ## Quiz #2
# Use `read_csv()` to read in `powerplant_data.csv` with more descriptive column names based on the description of features on this [website](http://archive.ics.uci.edu/ml/datasets/combined+cycle+power+plant). Then, use `.head()` on your dataframe to see if you've done this correctly. *Hint: First call `read_csv()` without parameters to see what the data looks like.*

# In[33]:


pp_labels = ["Atmospheric Temperature in C", "Exhaust Vacuum Speed",
             "Atmospheric Pressure", "Relative Humidity", "Power Output"]
df_powerplant = pd.read_csv("powerplant_data.csv", header=0, names=pp_labels)
df_powerplant.head()


# # Writing CSV Files
# Awesome! Now, we'll save your second dataframe with power plant data into a csv file for the next section.

# In[34]:


df_powerplant.to_csv('powerplant_data_edited.csv')


# Let's see if that worked the way we wanted.

# In[35]:


df = pd.read_csv('powerplant_data_edited.csv')
df.head()


# What's this `Unnamed:0`? `to_csv()` will store our index unless we tell it not to. To make it ignore the index, we have to provide the parameter `index=False`

# In[30]:


df_powerplant.to_csv('powerplant_data_edited.csv', index=False)


# In[36]:


df = pd.read_csv('powerplant_data_edited.csv')
df.head()


# In[ ]:





# In[ ]:




