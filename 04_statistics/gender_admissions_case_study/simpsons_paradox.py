
# coding: utf-8

# # Simpson's Paradox
# Use `admission_data.csv` for this exercise.

# In[10]:


# Load and view first few lines of dataset
import pandas as pd
df = pd.read_csv('admission_data.csv')
df.head()


# ### Proportion and admission rate for each gender

# In[11]:


# Proportion of students that are female
girls = df.query('gender == "female"').count()[1]
total = df.count()[1]
girls / total


# In[12]:


# Proportion of students that are male
guys = df.query('gender == "male"').count()[1]
guys / total


# In[13]:


# Admission rate for females
girls_admitted = df.query('gender == "female"')['admitted'].value_counts()[1]
girls_admitted / girls


# In[14]:


# Admission rate for males
guys_admitted = df.query('gender == "male"')['admitted'].value_counts()[1]
guys_admitted / guys


# ### Proportion and admission rate for physics majors of each gender

# In[23]:


# What proportion of female students are majoring in physics?
girls_physics = df.query('gender == "female" and major == "Physics"').count()[1]
girls_physics / girls


# In[24]:


# What proportion of male students are majoring in physics?
guys_physics = df.query('gender == "male" and major == "Physics"').count()[1]
guys_physics / guys


# In[25]:


# Admission rate for female physics majors
girls_physics_admissions = df.query('gender=="female" and major=="Physics"')['admitted'].value_counts()
girls_physics_admissions[1] / sum(girls_physics_admissions)


# In[117]:


# Admission rate for male physics majors
guys_physics_admissions = df.query('gender=="male" and major=="Physics"')['admitted'].value_counts()
guys_physics_admissions[1] / sum(guys_physics_admissions)


# ### Proportion and admission rate for chemistry majors of each gender

# In[28]:


# What proportion of female students are majoring in chemistry?
girls_chemistry = df.query('gender == "female" and major=="Chemistry"').count()[0]
girls_chemistry / girls


# In[29]:


# What proportion of male students are majoring in chemistry?
guys_chemistry = df.query('gender == "male" and major=="Chemistry"').count()[0]
guys_chemistry / guys


# In[43]:


# Admission rate for female chemistry majors
girls_chemistry_admissions = df.query('gender=="female" and major=="Chemistry" and admitted==True').count()[0]
girls_chemistry_admissions / girls_chemistry


# In[44]:


# Admission rate for male chemistry majors
guys_chemistry_admissions = df.query('gender=="male" and major=="Chemistry" and admitted==True').count()[0]
guys_chemistry_admissions / guys_chemistry


# ### Admission rate for each major

# In[79]:


# Admission rate for physics majors
admissions_physics = df.query('major == "Physics"')['admitted'].describe()
admissions_physics[3] / admissions_physics[0]


# In[80]:


# Admission rate for chemistry majors
admissions_physics = df.query('major == "Chemistry"')['admitted'].describe()
admissions_physics[3] / admissions_physics[0]


# In[ ]:




