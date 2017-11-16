import numpy as np

tests = 100000

#A fair coin flip produces heads
coin_flips = np.random.binomial(1, .5, tests)
print(sum(coin_flips)/tests)

#Five fair coin flips produce exactly one head
coin_flips = np.random.binomial(5, .5, tests)
print(np.sum(coin_flips==1)/len(coin_flips))

#Ten fair coin flips produce exactly four heads
coin_flips = np.random.binomial(10, .5, tests)
print(np.sum(coin_flips==4)/len(coin_flips))

#Five biased coin flips with P(H) = 0.8 produce exactly five heads
coin_flips = np.random.binomial(5, .8, tests)
print(np.sum(coin_flips==5)/len(coin_flips))

#Ten biased coin flips with P(H) = 0.15 produce three or more heads
coin_flips = np.random.binomial(10, .15, tests)
print(np.sum(coin_flips>=3)/len(coin_flips))