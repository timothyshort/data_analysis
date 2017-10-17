
# coding: utf-8

# # Plotting Wine Type and Quality with Matplotlib

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
import seaborn as sns
sns.set_style('darkgrid')

wine_df = pd.read_csv('winequality_edited.csv')


# ### Create arrays for red bar heights white bar heights
# Remember, there's a bar for each combination of color and quality rating. Each bar's height is based on the proportion of samples of that color with that quality rating.
# 1. Red bar proportions = counts for each quality rating / total # of red samples
# 2. White bar proportions = counts for each quality rating / total # of white samples

# In[6]:


# get counts for each rating and color
color_counts = wine_df.groupby(['color', 'quality']).count()['pH']
color_counts


# In[7]:


# get total counts for each color
color_totals = wine_df.groupby('color').count()['pH']
color_totals


# In[8]:


# get proportions by dividing red rating counts by total # of red samples
red_proportions = color_counts['red'] / color_totals['red']
red_proportions


# In[9]:


# get proportions by dividing white rating counts by total # of white samples
white_proportions = color_counts['white'] / color_totals['white']
white_proportions


# ### Plot proportions on a bar chart
# Set the x coordinate location for each rating group and and width of each bar.

# In[15]:


ind = np.arange(len(red_proportions))  # the x locations for the groups
width = 0.35       # the width of the bars


# Now let’s create the plot.

# In[16]:


# plot bars
red_bars = plt.bar(ind, red_proportions, width, color='r', alpha=.7, label='Red Wine')
white_bars = plt.bar(ind + width, white_proportions, width, color='w', alpha=.7, label='White Wine')

# title and labels
plt.ylabel('Proportion')
plt.xlabel('Quality')
plt.title('Proportion by Wine Color and Quality')
locations = ind + width / 2  # xtick locations
labels = ['3', '4', '5', '6', '7', '8', '9']  # xtick labels
plt.xticks(locations, labels)

# legend
plt.legend()


# Oh, that didn't work because we're missing a red wine value for a the 9 rating. Even though this number is a 0, we need it for our plot. Run the last two cells after running the cell below.

# In[14]:


red_proportions['9'] = 0
red_proportions


# In[ ]:




