# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 13:18:40 2022

@author: mprem
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
sgi=pd.read_csv(r"E:\Prem PhD\Watershed management\Groundwater data\CSV_Files\Newtrial\SGI.csv")
sgi=sgi.iloc[:,:].values
districts={0:"CHITTOOR",1:"ANANTAPUR",2:"WEST GODAVARI",3:"VISAKHAPATNAM",4:"EAST GODAVARI",5:"VIZIANAGARAM",6:"SRIKAKULAM",7:"SRI POTTI SRIRAMULU NELLORE",8:"PRAKASAM",9:"KURNOOL",10:"KRISHNA",11:"GUNTUR",12:"Y.S.R."}
sgi_values=sgi[:,8:195]
date=pd.read_csv(r"E:\Prem PhD\Watershed management\Groundwater data\SGI_code\BH1_.csv")
date=date.iloc[:,0].values
m=0;i=0;events=[];total_events=np.zeros((2,2))
drought_events=[];TVDP=[];TVRP=[];IDS=[];IRS=[];count=0;GW_duration=[];avg_IRS=[];avg_IDS=[];DD_duration=[];DR_duration=[];IDS_dist=[];IRS_dist=[];num=0;
district_wise_drought=np.zeros((114,6))
for wells in range(0,len(sgi)):
    DDD=[];DRD=[];
    while m<187:
        DDP=[];DRP=[];
        x=i+1
        event=[];time=[]
        if sgi_values[wells,i]<0:
            if sgi_values[wells,i+1]<0:
                x=i+2
                if sgi_values[wells,i+2]<0:
                    event=(sgi_values[wells,i:i+3])
                    time=(date[i:i+3])
                    x=i+3
                    while sgi_values[wells,x]<0:
                        event=(np.concatenate((event,[sgi_values[wells,x]]),axis=0))
                        time=(np.concatenate((time,[date[x]]),axis=0))
                        x=x+1
                    event=np.reshape(event,(len(event),1))
                    time=np.reshape(time,(len(time),1))
                    events=np.concatenate((time,event),axis=1)
                    PI=events[:,1].min()
                    count=count+1
                    for length in range(0,len(events)):
                        if events[length,1]==PI:
                            DRP.append(len(events[length+1:,1]))
                            DDP.append(len(events[0:length+1:,1]))
                    for j in range(0,DDP[0]-1):
                        if events[j+1,1]-events[j,1]<0:
                            TVDP.append(events[j+1,1]-events[j,1])
                    for month in range(0,DRP[0]-1):
                        if events[DDP[0]-1+month+1,1]-events[DDP[0]-1+month,1]>0:
                            TVRP.append(events[DDP[0]-1+month+1,1]-events[DDP[0]-1+month,1])
                    if DDP[0]-1==0:
                        IDS.append(sum(TVDP)/(DDP[0]))
                    else:
                        IDS.append(sum(TVDP)/(DDP[0]-1))
                    if DRP[0]-1==0:
                        IRS.append(sum(TVRP)/(DRP[0]))
                    else:
                        IRS.append(sum(TVRP)/(DRP[0]-1))
                    drought_events.append(count)
                    GW_duration.append(len(events))
        i=x;m=x;
    for irs in range(0,len(IRS)):
        avg_IRS.append(abs(IRS[irs]))
    for ids in range(0,len(IDS)):
        avg_IDS.append(-1*abs(IDS[ids]))
        #district_wise_drought[wells,0]=sum(avg_IDS)/(sum(DDD)-len(DDD))
        #district_wise_drought[wells,1]=sum(avg_IRS)/(sum(DRD)-len(DRD))
    district_wise_drought[wells,2]=sum(GW_duration)
    district_wise_drought[wells,3]=sum(DDD)
    district_wise_drought[wells,4]=sum(DRD)
    district_wise_drought[wells,5]=drought_events[-1]
for dist in range(0,13):
    prev=num
    for total in range(0,len(sgi)):
        if district_wise_drought[total,0]==districts[dist]:
            num=num+1
    DD_duration.append(district_wise_drought[prev:num,4])
    DR_duration.append(district_wise_drought[prev:num,5])
    IDS_dist.append(district_wise_drought[prev:num,1])
    IRS_dist.append(district_wise_drought[prev:num,1])
fig,axes=plt.subplots(2,2,figsize=(18,10))  
sns.boxplot(ax=axes[0, 0], data=DD_duration[dist], x=districts[dist], y='Months')
    
                    
                    
                    