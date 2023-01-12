# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 09:30:27 2022

@author: mprem
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
from statistics import median
sgi=pd.read_csv(r"H:\Prem PhD\Watershed management\Groundwater data\CSV_Files\Newtrial\SGI.csv")
sgi=sgi.iloc[:,:].values
district=np.reshape((sgi[:,1]),(len(sgi[:,1]),1))
districts={0:"CHITTOOR",1:"ANANTAPUR",2:"KURNOOL",3:"Y.S.R.",4:"SRI POTTI SRIRAMULU NELLORE",5:"PRAKASAM",6:"KRISHNA",7:"GUNTUR",8:"WEST GODAVARI",9:"VISAKHAPATNAM",10:"EAST GODAVARI",11:"VIZIANAGARAM",12:"SRIKAKULAM"}
sgi_values=sgi[:,8:]
date=pd.read_csv(r"H:\Prem PhD\Watershed management\Groundwater data\SGI_code\BH1_.csv")
date=date.iloc[:,0].values
total_events=np.zeros((2,2));
points=sgi[:,2];district_wise_mild=[];district_wise_moderate=[];district_wise_severe=[];district_wise_extreme=[];district_wise_DFI=[]
regions_={"RAY":sum(district_wise_mild[0:4]),"SCA":sum(district_wise_mild[4:8]),"NCA":sum(district_wise_mild[8:])}
for dists in range(0,13):
    well_wise_mild=[];well_wise_moderate=[];well_wise_severe=[];well_wise_extreme=[];DFI=[];
    for wells in range(0,len(sgi)):
        i=0;m=0;
        mild_GWD=[];moderate_GWD=[];severe_GWD=[];extreme_GWD=[];mild_count=0;moderate_count=0;severe_count=0;extreme_count=0;mild_d=[];mod_d=[];sev_d=[];ext_d=[];
        if districts[dists]==sgi[wells,1]:
            while m<len(sgi_values[0,:]):
                x=i+1
                if i==len(sgi_values[0,:])-2:
                    print("No drought event")
                elif i== len(sgi_values[0,:])-1:
                    print("End of GW time series")
                elif (sgi_values[wells,i]<0 and sgi_values[wells,i]>-0.5):
                    mild_d.append(1)
                    if (sgi_values[wells,i+1]<0 and sgi_values[wells,i+1]>-0.5):
                        x=i+2
                        mild_d.append(1)
                        if (sgi_values[wells,i+2]<0 and sgi_values[wells,i+2]>-0.5):
                            x=i+3
                            mild_d.append(1)
                            if i+2==len(sgi_values[0,:])-1:
                                print("End of GW time series")
                            else:
                                while (sgi_values[wells,x]<0 and sgi_values[wells,x]>-0.5):
                                    x=x+1
                                    mild_d.append(1)
                                    if x==len(sgi_values[0,:]):
                                        break
                                mild_GWD.append(mild_count+1)
                                mild_count=mild_count+1
                    i=x;m=x;
                elif (sgi_values[wells,i]<=-0.5 and sgi_values[wells,i]>-1.0):
                    mod_d.append(1)
                    if i==len(sgi_values[0,:])-2:
                        print("No drought event")
                    elif i== len(sgi_values[0,:])-1:
                        print("End of GW time series")
                    if (sgi_values[wells,i+1]<=-0.5 and sgi_values[wells,i+1]>-1.0):
                        x=i+2
                        mod_d.append(1)
                        if (sgi_values[wells,i+2]<=-0.5 and sgi_values[wells,i+2]>-1.0):
                            x=i+3
                            mod_d.append(1)
                            if i+2==len(sgi_values[0,:])-1:
                                print("End of GW time series")
                            else:
                                while (sgi_values[wells,x]<=-0.5 and sgi_values[wells,x]>-1.0):
                                    x=x+1
                                    mod_d.append(1)
                                    if x==len(sgi_values[0,:]):
                                        break
                                moderate_GWD.append(moderate_count+1)
                                moderate_count=moderate_count+1
                    i=x;m=x;
                elif (sgi_values[wells,i]<=-1.0 and sgi_values[wells,i]>-1.5):
                    sev_d.append(1)
                    if i==len(sgi_values[0,:])-2:
                        print("No drought event")
                    elif i== len(sgi_values[0,:])-1:
                        print("End of GW time series")
                    if (sgi_values[wells,i+1]<=-1.0 and sgi_values[wells,i+1]>-1.5):
                        x=i+2
                        sev_d.append(1)
                        if (sgi_values[wells,i+2]<=-1.0 and sgi_values[wells,i+2]>-1.5):
                            x=i+3
                            sev_d.append(1)
                            if i+2==len(sgi_values[0,:])-1:
                                print("End of GW time series")
                            else:
                                while (sgi_values[wells,x]<=-1.0 and sgi_values[wells,x]>-1.5):
                                    x=x+1
                                    sev_d.append(1)
                                    if x==len(sgi_values[0,:]):
                                        break
                                severe_GWD.append(severe_count+1)
                                severe_count=severe_count+1
                    i=x;m=x;
                else:
                    if sgi_values[wells,i]<=-1.5:
                        ext_d.append(1)
                        if i==len(sgi_values[0,:])-2:
                            print("No drought event")
                        elif i== len(sgi_values[0,:])-1:
                            print("End of GW time series")
                        if (sgi_values[wells,i+1]<=-1.5):
                            x=i+2
                            ext_d.append(1)
                            if (sgi_values[wells,i+2]<=-1.5):
                                x=i+3
                                ext_d.append(1)
                                if i+2==len(sgi_values[0,:])-1:
                                    print("End of GW time series")
                                else:
                                    while (sgi_values[wells,x]<=-1.5):
                                        x=x+1
                                        ext_d.append(1)
                                        if x==len(sgi_values[0,:]):
                                            break
                                    extreme_GWD.append(extreme_count+1)
                                    extreme_count=extreme_count+1
                i=x;m=x;
            well_wise_mild.append(max(mild_GWD))
            well_wise_moderate.append(max(moderate_GWD))
            well_wise_severe.append(max(severe_GWD))
            well_wise_extreme.append(max(extreme_GWD)) 
            DFI.append(((1*sum(mild_d))+(2*sum(mod_d))+(3*sum(sev_d))+(4*sum(ext_d)))/(4*len(sgi_values[0,:])))
    district_wise_mild.append(median(well_wise_mild))
    district_wise_moderate.append(median(well_wise_moderate))
    district_wise_severe.append(median(well_wise_severe))
    district_wise_extreme.append(median(well_wise_extreme))
    district_wise_DFI.append(median(DFI))
regions_mild={'RAY':sum(district_wise_mild[0:4]),'SCA':sum(district_wise_mild[4:8]),'NCA':sum(district_wise_mild[8:])}
regions_moderate={'RAY':sum(district_wise_moderate[0:4]),'SCA':sum(district_wise_moderate[4:8]),'NCA':sum(district_wise_moderate[8:])}
regions_severe={'RAY':sum(district_wise_severe[0:4]),'SCA':sum(district_wise_severe[4:8]),'NCA':sum(district_wise_severe[8:])}
regions_extreme={'RAY':sum(district_wise_extreme[0:4]),'SCA':sum(district_wise_extreme[4:8]),'NCA':sum(district_wise_extreme[8:])}
y1=np.array(list(regions_mild.values()));y2=np.array(list(regions_moderate.values()));y3=np.array(list(regions_severe.values()));y4=np.array(list(regions_extreme.values()));
ticks=['CHI','ATP','KUR','CUD','NEL','PRA','KRI','GUN','WG','VIS','EG','VZM','SRI']
fig,ax=plt.subplots(nrows=1,ncols=1,figsize=(15,8),dpi=600,sharex=True)
li=[0,1,2,3,4,5,6,7,8,9,10,11,12]
for dis in range(0,13):
    y1=np.array(district_wise_mild[dis]);y2=np.array(district_wise_moderate[dis]);y3=np.array(district_wise_severe[dis]);y4=np.array(district_wise_extreme[dis]);
    ax.bar(li[dis],y1,width=0.2,color='green')
    ax.bar(li[dis],y2,bottom=y1,width=0.2,color='orange')
    ax.bar(li[dis],y3,bottom=y1+y2,width=0.2,color='maroon')
    ax.bar(li[dis],y4,bottom=y1+y2+y3,width=0.2,color='red')
#ax.text(0,-50,'RAY-Rayalaseema, SCA-South Coastal Andhra, NCA-North Coastal Andhra',fontsize=16,weight='bold')
ax.legend(["Mild_GWD","Moderate_GWD","Severe_GWD","Extreme_GWD"])
ax.set_ylabel("No.of GWDs",weight='bold',fontsize=16)
ax.text(0,110,'b)',style='italic',fontsize=16,weight='bold')
plt.xticks(range(0,13),ticks,rotation='horizontal',weight='bold',fontsize=16)
plt.show()
            
    
                    
                
                                
