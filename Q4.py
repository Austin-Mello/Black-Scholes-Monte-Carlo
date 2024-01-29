#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 17:17:47 2022

@author: vincentliang
"""

import numpy as np
import pandas as pd
from fileIO import *
import matplotlib.pyplot as plt


# Q4
TSLA_returns = Q4Returns("/TSLA-returns.csv")
print(TSLA_returns)

# Need:
# 60-day rolling mean
# 60-day rolling volatilities(SD)
# 60-day rolling skewness
# 60-day rolling excess kurtosis

# mean
rmean = TSLA_returns['TSLA'].rolling(60).mean()
plotter(rmean, "RollingMean")

# volatility
rstd = TSLA_returns['TSLA'].rolling(60).std()
plotter(rstd, "RollingStd")

# skewness
rskew = TSLA_returns['TSLA'].rolling(60).skew()
plotter(rskew, "RollingSkew")

# excess kurtosis
rkurt = TSLA_returns['TSLA'].rolling(60).kurt()
plotter(rkurt, "RollingKurt")
