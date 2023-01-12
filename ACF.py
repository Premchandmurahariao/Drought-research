# -*- coding: utf-8 -*-
"""
Created on Tue May 24 07:55:46 2022

@author: mprem
"""

import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import warnings
sgi=pd.read_csv(r"E:\Prem PhD\Watershed management\Groundwater data\CSV_Files\Newtrial\SGI.csv")
sgi=sgi.iloc[:,:].values
fig, axs=plt.subplots(nrows=19,ncols=6,figsize=(20,20),dpi=300,sharex=True,)
col=0

for rows in range(0,19):
    i=0
    for well in range(col,col+6):
        plt.rcParams['font.size']='5'
        sgi_well=(np.reshape(sgi[well,8:],(len(sgi[well,8:]),1)))
        sgi_well=pd.DataFrame(sgi_well)
        plot_acf(sgi_well,lags=60,alpha=0.05,ax=axs[rows,i])
        axs[rows,0].set_ylabel('ACF',weight='bold')
        axs[rows,i].legend(['ACF','Confidence Interval'],loc='upper right')
        warnings.simplefilter('error', UserWarning)
        i=i+1
    col=col+6
    #plot_acf(sgi_well,lags=60,alpha=0.05)
    #plt.savefig(r"E:\Prem PhD\Watershed management\Groundwater data\SGI_graphs\GW_drought_speed\ACF\ACF_{}.png".format(sgi[well,2]))
for base in range(0,6):
    plt.rcParams['font.size']='5'
    axs[rows,base].set_xlabel('Lag Months',weight='bold')
plt.show()

    