#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%%
df = pd.read_csv('dataframe\original_user_data\DlRlcStats.csv', sep=',')
df
#%%
user1 = df[df['RNTI']==1]
user2 = df[df['RNTI']==2]
user3 = df[df['RNTI']==3]
user4 = df[df['RNTI']==4]
user5 = df[df['RNTI']==5]
user6 = df[df['RNTI']==6]
user7 = df[df['RNTI']==7]
user8 = df[df['RNTI']==8]
user9 = df[df['RNTI']==9]
user10 = df[df['RNTI']==10]
# %%
time1 = user1['% start']
delay1 =user1['delay']

time2 = user2['% start']
delay2 =user2['delay']

time3 = user3['% start']
delay3 =user3['delay']

time4 = user4['% start']
delay4 =user4['delay']

time5 = user5['% start']
delay5 =user5['delay']

time6 = user6['% start']
delay6 =user6['delay']

time7 = user7['% start']
delay7 =user7['delay']

time8 = user8['% start']
delay8 =user8['delay']

time9 = user9['% start']
delay9 =user9['delay']

time9 = user9['% start']
delay9 =user9['delay']

time10 = user10['% start']
delay10 =user10['delay']
# %%
plt.plot(time1,delay1,label='user1',color ='blue')
plt.plot(time2,delay2,label='user2',color ='green')
plt.plot(time3,delay3,label='user3',color ='orange')
plt.plot(time4,delay4,label='user4',color ='gray')
plt.plot(time5,delay5,label='user5',color ='violet')
plt.plot(time6,delay6,label='user6',color ='yellow')
plt.plot(time7,delay7,label='user7',color ='brown')
plt.plot(time8,delay8,label='user8',color ='pink')
plt.plot(time9,delay9,label='user9',color ='red')
plt.plot(time10,delay10,label='user10',color ='black')
plt.ylim(0.00062,0.0011)
plt.legend(loc='upper left',bbox_to_anchor = (1,1),ncol=1,fontsize ='medium',title='users',title_fontsize='large')
plt.title('Delay Data-Original Position')
plt.xlabel('Time(s)')
plt.ylabel('Delay (ms)')
plt.show()

#____POSICIONAMENTO ORIGINAL__________


#%%
df2 = pd.read_csv('dataframe\optmized_user_data\DlRlcStats.csv', sep=',')
df2
#%%
ouser1 = df2[df2['RNTI']==1]
ouser2 = df2[df2['RNTI']==2]
ouser3 = df2[df2['RNTI']==3]
ouser4 = df2[df2['RNTI']==4]
ouser5 = df2[df2['RNTI']==5]
ouser6 = df2[df2['RNTI']==6]
ouser7 = df2[df2['RNTI']==7]
ouser8 = df2[df2['RNTI']==8]
ouser9 = df2[df2['RNTI']==9]
ouser10 = df2[df2['RNTI']==10]
# %%
time1 = ouser1['% start']
delay1 =ouser1['delay']

time2 = ouser2['% start']
delay2 =ouser2['delay']

time3 = ouser3['% start']
delay3 =ouser3['delay']

time4 = ouser4['% start']
delay4 =ouser4['delay']

time5 = ouser5['% start']
delay5 =ouser5['delay']

time6 = ouser6['% start']
delay6 =ouser6['delay']

time7 = ouser7['% start']
delay7 =ouser7['delay']

time8 = ouser8['% start']
delay8 =ouser8['delay']

time9 = ouser9['% start']
delay9 =ouser9['delay']

time9 = ouser9['% start']
delay9 =ouser9['delay']

time10 = ouser10['% start']
delay10 =ouser10['delay']
# %%
plt.plot(time1,delay1,label='user-opt1',color ='blue')
plt.plot(time2,delay2,label='user-opt2',color ='green')
plt.plot(time3,delay3,label='user-opt3',color ='orange')
plt.plot(time4,delay4,label='user-opt4',color ='gray')
plt.plot(time5,delay5,label='user-opt5',color ='violet')
plt.plot(time6,delay6,label='user-opt6',color ='yellow')
plt.plot(time7,delay7,label='user-opt7',color ='brown')
plt.plot(time8,delay8,label='user-opt8',color ='pink')
plt.plot(time9,delay9,label='user-opt9',color ='red')
plt.plot(time10,delay10,label='user-opt10',color ='black')
plt.ylim(0.00062,0.00083)
plt.legend(loc='upper left',bbox_to_anchor = (1,1),ncol=1,fontsize ='medium',title='users',title_fontsize='large')
plt.title('Delay Data-Optmized Position')
plt.xlabel('Time(s)')
plt.ylabel('Delay (ms)')
plt.show()
#%%
user4['delay'].mean() > ouser4['delay'].mean()
#%%


# %%
user3['delay'].mean() > ouser3['delay'].mean()
#%%

#%%
user5['delay'].mean() > ouser5['delay'].mean()
