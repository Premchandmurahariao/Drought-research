# -*- coding: utf-8 -*-
"""
Created on Fri May 20 10:01:10 2022

@author: mprem
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
from sklearn.metrics import r2_score
from scipy.stats import pearsonr
sgi=pd.read_csv(r"E:\Prem PhD\Watershed management\Groundwater data\CSV_Files\Newtrial\SGI.csv")
sgi=sgi.iloc[:,:].values
district_wise_data=pd.read_csv(r"E:\Prem PhD\Watershed management\Groundwater data\SGI_graphs\GW_drought_speed\District_wise_drought_data.csv")
district_wise_data=district_wise_data.iloc[:,:].values
drought_events=district_wise_data[:,9]
wells=district_wise_data[:,1];num=0;
districts={0:"CHITTOOR",1:"ANANTAPUR",2:"WEST GODAVARI",3:"VISAKHAPATNAM",4:"EAST GODAVARI",5:"VIZIANAGARAM",6:"SRIKAKULAM",7:"SRI POTTI SRIRAMULU NELLORE",8:"PRAKASAM",9:"KURNOOL",10:"KRISHNA",11:"GUNTUR",12:"Y.S.R."}
well=0;district_wise_optimum=np.zeros((len(sgi),8));optimum_IDS=[];optimum_IRS=[];IDS_dist=[];IRS_dist=[];
def nse(predictions, targets):
    if (1-(np.sum((predictions-targets)**2)/np.sum((targets-np.mean(targets))**2)))== ValueError or RuntimeWarning:
        return 0
    else:
        return (1-(np.sum((predictions-targets)**2)/np.sum((targets-np.mean(targets))**2)))
def R2_score(targets,predictions):
    if r2_score(targets,predictions)== ValueError or RuntimeWarning:
        return 0
    else:
        return (r2_score(targets,predictions))
for district in range(0,13):
    while sgi[well,1]==districts[district]:
        Avg_RE_d=[];Avg_RE_r=[]; R2_score_d=[]; R2_score_r=[];NSE_d=[];NSE_r=[];
        IDS_IRS=pd.read_csv(r"E:\Prem PhD\Watershed management\Groundwater data\SGI_graphs\GW_drought_speed\mean_IDS_IRS\mean_IDS_IRS_{}.csv".format(sgi[well,2]))
        IDS_IRS=IDS_IRS.iloc[:,:].values
        m_IDS=IDS_IRS[0:int(drought_events[well]),1];m_IRS=IDS_IRS[int(drought_events[well]):int(2*drought_events[well]),1];
        simulated=pd.read_csv(r"E:\Prem PhD\Watershed management\Groundwater data\SGI_graphs\GW_drought_speed\Groups\Groups_{}.csv".format(sgi[well,2]))
        simulated=simulated.iloc[:,:].values
        sim_duration_d=np.reshape(simulated[0,:],(len(simulated[0,:]),1))
        sim_duration_r=np.reshape(simulated[1,:],(len(simulated[1,:]),1))
        observed=pd.read_csv(r"E:\Prem PhD\Watershed management\Groundwater data\SGI_graphs\GW_drought_speed\OBS_Duration\duration_{}.csv".format(sgi[well,2]))
        observed=observed.iloc[:,:].values
        obs_duration_d=np.reshape(observed[0,:],(len(observed[0,:]),1))
        obs_duration_r=np.reshape(observed[1,:],(len(observed[1,:]),1))
        offset=int(drought_events[well]-round(2/3*drought_events[well]))
        for events in range(0,1):
            avg_sim_dur=(sim_duration_d[0:offset,0]).mean()
            avg_sim_dur_r=(sim_duration_r[0:offset,0]).mean()
            avg_obs_dur=(obs_duration_d[0:offset,0]).mean()
            avg_obs_dur_r=(obs_duration_r[0:offset,0]).mean()
            Avg_RE_d.append((abs(avg_sim_dur-avg_obs_dur)/avg_obs_dur)*100)
            Avg_RE_r.append((abs(avg_sim_dur-avg_obs_dur)/avg_obs_dur)*100)
            R2_score_d.append(R2_score((obs_duration_d[0:offset]),(sim_duration_d[0:offset])))
            R2_score_r.append(R2_score((obs_duration_r[0:offset]),(sim_duration_r[0:offset])))
            NSE_d.append(nse(sim_duration_d[0:offset],obs_duration_d[0:offset]))
            NSE_r.append(nse(sim_duration_r[0:offset],obs_duration_r[0:offset]))
        for events in range (1,int(drought_events[well])):
            avg_sim_dur=(sim_duration_d[offset*events:offset*(events+1),0]).mean()
            avg_sim_dur_r=(sim_duration_r[offset*events:offset*(events+1),0]).mean()
            avg_obs_dur=(obs_duration_d[offset*events:offset*(events+1),0]).mean()
            avg_obs_dur_r=(obs_duration_r[offset*events:offset*(events+1),0]).mean()
            Avg_RE_d.append((abs(avg_sim_dur-avg_obs_dur)/avg_obs_dur)*100)
            Avg_RE_r.append((abs(avg_sim_dur_r-avg_obs_dur_r)/avg_obs_dur_r)*100)
            #R2_score_d.append(R2_score((obs_duration_d[offset*events:offset*(events+1)]),(sim_duration_d[offset*events:offset*(events+1)])))
            #R2_score_r.append(R2_score((obs_duration_r[offset*events:offset*(events+1)]),(sim_duration_r[offset*events:offset*(events+1)])))
            #NSE_d.append(nse(sim_duration_d[offset*events:offset*(events+1)],obs_duration_d[offset*events:offset*(events+1)]))
            #NSE_r.append(nse(sim_duration_r[offset*events:offset*(events+1)],obs_duration_r[offset*events:offset*(events+1)]))
        #if Avg_RE_d.index(min(abs(h) for h in Avg_RE_d)) and R2_score_d.index(max(R2_score_d)) == NSE_d.index(max(NSE_d)):
            #optimum_IDS.append(m_IDS[Avg_RE_d.index(min(Avg_RE_d))])
        #else:
            #optimum_IDS.append(mean(m_IDS[Avg_RE_d.index(min(Avg_RE_d))]+m_IDS[R2_score_d.index(max(R2_score_d))]+m_IDS[NSE_d.index(max(NSE_d))]))
        #if Avg_RE_r.index(min(Avg_RE_r)) and R2_score_r.index(max(R2_score_r)) == NSE_r.index(max(NSE_r)):
            #optimum_IRS.append(m_IRS[Avg_RE_r.index(min(Avg_RE_r))])
        #else:
            #optimum_IRS.append(mean(m_IRS[Avg_RE_r.index(min(Avg_RE_r))]+m_IRS[R2_score_r.index(max(R2_score_r))]+m_IRS[NSE_r.index(max(NSE_r))]))
        optimum_IDS.append(m_IDS[Avg_RE_d.index(min(Avg_RE_d))])
        optimum_IRS.append(m_IRS[Avg_RE_r.index(min(Avg_RE_r))])
        district_wise_optimum[well,0]=sgi[well,2]
        district_wise_optimum[well,1]=optimum_IDS[well]
        district_wise_optimum[well,2]=optimum_IRS[well]
        district_wise_optimum[well,3]=min(Avg_RE_d)
        district_wise_optimum[well,4]=min(Avg_RE_r)
        well=well+1
        if well >=len(sgi):
            break
#(pd.DataFrame(district_wise_optimum)).to_csv(r"E:\Prem PhD\Watershed management\Groundwater data\SGI_graphs\GW_drought_speed\District_wise_optimum_data_3.csv")
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(15, 5),dpi=400,sharex=True)
ticks=['CHITTOOR','ANANTAPUR','WEST GODAVARI','VISAKHAPATNAM','EAST GODAVARI','VIZIANAGARAM','SRIKAKULAM','NELLORE','PRAKASAM','KURNOOL','KRISHNA','GUNTUR','CUDDAPAH']
district_wise_optimum=(pd.read_csv(r"E:\Prem PhD\Watershed management\Groundwater data\SGI_graphs\GW_drought_speed\District_wise_optimum_data.csv")).iloc[:,:].values
medians_D=[];medians_R=[];
for dist in range(0,13):
    prev=num
    for total in range(0,len(sgi)):
        if sgi[total,1]==districts[dist]:
            num=num+1
    IDS_dist.append(district_wise_optimum[prev:num,-2])
    IRS_dist.append(district_wise_optimum[prev:num,-1])
    bplot1 = axs[0].boxplot(IDS_dist[dist],positions=[dist],widths=0.45,vert=True,patch_artist=False,showmeans=False,showfliers=False)
    bplot2 = axs[1].boxplot(IRS_dist[dist],positions=[dist],widths=0.45,vert=True,patch_artist=False,showmeans=False,showfliers=False)
    medians_D.append([round(item.get_ydata()[0], 1) for item in bplot1['medians']][0])
    medians_R.append([round(item.get_ydata()[0], 1) for item in bplot2['medians']][0])
axs[0].set_ylabel('TDD',weight='bold')
#axs[0].set_title('District wise optimum IDS variation',weight='bold')
axs[1].set_ylabel('Severity',weight='bold')
#axs[1].set_title('District wise optimum IRS variation',weight='bold')
plt.sca(axs[0])
axs[0].text(0,75,'c)',style='italic',fontsize=12,weight='bold')
plt.xticks(range(0,13),ticks,rotation='vertical',weight='bold')
plt.sca(axs[1])
axs[1].text(0,-80,'d)',style='italic',fontsize=12,weight='bold')
plt.xticks(range(0,13),ticks,rotation='vertical',weight='bold')
axs[0].legend([bplot1["medians"][0]],["Median"],loc='best')
axs[1].legend([bplot2["medians"][0]],["Median"],loc='best')
plt.show()
#opt_data=(pd.read_csv(r"E:\Prem PhD\Watershed management\Groundwater data\SGI_graphs\GW_drought_speed\District_wise_optimum_data.csv"))
#opt_data=opt_data.iloc[:,:].values
#for well in range(0,len(opt_data)):
    #total_var=pd.read_csv(r"E:\Prem PhD\Watershed management\Groundwater data\SGI_graphs\GW_drought_speed\TVDP_TVRP\TVDP_TVRP_{}.csv".format(int(opt_data[well,1])))
    #total_var=total_var.iloc[:,:].values
    #sum_TVDP=(total_var[0:int(len(total_var)/2),1])
    #sum_TVRP=(total_var[int(len(total_var)/2):,2])
    #event_wise_DDD=pd.read_csv(r"E:\Prem PhD\Watershed management\Groundwater data\SGI_graphs\GW_drought_speed\Event_wise\DDD_DRD_{}.csv".format(int(opt_data[well,1])))
    #event_wise_DDD=event_wise_DDD.iloc[:,:].values
    #e_DDD=event_wise_DDD[0:int(len(event_wise_DDD)/2),1]
    #e_DRD=event_wise_DDD[int(len(event_wise_DDD)/2):,1]
    #o_IDS=opt_data[well,2];o_IRS=opt_data[well,3];
    #s_DDD=sum_TVDP/o_IDS;s_DRD=sum_TVRP/o_IRS
    #district_wise_optimum[well,5]=((pearsonr(e_DDD,s_DDD))[0]**2)
    #district_wise_optimum[well,6]=((pearsonr(e_DRD,s_DRD))[0]**2)
#(pd.DataFrame(district_wise_optimum)).to_csv(r"E:\Prem PhD\Watershed management\Groundwater data\SGI_graphs\GW_drought_speed\District_wise_optimum_data.csv")

            
        


                                                                                                     