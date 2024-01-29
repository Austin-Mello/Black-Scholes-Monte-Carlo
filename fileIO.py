from curses import raw
"""
Created on Fri Nov 25 17:17:47 2022

@author: Austin Mello
"""

import pandas as pd
import os

'''
IO function to clean the data before use in part2.py.  Methods include removing
unessecary series, filtering by date, and casting data entries to their 
appropriate data types.
'''
def buildDataset(file):
    rawData = pd.read_csv(f'{os.getcwd()}{file}')
    rawData.drop('Volume', inplace=True, axis=1)
    rawData.drop('Open Int', inplace=True, axis=1)

    cleanData = pd.DataFrame()
    cleanData = rawData.loc[rawData['Time'] == "11/23/22"]
    cleanData['Last'] = cleanData['Last'].astype('float')
    cleanData['Strike'] = cleanData['Strike'].astype('float')
    return cleanData

def Q4Returns(file):
    return pd.read_csv(f'{os.getcwd()}{file}', parse_dates = True, index_col = 'date')

def plotter(series, filename):
    plot = series.plot()
    img = plot.get_figure()
    img.savefig(filename)