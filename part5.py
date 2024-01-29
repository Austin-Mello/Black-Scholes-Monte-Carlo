"""
Created on Wed Nov 30 14:13:47 2022

@author: Austin Mello
"""
from random import sample
from fileIO import *
from part1 import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#List of strike prices. Iterated over by both methods.
STRIKE_TABLE = [10, 100, 160, 180, 200, 300, 400] 

#Calls fileIO function for the Tesla returns
TSLA_returns = Q4Returns("/TSLA-returns.csv")


paths = []
pop = 10000
sample = 60
sigma = TSLA_returns.std()

for i in range(pop):
    y = np.random.choice(TSLA_returns.TSLA.to_list(), size=sample, replace=True)
    y = y - TSLA_returns.TSLA.mean()
    st = np.log(180) + np.cumsum(y)
    paths.append(np.exp(st[sample-1]))


for j in range(sample):
    paths[j] = paths[j] + r

monte = []
black = []

for i in range(len(STRIKE_TABLE)):
    sum = 0
    for j in range(pop):
        sum = sum + max(paths[j] - STRIKE_TABLE[i], 0)
    monte.append(sum/pop)

print(monte)

for i in range(len(STRIKE_TABLE)):
    black.append(black_scholes_call(S, STRIKE_TABLE[i], T, r, sigma)[0])

print(black)

data = { 'monte': monte,
        'black': black
}
plt.plot(STRIKE_TABLE, monte, STRIKE_TABLE, black)
plt.xlabel('Strike Prices')
plt.ylabel('Call Value')
plt.savefig('MonteVsBlack')
