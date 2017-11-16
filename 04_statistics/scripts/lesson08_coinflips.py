import numpy as np
import matplotlib.pyplot as plt


#Intro to random numbers
#print(np.random.randint(2, size = 10000).mean())
#print(np.random.choice([0, 1], size = 10000, p=[.8, .2]).mean())

trials = int(1e6)

#Coin Flips
print('Probably of 1 Head with Three Coin Flips with P(H) = .6')
coin_flips = np.random.choice([0,1], size = (trials,3), p=[.4, .6])
sum_coin_flips = coin_flips.sum(axis=1)
print((sum_coin_flips == 1).mean())


#Dice Rolls
print('Rolling an even number dice')
dice = np.random.choice([0,5], size = trials)
print((dice % 2 ==0).mean())

#Two Dice Rolls
print('Probably of rolling doubles')
dice1 = np.random.randint(6, size = trials)
dice2 = np.random.randint(6, size = trials)
print((np.sum(dice1 == dice2))/len(dice1))