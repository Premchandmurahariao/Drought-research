# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 11:47:28 2021

@author: mprem
"""

import numpy as np
import pandas as pd
import pymannkendall as mk
data=pd.read_csv(r"E:\Prem PhD\Watershed management\Groundwater data\CSV_Files\Newtrial\SGI.csv")
x=0;y=0;c=0;
for i in range(0,114):
    data1=data.iloc[i,6:204].values
    trend=mk.hamed_rao_modification_test(data1,alpha=0.05)
    print(trend)
    print(data.iloc[i,2])
    if trend.trend=='increasing':
        x=x+1
    elif trend.trend=='no trend':
        y=y+1
    else:
        c=c+1
print(x)
print(y)
print(c)