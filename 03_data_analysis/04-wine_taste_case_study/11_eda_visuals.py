
# coding: utf-8

# # EDA with Visuals
# Create visualizations to answer the quiz questions below this notebook.

# In[6]:


# Load dataset
import pandas as pd
get_ipython().magic('matplotlib inline')

wines_df = pd.read_csv('winequality_edited.csv')
wines_df.head()


# ### Histograms for Various Features

# In[43]:


wines_df['fixed_acidity'].hist().set_title('Distribution to Fixed Acidity');


# In[44]:


wines_df['total_sulfur_dioxide'].hist().set_title('Distribution to Total Sulfur Dioxide');


# In[45]:


wines_df['pH'].hist().set_title('Distribution to pH');


# In[46]:


wines_df['alcohol'].hist().set_title('Distribution to Alcohol');


# ### Scatterplots of Quality Against Various Features

# In[38]:


wines_df.plot(x='volatile_acidity', y='quality', kind='scatter',
              title='Volatile Acidity vs Quality');


# In[47]:


wines_df.plot(x='residual_sugar', y='quality', kind='scatter',
              title='Residual Sugar vs Quality');


# In[48]:


wines_df.plot(x='pH', y='quality', kind='scatter',
              title='pH vs Quality');


# In[49]:


wines_df.plot(x='alcohol', y='quality', kind='scatter',
              title='Alcohol vs Quality');


# In[ ]:




