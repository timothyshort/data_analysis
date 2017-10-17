
# coding: utf-8

# # Plotting with Matplotlib
# Use Matplotlib to create bar charts that visualize the conclusions you made with groupby and query.

# In[168]:


# Import necessary packages and load `winequality_edited.csv`
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

df = pd.read_csv('winequality_edited.csv')
df.head()


# ### #1: Do wines with higher alcoholic content receive better ratings?
# Create a bar chart with one bar for low alcohol and one bar for high alcohol wine samples. This first one is filled out for you.

# In[169]:


# Use query to select each group and get its mean quality
median = df['alcohol'].median()
low = df.query('alcohol < {}'.format(median))
high = df.query('alcohol >= {}'.format(median))

mean_quality_low = low['quality'].mean()
mean_quality_high = high['quality'].mean()


# In[170]:


# Create a bar chart with proper labels
locations = [1, 2]
heights = [mean_quality_low, mean_quality_high]
labels = ['Low', 'High']
plt.bar(locations, heights, tick_label=labels)
plt.title('Average Quality Ratings by Alcohol Content')
plt.xlabel('Alcohol Content')
plt.ylabel('Average Quality Rating');


# ### #2: Do sweeter wines receive higher ratings?
# Create a bar chart with one bar for low residual sugar and one bar for high residual sugar wine samples.

# In[171]:


# Use query to select each group and get its mean quality
sugar_med = df['residual_sugar'].median()
low_sugar = df.query('residual_sugar < {}'.format(sugar_med))
high_sugar = df.query('residual_sugar >= {}'.format(sugar_med))

low_sugar_quality = low_sugar['quality'].mean()
high_sugar_quality = high_sugar['quality'].mean()


# In[172]:


# Create a bar chart with proper labels

locations = [1,2]
data = [low_sugar_quality, high_sugar_quality]
labels = ['Low', 'High']
plt.bar(locations, data, tick_label=labels)
plt.title("Average Quality Ratings by Residual Sugar Content")
plt.xlabel("Residual Quantity Content")
plt.ylabel("Quality");


# ### #3: What level of acidity receives the highest average rating?
# Create a bar chart with a bar for each of the four acidity levels.

# In[173]:


# Use groupby to get the mean quality for each acidity level
acidities = df.groupby('acidity_levels').mean()

acidity_lows = df.query('acidity_levels=="Low"')['quality'].mean()
acidity_meds = df.query('acidity_levels=="Medium"')['quality'].mean()
acidity_modhigh = df.query('acidity_levels=="ModeratelyHigh"')['quality'].mean()
acidity_high = df.query('acidity_levels=="High"')['quality'].mean()


# In[174]:


# Create a bar chart with proper labels
locations = [1,2,3,4]
labels = ["Low", "Medium", "Moderately High", "High"]
data = [acidity_lows, acidity_meds, acidity_modhigh, acidity_high]
plt.bar(locations, data, tick_label=labels)
plt.title("Average Quality Rating by Acidity Levels")
plt.xlabel("Acidity Level")
plt.ylabel("Average Quality Rating");


# ### Bonus: Create a line plot for the data in #3
# You can use pyplot's [plot](https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot) function for this.

# In[191]:


#x = df.groupby('quality').nunique()
y = df.groupby('quality')['pH'].mean()
x = df.groupby('quality')['quality'].mean()
plt.plot(x,y);
plt.title("Wine Quality vs pH Level")
plt.xlabel("Quality")
plt.ylabel("pH")


# Compare this with the bar chart. How might showing this visual instead of the bar chart affect someone's conclusion about this data?
