import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
students = np.array([1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0])
p = students.mean()

draws = 5 
sample = np.random.choice(students, draws)
print(sample.mean())

size = 10000
sample_dist = np.random.choice(students, [size, draws])
sample_props = sample_dist.mean(axis=1)
print(sample_props.mean())

pop_std = students.std()
print('Standard Deviation: {}'.format(pop_std))
pop_var = students.var()
print('Variance: {}'.format(pop_var))

sample_dist_std = sample_props.std()
print('Standard Deviation: {}'.format(sample_dist_std))
sample_dist_var = sample_props.var()
print('Variance: {}'.format(sample_dist_var))

print(p*(1-p))
print((p*(1-p))/draws)

##Simulate with 20 draws
draws = 20
sample_2 = np.random.choice(students, draws)
sample_2_mean = sample_2.mean()

sample_2_dist = np.random.choice(students, [size, draws])
sample_2_props = sample_2_dist.mean(axis=1)

sample_2_dist_std = sample_2_props.std()
print('Standard Deviation: {}'.format(sample_2_dist_std))
sample_2_dist_var = sample_2_props.var()
print('Variance: {}'.format(sample_2_dist_var))

plt.figure(figsize=(10,10))
plt.subplot(2,1,1)
plt.hist(sample_props, bins=5);
plt.subplot(2,1,2)
plt.hist(sample_2_props);