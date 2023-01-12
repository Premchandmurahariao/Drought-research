# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 14:52:24 2022

@author: mprem
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.text import OffsetFrom
from matplotlib.patches import ConnectionPatch
from scipy.stats import pearsonr
from scipy.stats import spearmanr
sgi=pd.read_csv(r"E:\Prem PhD\Watershed management\Groundwater data\CSV_Files\Newtrial\SGI.csv")
sgi=sgi.iloc[:,:].values
num=0;
districts={0:"CHITTOOR",1:"ANANTAPUR",2:"KURNOOL",3:"Y.S.R.",4:"SRI POTTI SRIRAMULU NELLORE",5:"PRAKASAM",6:"KRISHNA",7:"GUNTUR",8:"WEST GODAVARI",9:"VISAKHAPATNAM",10:"EAST GODAVARI",11:"VIZIANAGARAM",12:"SRIKAKULAM"}
IDS_dist=[];IRS_dist=[];
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(5,5),sharex=True)
plt.rcParams['font.size']='18'
ticks=['CHI','ATP','KUR','CUD','NEL','PRA','KRI','GUN','WG','VIS','EG','VZM','SRI']
district_wise_optimum=(pd.read_csv(r"E:\Prem PhD\Watershed management\Groundwater data\SGI_graphs\GW_drought_speed\District_wise_optimum_data.csv")).iloc[:,:].values
district_wise_rainfall=(pd.read_csv(r"E:\Prem PhD\Watershed management\Groundwater data\SGI_graphs\GW_drought_speed\District_wise_rainfall_data.csv")).iloc[:,:].values
district_wise_data=(pd.read_csv(r"E:\Prem PhD\Watershed management\Groundwater data\SGI_graphs\GW_drought_speed\District_wise_drought_data.csv")).iloc[:,:].values
medians_D=[];medians_R=[];medians_rainfall=[];medians_DDD=[];medians_DRD=[];region1=np.zeros((2,4));region2=np.zeros((2,4));
for dist in range(0,13):
    prev=num
    for total in range(0,len(sgi)):
        if sgi[total,1]==districts[dist]:
            num=num+1
    IDS_dist.append(district_wise_optimum[prev:num,-2])
    IRS_dist.append(district_wise_optimum[prev:num,-1])
    bplot1 = axs[0].boxplot(IDS_dist[dist],positions=[dist],widths=0.45,vert=True,patch_artist=False,showmeans=False,showfliers=False)
    bplot2 = axs[1].boxplot(IRS_dist[dist],positions=[dist],widths=0.45,vert=True,patch_artist=False,showmeans=False,showfliers=False)
    medians_D.append([(item.get_ydata()[0], 1) for item in bplot1['medians']][0])
    medians_R.append([(item.get_ydata()[0], 1) for item in bplot2['medians']][0])
medians=np.reshape(np.array(medians_D),(13,2))
medians2=np.reshape(np.array(medians_R),(13,2))
IDS_dist=[];IRS_dist=[];num=0;
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(25,5),dpi=600,sharex=True)
for dist in range(0,13):
    prev=num
    for total in range(0,len(sgi)):
        if sgi[total,1]==districts[dist]:
            num=num+1
    IDS_dist.append(district_wise_data[prev:num,7])
    IRS_dist.append(district_wise_data[prev:num,8])
    bplot1 = axs[0].boxplot(IDS_dist[dist],positions=[dist],widths=0.45,vert=True,patch_artist=False,showmeans=False,showfliers=False)
    bplot2 = axs[1].boxplot(IRS_dist[dist],positions=[dist],widths=0.45,vert=True,patch_artist=False,showmeans=False,showfliers=False)
    medians_DDD.append([(item.get_ydata()[0], 1) for item in bplot1['medians']][0])
    medians_DRD.append([(item.get_ydata()[0], 1) for item in bplot2['medians']][0])
medians3=np.reshape(np.array(medians_DDD),(13,2))
medians4=np.reshape(np.array(medians_DRD),(13,2))
for rows in range(0,13):
    medians_rainfall.append(np.median(district_wise_rainfall[rows,1:]))
medians_rainfall=np.reshape(np.array(medians_rainfall),(13,1))
fig, ax = plt.subplots(nrows=5, ncols=1, figsize=(12,20),sharex=True)
plots={0:medians,1:medians2,2:medians3,3:medians4,4:medians_rainfall}
colours={0:"r",1:"b",2:"g",3:"c",4:"y"}
plt.rcParams['font.size']='18'
for x in range(0,5):
    ax[x].plot(plots[x][:,0],label="Median",color=colours[x],linewidth=4)
    ax[x].legend()
ax[0].set_ylabel('TDD (months)',weight='bold')
ax[1].set_ylabel('Severity',weight='bold')
ax[2].set_ylabel('DDD (months)',weight='bold')
ax[3].set_ylabel('DRD (months)',weight='bold')
ax[4].set_ylabel('Rainfall (mm)',weight='bold')
ax[4].legend(loc='lower right')
plt.xticks(range(0,13),ticks,rotation='horizontal',weight='bold')
xyA = (0, 20)
xyB = (3, 20)
coordsA = "data"
coordsB = "data"
con = ConnectionPatch(xyA, xyB, coordsA, coordsB,arrowstyle="<->", shrinkA=0, shrinkB=0,mutation_scale=10, fc="r")
ax[4].plot([xyA[0], xyB[0]], [xyA[1], xyB[1]], ".")
ax[4].add_artist(con)
xyA = (4, 20)
xyB = (7, 20)
coordsA = "data"
coordsB = "data"
con = ConnectionPatch(xyA, xyB, coordsA, coordsB,arrowstyle="<->", shrinkA=0, shrinkB=0,mutation_scale=10, fc="r")
ax[4].plot([xyA[0], xyB[0]], [xyA[1], xyB[1]], ".")
ax[4].add_artist(con)
xyA = (8, 20)
xyB = (12, 20)
coordsA = "data"
coordsB = "data"
con = ConnectionPatch(xyA, xyB, coordsA, coordsB,arrowstyle="<->", shrinkA=0, shrinkB=0,mutation_scale=10, fc="r")
ax[4].plot([xyA[0], xyB[0]], [xyA[1], xyB[1]], ".")
ax[4].add_artist(con)
ax[4].annotate('RAY',xy=(0, 21), xycoords='data',xytext=(5, 5), textcoords='offset points',weight='bold')
ax[4].annotate('SCA',xy=(4, 21), xycoords='data',xytext=(5,5), textcoords='offset points',weight='bold')
ax[4].annotate('NCA',xy=(8, 21), xycoords='data',xytext=(5,5), textcoords='offset points',weight='bold')
ax[0].text(0,82,'a)',style='italic',fontsize=12,weight='bold')
ax[1].text(0,-79,'b)',style='italic',fontsize=12,weight='bold')
ax[2].text(0,50,'c)',style='italic',fontsize=12,weight='bold')
ax[3].text(0,35,'d)',style='italic',fontsize=12,weight='bold')
ax[4].text(0,30,'e)',style='italic',fontsize=12,weight='bold')
ax[4].text(0,-2,'RAY-Rayalaseema SCA-South Coastal Andhra, NCA-North Coastal Andhra',fontsize=12,weight='bold')
region1[:,0]=pearsonr(medians[:,0],medians_rainfall[:])
region1[:,1]=pearsonr(medians2[:,0],medians_rainfall[:])
region1[:,2]=pearsonr(medians3[:,0],medians_rainfall[:])
region1[:,3]=pearsonr(medians4[:,0],medians_rainfall[:])

