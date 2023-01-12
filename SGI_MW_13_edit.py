# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 13:47:06 2021

@author: mprem
"""
import pandas as pd
import matplotlib.pyplot as plt
from numpy import linspace
from scipy.stats import norm
import numpy as np
import pastas as ps
rainfall = pd.read_csv('BH2.csv', parse_dates=['Month'],
                     index_col='Month', squeeze=True)
date=pd.read_csv('BH2.csv')
date1=np.array(date.iloc[:,0].values)
date1=date1.reshape(len(date1),1)
def spi(rainfall):
    rainfall = rainfall.copy()
    for month in range(1, 13):
        data = rainfall[rainfall.index.month == month]
        n = data.size  # Number of observations
        pmin = 1 / (2 * n)
        pmax = 1 - pmin
        spi_values = norm.ppf(linspace(pmin,pmax,n))
        rainfall.loc[data.sort_values().index] = spi_values
    return rainfall
spi_13=np.array(spi(rainfall))
spi_13=spi_13.reshape(len(spi_13),1)
droughts=spi_13.copy()
droughts[droughts>0]=0
data_total=np.concatenate((date1,spi_13,(droughts.reshape(len(spi_13),1))),axis=1)
drought_date=[]
for i in range(0,187):
    if droughts[i,0]<0:
        drought_date.append(data_total[i,0])
plt.figure(figsize=(80,10))
plt.subplot(2,1,1)
plt.plot(data_total[:,0],spi_13[:,0],linestyle="-",color="k")
plt.axhline(0,linestyle="--", color="k")
plt.fill_between(data_total[:,0],0,droughts[:,0],color="red")
#plt.xticks([data_total[0,0],data_total[15,0],data_total[30,0],data_total[45,0],data_total[60,0],data_total[75,0],data_total[90,0],data_total[105,0],data_total[120,0],data_total[135,0],data_total[150,0],data_total[165,0],data_total[180,0],data_total[195,0]],data_total[203,0])
plt.xticks(drought_date,rotation=90,size=20)
plt.xlabel("Time",size=30)
plt.ylabel("SPI-1",size=30)
plt.title("Meteorological Drought",size=30)
plt.figure(figsize=(10,10))
#plt.subplot(2,1,2)
#plt.acorr(sgi_13[:,0], maxlags=60)
#plt.xlabel("Lags",size=15)
#plt.ylabel("Auto Correlation coefficient ACF")
#plt.grid(True)
#plt.show()
df=pd.DataFrame(spi_13)
df.to_csv(r"E:\Prem PhD\Watershed management\Groundwater data\CSV_files\Newtrial\precipitation\SPI_1_14_78.5.csv")