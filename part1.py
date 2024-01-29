"""
Created on Fri Nov 25 17:17:47 2022

@author: Austin Mello
"""

import numpy as np
from scipy.stats import norm

#Lambda functions for given functions below
N_prime = norm.pdf
N = norm.cdf

#All functions below are either copies for variations of the algorithms found @
#https://www.codearmo.com/blog/implied-volatility-european-call-python
def black_scholes_call(S, K, T, r, sigma):
    '''
    :param S: Asset price
    :param K: Strike price
    :param T: Time to maturity
    :param r: risk-free rate (treasury bills)
    :param sigma: volatility
    :return: call price
    '''

    ###standard black-scholes formula
    d1 = (np.log(S / K) + (r + ((sigma ** 2) / 2)) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    call = S * N(d1) -  N(d2)* K * np.exp(-r * T)
    return call

def black_scholes_put(S, K, T, r, sigma):
    '''
    :param S: Asset price
    :param K: Strike price
    :param T: Time to maturity
    :param r: risk-free rate (treasury bills)
    :param sigma: volatility
    :return: put price
    '''

    ###standard black-scholes formula
    d1 = (np.log(S / K) + (r + (sigma ** 2 / 2) * T) / (sigma * np.sqrt(T)))
    d2 = (d1 - sigma * np.sqrt(T))

    put = K * np.exp(-r * T) * N(-d2) - S * N(-d1) 
    return put

def vega(S, K, T, r, sigma):
    '''

    :param S: Asset price
    :param K: Strike price
    :param T: Time to Maturity
    :param r: risk-free rate (treasury bills)
    :param sigma: volatility
    :return: partial derivative w.r.t volatility
    '''

    ### calculating d1 from black scholes
    d1 = (np.log(S / K) + (r + (sigma ** 2) / 2) * T) / sigma * np.sqrt(T)

    vega = S  * np.sqrt(T) * N_prime(d1)
    return vega

def implied_volatility_call(C, S, K, T, r, tol=0.0001,
                            max_iterations=1000):
    '''

    :param C: Observed call price
    :param S: Asset price
    :param K: Strike Price
    :param T: Time to Maturity
    :param r: riskfree rate
    :param tol: error tolerance in result
    :param max_iterations: max iterations to update vol
    :return: implied volatility in percent
    '''


    ### assigning initial volatility estimate for input in Newton_rap procedure
    sigma = 0.65
    
    for i in range(max_iterations):

        ### calculate difference between blackscholes price and market price with
        ### iteratively updated volality estimate
        diff = black_scholes_call(S, K, T, r, sigma) - C

        ###break if difference is less than specified tolerance level
        if abs(diff) < tol:
            #print(f'found on {i}th iteration')
            #print(f'difference is equal to {diff}')
            break

        ### use newton rapshon to update the estimate
        sigma = sigma - diff / vega(S, K, T, r, sigma)

    return sigma

def implied_volatility_put(C, S, K, T, r, tol=0.0001,
                            max_iterations=1000):
    '''

    :param C: Observed call price
    :param S: Asset price
    :param K: Strike Price
    :param T: Time to Maturity
    :param r: riskfree rate
    :param tol: error tolerance in result
    :param max_iterations: max iterations to update vol
    :return: implied volatility in percent
    '''


    ### assigning initial volatility estimate for input in Newton_rap procedure
    sigma = 0.3
    
    for i in range(max_iterations):

        ### calculate difference between blackscholes price and market price with
        ### iteratively updated volality estimate
        diff = black_scholes_put(S, K, T, r, sigma) - C

        ###break if difference is less than specified tolerance level
        if abs(diff) < tol:
            #print(f'found on {i}th iteration')
            #print(f'difference is equal to {diff}')
            break

        ### use newton rapshon to update the estimate
        sigma = sigma - diff / vega(S, K, T, r, sigma)

    return sigma

#Given variables from assignment
S = 183
K1 = 160
K2 = 200
r = 0.038
T = .16
sugma = .65

#Function calls and print statements of function outputs.
C = black_scholes_call(S, K1, T, r, sugma)
P = black_scholes_put(S, K1, T, r, sugma)
print(f"Value of call is: {C}")
print(f"Value of put is: {P}")
print(f"Implied volatility of call is: {implied_volatility_call(C, S, K1, T, r)}")
print(f"Implied volatility of put is: {implied_volatility_put(C, S, K1, T, r)}")