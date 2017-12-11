import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline
np.random.seed(42)

full_data = pd.read_csv('coffee_dataset.csv')
sample_data = full_data.sample(200)

#Compare difference of heights by coffee drinker
diff_heights = []
for _ in range(10000):
    b_sample = sample_data.sample(200, replace=True)
    mean_heights_coffee = b_sample[b_sample['drinks_coffee'] == True]['height'].mean()
    mean_heights_no_coffee = b_sample[b_sample['drinks_coffee'] == False]['height'].mean()
    diff_heights.append(mean_heights_coffee - mean_heights_no_coffee)
print(np.percentile(diff_heights,.5), np.percentile(diff_heights,99.5))
plt.hist(diff_heights);
plt.title('Distribution of Height Difference by Coffee vs Non-Coffee Drinkers');

#Compare difference of heights by age
diff_height_age = []
for _ in range(10000):
    sample = sample_data.sample(200, replace=True)
    mean_height_old = sample[sample['age'] == ">=21"]['height'].mean()
    mean_height_young = sample[sample['age'] == "<21"]['height'].mean()
    diff_height_age.append(mean_height_old - mean_height_young)
print(np.percentile(diff_height_age, .5), np.percentile(diff_height_age, 99.5))
plt.hist(diff_height_age);
plt.title('Distribution of Height Difference by Age');

#Compare difference of heights by coffee drinker for under 21
diff_heights = []
for _ in range(10000):
    sample = sample_data.sample(200, replace=True)
    sample_young = sample[sample['age'] == "<21"]
    mean_height_cof = sample_young[sample_young['drinks_coffee'] == True]['height'].mean()
    mean_height_no_cof = sample_young[sample_young['drinks_coffee'] == False]['height'].mean()
    diff_heights.append(mean_height_cof - mean_height_no_cof)
plt.hist(diff_heights)