
# coding: utf-8

# # Appending Data
# First, import the necessary packages and load `winequality-red.csv` and `winequality-white.csv`.

# In[23]:


# import numpy and pandas
import numpy as np
import pandas as pd

# load red and white wine datasets
red_df = pd.read_csv('winequality-red.csv', sep=';')
white_df = pd.read_csv('winequality-white.csv', sep=';')


# ## Create Color Columns
# Create two arrays as long as the number of rows in the red and white dataframes that repeat the value “red” or “white.” NumPy offers really easy way to do this. Here’s the documentation for [NumPy’s repeat](https://docs.scipy.org/doc/numpy/reference/generated/numpy.repeat.html) function. Take a look and try it yourself.

# In[24]:


# create color array for red dataframe

color_red = np.repeat('red', len(red_df))

# create color array for white dataframe
color_white = np.repeat('white', len(white_df))


# Add arrays to the red and white dataframes. Do this by setting a new column called 'color' to the appropriate array. The cell below does this for the red dataframe.

# In[27]:


red_df['color'] = color_red
red_df.rename(columns={"total_sulfur-dioxide": "total_sulfur_dioxide"}, inplace=True)
red_df.head()


# Do the same for the white dataframe and use `head()` to confirm the change.

# In[28]:


white_df['color'] = color_white
white_df.head()


# ## Combine DataFrames with Append
# Check the documentation for [Pandas' append](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.append.html) function and see if you can use this to figure out how to combine the dataframes. (Bonus: Why aren't we using the [merge](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.merge.html) method to combine the dataframes?) If you don’t get it, I’ll show you how afterwards. Make sure to save your work in this notebook! You'll come back to this later.

# In[29]:


# append dataframes
wine_df = white_df.append(red_df)

# view dataframe to check for success
wine_df.head()


# ## Save Combined Dataset
# Save your newly combined dataframe as `winequality_edited.csv`. Remember, set `index=False` to avoid saving with an unnamed column!

# In[32]:


wine_df.to_csv('winequality_edited.csv', index=False)
wines_df = pd.read_csv('winequality_edited.csv')
wines_df.info()


# In[ ]:




