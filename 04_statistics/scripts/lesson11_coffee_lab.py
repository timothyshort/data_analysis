import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
% matplotlib inline

np.random.seed(42)

coffee_full = pd.read_csv('coffee_dataset.csv')
coffee_red = coffee_full.sample(200)
coffee_red.head()

#Explore one sample
sample_coffee_drinkers = coffee_red[coffee_red['drinks_coffee'] == True]
sample_not_coffee_drinkers = coffee_red[coffee_red['drinks_coffee'] == False]
sample_p = sample_coffee_drinkers['drinks_coffee'].count() / coffee_red.shape[0]
sample_not_p = sample_not_coffee_drinkers['drinks_coffee'].count() / coffee_red.shape[0]
print('Avg Height Coffee Drinkers: {}',format(sample_coffee_drinkers['height'].mean()))
print('Avg Height Non-Coffee Drinkers: {}'.format(sample_not_coffee_drinkers['height'].mean()))

#Generate 10,000 samples
mean_heights = []
for _ in range (10000):
    new_sample = coffee_full.sample(200)
    mean_heights.append(new_sample[new_sample['drinks_coffee'] == False]['height'].mean())

#Plot histogram
plt.hist(mean_heights);

#Extract data & Confidence Intervals
conf_low = np.percentile(mean_heights, 2.5)
conf_high = np.percentile(mean_heights, 97.5)
pop_mean_height = coffee_full[coffee_full['drinks_coffee'] == False]['height'].mean()
sample_height_means = np.mean(mean_heights)

#Print results
print('Population Mean Height: {}'.format(pop_mean_height))
print('Sample C.I. Lower Bound: {}'.format(conf_low))
print('Sample C.I. Upper Bound: {}'.format(conf_high))
print('Sample Mean: {}'.format(sample_height_means))