# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 06:17:19 2022

@author: mprem
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.text import OffsetFrom
from matplotlib.patches import ConnectionPatch
sgi=pd.read_csv(r"H:\Prem PhD\Watershed management\Groundwater data\CSV_Files\Newtrial\SGI.csv")
sgi=sgi.iloc[:,:].values
num=0;
districts={0:"CHITTOOR",1:"ANANTAPUR",2:"KURNOOL",3:"Y.S.R.",4:"SRI POTTI SRIRAMULU NELLORE",5:"PRAKASAM",6:"KRISHNA",7:"GUNTUR",8:"WEST GODAVARI",9:"VISAKHAPATNAM",10:"EAST GODAVARI",11:"VIZIANAGARAM",12:"SRIKAKULAM"}
IDS_dist=[];IRS_dist=[];
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(22,8),dpi=600,sharex=True)
plt.rcParams['font.size']='18'
ticks=['CHI','ATP','KUR','CUD','NEL','PRA','KRI','GUN','WG','VIS','EG','VZM','SRI']
district_wise_optimum=(pd.read_csv(r"H:\Prem PhD\Watershed management\Groundwater data\SGI_graphs\GW_drought_speed\District_wise_optimum_data.csv")).iloc[:,:].values
medians_D=[];medians_R=[];
for dist in range(0,13):
    prev=num
    for total in range(0,len(sgi)):
        if sgi[total,1]==districts[dist]:
            num=num+1
    IDS_dist.append(district_wise_optimum[prev:num,12])
    IRS_dist.append(district_wise_optimum[prev:num,13])
    bplot1 = axs[0].boxplot(IDS_dist[dist],positions=[dist],widths=0.45,vert=True,patch_artist=False,showmeans=False,showfliers=False)
    bplot2 = axs[1].boxplot(IRS_dist[dist],positions=[dist],widths=0.45,vert=True,patch_artist=False,showmeans=False,showfliers=False)
    medians_D.append([(item.get_ydata()[0], 1) for item in bplot1['medians']][0])
    medians_R.append([(item.get_ydata()[0], 1) for item in bplot2['medians']][0])
medians=np.reshape(np.array(medians_D),(13,2))
medians2=np.reshape(np.array(medians_R),(13,2))
#axs[0].plot(medians[:,0])
#axs[1].plot(medians2[:,0])
axs[0].set_ylabel('Months',weight='bold')
#axs[0].set_title('District wise optimum IDS variation',weight='bold')
axs[1].set_ylabel('Months',weight='bold')
#axs[1].set_title('District wise optimum IRS variation',weight='bold')
plt.sca(axs[0])
axs[0].text(0,-0.50,'c)',style='italic',fontsize=16,weight='bold')
plt.xticks(range(0,13),ticks,rotation='horizontal',weight='bold')
plt.sca(axs[1])
axs[1].text(0,0.0,'d)',style='italic',fontsize=16,weight='bold')
plt.xticks(range(0,13),ticks,rotation='horizontal',weight='bold')
axs[0].legend([bplot1["medians"][0]],["Median"],loc='best',fontsize=12)
axs[1].legend([bplot2["medians"][0]],["Median"],loc='best',fontsize=12)
for rows in range(0,1):
    for cols in range(0,1):
        xyA = (0, -0.6)
        xyB = (3, -0.6)
        xyA1= (0, -0.1)
        xyB1 =(3, -0.1)
        coordsA = "data"
        coordsB = "data"
        con = ConnectionPatch((xyA), (xyB), coordsA, coordsB,
                      arrowstyle="<->", shrinkA=0, shrinkB=0,
                      mutation_scale=10, fc="r")
        con1 = ConnectionPatch((xyA1), (xyB1), coordsA, coordsB,
                     arrowstyle="<->", shrinkA=0, shrinkB=0,
                      mutation_scale=10, fc="r")
        axs[cols].plot([(xyA[0]), (xyB[0])], [(xyA[1]), (xyB[1])], ".")
        axs[cols].add_artist(con)
        axs[cols+1].plot([(xyA1[0]), (xyB1[0])], [(xyA1[1]), (xyB1[1])], ".")
        axs[cols+1].add_artist(con1)
axs[0].annotate('RAY',xy=((0, -0.59)), xycoords='data',xytext=(5, 5), textcoords='offset points',weight='bold')
axs[1].annotate('RAY',xy=((0,-0.09)), xycoords='data',xytext=(5, 5), textcoords='offset points',weight='bold')
for rows in range(0,1):
    for cols in range(0,1):
        xyA = (4, -0.6)
        xyB = (7, -0.6)
        xyA1= (4, -0.1)
        xyB1 = (7, -0.1)
        coordsA = "data"
        coordsB = "data"
        con = ConnectionPatch((xyA), (xyB), coordsA, coordsB,
                      arrowstyle="<->", shrinkA=0, shrinkB=0,
                      mutation_scale=10, fc="r")
        con1 = ConnectionPatch((xyA1), (xyB1), coordsA, coordsB,
                      arrowstyle="<->", shrinkA=0, shrinkB=0,
                      mutation_scale=10, fc="r")
        axs[cols].plot([(xyA[0]), (xyB[0])], [(xyA[1]), (xyB[1])], ".")
        axs[cols].add_artist(con)
        axs[cols+1].plot([(xyA1[0]), (xyB1[0])], [(xyA1[1]), (xyB1[1])], ".")
        axs[cols+1].add_artist(con1)
axs[0].annotate('SCA',xy=((4, -0.59)), xycoords='data',xytext=(5, 5), textcoords='offset points',weight='bold')
axs[1].annotate('SCA',xy=((4,-0.09)), xycoords='data',xytext=(5, 5), textcoords='offset points',weight='bold')
for rows in range(0,1):
    for cols in range(0,1):
        xyA = (8, -0.6)
        xyB = (12, -0.6)
        xyA1= (8, -0.1)
        xyB1 = (12, -0.1)
        coordsA = "data"
        coordsB = "data"
        con = ConnectionPatch((xyA), (xyB), coordsA, coordsB,
                      arrowstyle="<->", shrinkA=0, shrinkB=0,
                      mutation_scale=10, fc="r")
        con1 = ConnectionPatch((xyA1), (xyB1), coordsA, coordsB,
                      arrowstyle="<->", shrinkA=0, shrinkB=0,
                      mutation_scale=10, fc="r")
        axs[cols].plot([(xyA[0]), (xyB[0])], [(xyA[1]), (xyB[1])], ".")
        axs[cols].add_artist(con)
        axs[cols+1].plot([(xyA1[0]), (xyB1[0])], [(xyA1[1]), (xyB1[1])], ".")
        axs[cols+1].add_artist(con1)
axs[0].annotate('NCA',xy=((8, -0.59)), xycoords='data',xytext=(5, 5), textcoords='offset points',weight='bold')
axs[1].annotate('NCA',xy=((8,-0.09)), xycoords='data',xytext=(5, 5), textcoords='offset points',weight='bold')
axs[0].text(0,-0.69,'RAY-Rayalaseema, SCA-South Coastal Andhra, NCA-North Coastal Andhra',fontsize=12,weight='bold')
axs[1].text(0,-0.17,'RAY-Rayalaseema, SCA-South Coastal Andhra, NCA-North Coastal Andhra',fontsize=12,weight='bold')
#axs[0].legend(loc=(12,75))