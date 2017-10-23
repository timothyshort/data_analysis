
# coding: utf-8

# # Drawing Conclusions
# Use the space below to address questions on datasets `clean_08.csv` and `clean_18.csv`

# In[3]:


# load datasets
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
df_08 = pd.read_csv('clean_08.csv')
df_18 = pd.read_csv('clean_18.csv')


# ### Q1: Are more unique models using alternative sources of fuel? By how much?

# In[4]:


df_08['fuel'].value_counts()
gasoline = df_08['fuel'].value_counts()[0]
cng = df_08['fuel'].value_counts()[1]
gas = df_08['fuel'].value_counts()[2]
ethanol = df_08['fuel'].value_counts()[3]

x_labels = ['Gasoline', 'CNG', 'Gas', 'Ethanol']
y_values = [gasoline, cng, gas, ethanol]
locations = [1, 2, 3, 4]
plt.bar(locations, y_values, tick_label = x_labels);


# In[5]:


df_18['fuel'].value_counts()
gasoline = df_18['fuel'].value_counts()[0]
gas = df_18['fuel'].value_counts()[1]
ethanol = df_18['fuel'].value_counts()[2]
diesel = df_18['fuel'].value_counts()[3]
electricity = df_18['fuel'].value_counts()[4]

x_labels = ['Gasoline', 'Gas', 'Ethanol', 'Diesel', 'Electricity']
y_values = [gasoline, gas, ethanol, diesel, electricity]
locations = [1, 2, 3, 4, 5]
plt.bar(locations, y_values, tick_label = x_labels);


# ### Q2: How much have vehicle classes improved in fuel economy?  

# In[6]:


#df_08.head()
#df_08.groupby('veh_class')['cmb_mpg'].describe()
df_08.groupby('veh_class')['cmb_mpg'].mean()


# In[7]:


#df_18.groupby('veh_class')['cmb_mpg'].describe()
df_18.groupby('veh_class')['cmb_mpg'].mean()


# In[8]:


station_wagon_dx = df_18.groupby('veh_class')['cmb_mpg'].mean()[8] - df_08.groupby('veh_class')['cmb_mpg'].mean()[6]
large_car_dx = df_18.groupby('veh_class')['cmb_mpg'].mean()[0] - df_08.groupby('veh_class')['cmb_mpg'].mean()[1]
midsize_car_dx = df_18.groupby('veh_class')['cmb_mpg'].mean()[1] - df_08.groupby('veh_class')['cmb_mpg'].mean()[2]
small_car_dx = df_18.groupby('veh_class')['cmb_mpg'].mean()[5] - df_08.groupby('veh_class')['cmb_mpg'].mean()[5]
minivan_dx = df_18.groupby('veh_class')['cmb_mpg'].mean()[2] - df_08.groupby('veh_class')['cmb_mpg'].mean()[3]
pickup_dx = df_18.groupby('veh_class')['cmb_mpg'].mean()[3] - df_08.groupby('veh_class')['cmb_mpg'].mean()[4]
suv_dx = (df_18.groupby('veh_class')['cmb_mpg'].mean()[4] + df_18.groupby('veh_class')['cmb_mpg'].mean()[7]) / 2 - df_08.groupby('veh_class')['cmb_mpg'].mean()[0]


# In[9]:


location = [1, 2, 3, 4, 5, 6, 7]
labels = ['Small Car', 'Midsize Car', 'Large Car', 'Station Wagon', 'Pickup', 'SUV', 'Minivan']
values = [small_car_dx, midsize_car_dx, large_car_dx, station_wagon_dx, pickup_dx, suv_dx, minivan_dx]
plt.figure(figsize=(10,6));
plt.bar(location, values, tick_label=labels);
plt.title('Change in Fuel Efficiency by Vehicle Class\nFrom 2008 to 2018');
plt.xlabel('Vehicle Class');
plt.ylabel('Change in Fuel Efficiency');


# ### Q3: What are the characteristics of SmartWay vehicles? Have they changed over time?

# In[10]:


df_08.query('smartway == "yes"').describe()


# In[11]:


print("Combined MPG Comparison")
print('2008:', df_08.query('smartway == "yes"')['cmb_mpg'].mean())
print('2018:', df_18.query('smartway == "Yes"')['cmb_mpg'].mean())


# In[12]:


print("Greenhouse Gas Score Comparison")
print('2008:', df_08.query('smartway == "yes"')['greenhouse_gas_score'].mean())
print('2018:', df_18.query('smartway == "Yes"')['greenhouse_gas_score'].mean())


# In[13]:


print("Air Pollution Score")
print('2008:', df_08.query('smartway == "yes"')['air_pollution_score'].mean())
print('2018:', df_18.query('smartway == "Yes"')['air_pollution_score'].mean())


# ### Q4: What features are associated with better fuel economy?

# In[80]:


x = df_18.groupby('cmb_mpg')['cmb_mpg'].mean()
y = df_18.groupby('cmb_mpg')['greenhouse_gas_score'].mean()
plt.plot(x,y);
plt.title('Greenhouse Gas Score vs Combined MPG');
plt.xlabel('Combined MPG');
plt.ylabel('Mean Greanhouse Gas Score');


# In[167]:


x = df_18.groupby('fuel')
y = df_18.groupby('fuel')['cmb_mpg'].mean()
plt.plot(y);
plt.title('Fuel Type vs Average MPG');
plt.xlabel('Fuel Type');
plt.ylabel('Average MPG');


# In[115]:


y = df_18.groupby('veh_class')['cmb_mpg'].mean()
plt.figure(figsize=(12,5));
plt.plot(y);
plt.title('Vehicle Class vs Average MPG');
plt.xlabel('Vehicle Class');
plt.ylabel('Average MPG');


# In[ ]:




