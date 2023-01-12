# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 11:47:28 2021

@author: mprem
"""

import numpy as np
import pandas as pd
import pymannkendall as mk
data=pd.read_csv(r"E:\Prem PhD\Watershed management\Groundwater data\CSV_Files\AP_2004_2021.csv")
data1=data.iloc[:,:].values
count=0;
for i in range(0,len(data1)):
    if data1[i,-1]>=round(204-(204*(5/100))):
        count=count+1
print("selected wells equal to {}".format(count))
    