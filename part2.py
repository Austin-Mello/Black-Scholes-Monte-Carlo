"""
Created on Fri Nov 25 17:17:47 2022

@author: Austin Mello
"""

from fileinput import filename
from tkinter import Y
from part1 import *
from fileIO import *
import pandas as pd
import matplotlib.pyplot as plt

'''
Function designed to take an input file, parse the calls and puts, and calculate
their implied volatilities.
Inputs: Filename
        time: Set to the time declared in part1 by default.  Can be overloaded
            as needed.
Outputs: Two plots of implied volatilities for both calls and puts. File type
         by default is .png
Variables: allData: Used to initially store the incoming dataframe from the csv
            calls: Dataframe used to store the calls
            puts: Dataframe used to store the puts
'''
def impliedVol(fileName, time = T):
    allData = pd.DataFrame
    calls = pd.DataFrame
    puts = pd.DataFrame

    #Calls the IO function in the fileIO module and parses the calls and puts.
    allData = buildDataset(fileName)
    calls = allData.loc[allData['Type'] == "Call"]
    puts = allData.loc[allData['Type'] == "Put"]

    #Creates a new series to capture implied volatilities.
    calls["Implied Volatility"] = 0.0
    puts["Implied Volatility"] = 0.0

    #Iterates through dataframe entries, calls part1's Newton-Raphson algo, and
    #stores the results in the dataframe.
    for i in range(calls['Strike'].size):
        calls['Implied Volatility'].iloc[i] = implied_volatility_call(calls['Last'].iloc[i], S, calls['Strike'].iloc[i], T, r)

    #Plots the implied volatilities and stores the plots in the parent directory
    plt.plot(calls.index, calls['Implied Volatility'])
    plt.savefig('ImpliedVolatilityCalls')
    plt.clf()

    #Same as above, but for puts
    for i in range(puts['Strike'].size):
        puts['Implied Volatility'].iloc[i] = implied_volatility_put(puts['Last'].iloc[i], S, puts['Strike'].iloc[i], T, r)

    plt.plot(puts.index, puts['Implied Volatility'])
    plt.savefig('ImpliedVolatilityPuts')
    plt.clf()

    print(calls)
    print(puts)


# Main function. Calls the above functions and feeds it the .csv 
#filename and the time, if necessary.

impliedVol('/TSLA-options-2mth.csv')
#impliedVol('/TSLA-options-14mth.csv', 1.16)



