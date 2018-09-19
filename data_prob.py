# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 14:21:48 2017

@author: iromanow
"""

from __future__ import division
import pandas as pd


# to do: use the column names as values passed in (but make them default), so that they can be user specified. 


def calc_prob(data):
#    get the oldest date, and the youngest date to calculate the range for the dictionary
    minimum = data["lower_date"].min().astype(int)
    maximum = data["upper_date"].max().astype(int)
    
#    initiate the dictionary
    x = dict.fromkeys(range(minimum, maximum), 0)   
    
#    calculat the 'probability of existence' for any one year = year / range of dates times the number of hornos/prensas (volume)
    data['range'] =   (1 / (data["upper_date"] - data["lower_date"] ))

#    print(data['range'])
    
#    drop nans because they fuck with recasting into integers
    data = data.dropna(subset=["lower_date"])
    data = data.dropna(subset=["upper_date"])
    
#   for each site
    for row in range(len(data)):
#        for each year
        for year in range(data["lower_date"].astype(int).iloc[row], data["upper_date"].astype(int).iloc[row]):
#           update that year with the probability of that site
            x[year] += 1#data['range'].iloc[row]

#   recast it into a useful data structure
    s = pd.Series(x, name='Probability')
    s.index.name = 'Year'
    s.reset_index()

    return s

