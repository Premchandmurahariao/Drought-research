# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 15:53:16 2022

@author: mprem
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np
from matplotlib.text import OffsetFrom
import pandas as pd
from matplotlib.patches import ConnectionPatch
sgi=pd.read_csv(r"E:\Prem PhD\Watershed management\Groundwater data\CSV_Files\Newtrial\avg_SGI.csv")
sgi=sgi.iloc[:,1:].values
run=sgi[-1,167:194]
gem=run.copy()
gem[gem>0]=0
gem1=run.copy()
gem1[gem<0]=0
fig,ax=plt.subplots(nrows=1,ncols=1,figsize=(4,2),dpi=300)
ax.plot(np.arange(0,27,1),run)
ax.axhline(0,linestyle="-", color="k")
ax.fill_between(np.arange(0,27,1),0,gem,color='red',label='Negative Run')
ax.fill_between(np.arange(0,27,1),0,gem1,color='blue',label='Positive Run')
plt.xlim(0,26);plt.ylim(-2,2);
#ax.axvline((12,0),linestyle="-", color="k")
xyA = (5, 0)
xyB = (12, -1.05)
coordsA = "data"
coordsB = "data"
con = ConnectionPatch(xyA, xyB, coordsA, coordsB,
                      arrowstyle="-|>", shrinkA=0, shrinkB=0,
                      mutation_scale=10, fc="r")
ax.plot([xyA[0], xyB[0]], [xyA[1], xyB[1]], ".")
ax.add_artist(con)
xyA = (12, -1.05)
xyB = (22, 0)
coordsA = "data"
coordsB = "data"
con = ConnectionPatch(xyA, xyB, coordsA, coordsB,
                      arrowstyle="-|>", shrinkA=0, shrinkB=0,
                      mutation_scale=10, fc="r")
ax.plot([xyA[0], xyB[0]], [xyA[1], xyB[1]], ".")
ax.add_artist(con)
xyA = (12, -1.05)
xyB = (12, 0)
coordsA = "data"
coordsB = "data"
con = ConnectionPatch(xyA, xyB, coordsA, coordsB,
                      arrowstyle="-", shrinkA=0, shrinkB=0,
                      mutation_scale=10, fc="r")
ax.plot([xyA[0], xyB[0]], [xyA[1], xyB[1]], ".")
ax.add_artist(con)
ax.annotate(
    'DDD',
    xy=(8, -0.01), xycoords='data',
    xytext=(15, 15), textcoords='offset points',
    arrowprops=dict(arrowstyle="->"))
ax.annotate(
    'DRD',
    xy=(18, -0.01), xycoords='data',
    xytext=(15, 15), textcoords='offset points',
    arrowprops=dict(arrowstyle="->"))
ax.annotate(
    '$t_{on}$',
    xy=(5, 0), xycoords='data',
    xytext=(-15, -15), textcoords='offset points',
    arrowprops=dict(arrowstyle="->"))
ax.annotate(
    '$t_{pe}$',
    xy=(12, -1.05), xycoords='data',
    xytext=(-35, 0.5), textcoords='offset points',
    arrowprops=dict(arrowstyle="->"))
ax.annotate(
    '$t_{end}$',
    xy=(22, 0), xycoords='data',
    xytext=(-20,-30), textcoords='offset points',
    arrowprops=dict(arrowstyle="->"))
ax.set_ylabel('SGI',weight='bold')
ax.set_xlabel('Duration (Months)',weight='bold')
ax.legend(loc='best')