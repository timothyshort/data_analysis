import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline
np.random.seed(42)

full_data = pd.read_csv('coffee_dataset.csv')
sample_data = full_data.sample(200)

#Hypothesis testing
#H0: On average, non-coffee drinkers are the same height or taller.
#H1: On average, coffee drinkers are shorter than non-coffee drinkers.

#Bootstrap Samples
heights_diff = []
heights_coff = []
heights_no_coff = []
for _ in range(10000):
    b_sample = sample_data.sample(200, replace=True)
    hc = b_sample[b_sample['drinks_coffee'] == True]['height'].mean()
    hn = b_sample[b_sample['drinks_coffee'] == False]['height'].mean()
    heights_coff.append(hc)
    heights_no_coff.append(hn)
    heights_diff.append(hn - hc)

plt.hist(heights_diff);
plt.title('Distribution of Height Difference\nCoffee Drinkers - Non-Coffee Drinkers');

np.std(heights_no_coff)
np.std(heights_coff)
np.std(heights_diff)