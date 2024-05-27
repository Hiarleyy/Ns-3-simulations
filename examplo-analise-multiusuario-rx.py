#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# %%
df = pd.read_csv('RxPacketTrace.txt', sep='\s+',
                 usecols=['DL/UL', 'time', 'rnti', 'SINR(dB)'])
# a coluna time tem 90k registros
# a colune SINR(dB) tem 90k registros somados para 10 users
df['SINR(dB)'].describe()
#%%
df['rnti'].value_counts()

#%%
#verificando valores unicos para o ruído
unique_SINR = pd.Series(df['SINR(dB)'].unique())
unique_SINR.count() # 10 valores unicos constantes para cada USER
# %%
#USERS (fazer uma função depois)
u1 = df[df['rnti']==1]
u2 = df[df['rnti']==2]
u3 = df[df['rnti']==3]
u4 = df[df['rnti']==4]
u5 = df[df['rnti']==5]
u6 = df[df['rnti']==6]
u7 = df[df['rnti']==7]
u8 = df[df['rnti']==8]
u9 = df[df['rnti']==9]
u10 = df[df['rnti']==10]
#%%
t1 = u1['time']
t2 = u2['time']
t3 = u3['time']
t4 = u4['time']
t5 = u5['time']
t6 = u6['time']
t7 = u7['time']
t8 = u8['time']
t9 = u9 ['time']
t10 = u10 ['time']
# %%

s1 = u1['SINR(dB)']
s2 = u2['SINR(dB)']
s3 = u3['SINR(dB)']
s4 = u4['SINR(dB)']
s5 = u5['SINR(dB)']
s6 = u6['SINR(dB)']
s7 = u7['SINR(dB)']
s8 = u8['SINR(dB)']
s9 = u9['SINR(dB)']
s10 = u10['SINR(dB)']
# %%
#GRAFICO
plt.plot(t1, s1, label='1')
plt.plot(t2, s2, label='2')
plt.plot(t3, s3, label='3')
plt.plot(t4, s4, label='4')
plt.plot(t5, s5, label='5')
plt.plot(t6, s6, label='6')
plt.plot(t7, s7, label='7')
plt.plot(t8, s8, label='8')
plt.plot(t9, s9, label='9')
plt.plot(t10, s10, label='10')
plt.title('SINR rate (10 users)')
plt.xlabel('time(s)')
plt.ylabel('SINR(dB)')
plt.legend(loc='upper left',
           bbox_to_anchor=(1,1),
           ncol=1,
           fontsize='medium',
           title='Users',
           title_fontsize='large',
)


plt.show()

