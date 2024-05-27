#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# %%
df = pd.read_csv('DlRlcStats.csv',usecols=['% start', 'RNTI', 'delay'	] , sep=';')
df.describe()
#%%
delay_unique_cout = pd.Series(df['delay'].unique())
delay_unique_cout
#%%
u1 = df[df['RNTI']== 1]
u2 = df[df['RNTI']== 2]
u3 = df[df['RNTI']== 3]
u4 = df[df['RNTI']== 4]
u5 = df[df['RNTI']== 5]
u6 = df[df['RNTI']== 6]
u7 = df[df['RNTI']== 7]
u8 = df[df['RNTI']== 8]
u9 = df[df['RNTI']== 9]
u10 = df[df['RNTI']== 10]
# %%
# o tempo é o mesmo para todos, menos para u7
t1 = u1['% start']
t2 = u2['% start']
t3 = u3['% start']
t4 = u4['% start']
t5 = u5['% start']
t6 = u6['% start']
t7 = u7['% start']
t8 = u8['% start']
t9 = u9['% start']
t10 = u10['% start']
# %%
delay1 = u1['delay']
delay1 = np.where( delay1 == 0, np.nan, delay1)
delay2 = u2['delay']
delay2 = np.where( delay2 == 0, np.nan, delay2)
delay3 = u3['delay']
delay3 = np.where( delay3 == 0, np.nan, delay3)
delay4 = u4['delay']
delay4 = np.where( delay4 == 0, np.nan, delay4)
delay5 = u5['delay']
delay5 = np.where( delay5 == 0, np.nan, delay5)
delay6 = u6['delay']
delay6 = np.where( delay6 == 0, np.nan, delay6)

delay7 = u7['delay']
delay7 = np.where( delay7 == 0, np.nan, delay7)

delay8 = u8['delay']
delay8 = np.where( delay8 == 0, np.nan, delay8)

delay9 = u9['delay']
delay9 = np.where( delay9 == 0, np.nan, delay9)

delay10 = u10['delay']
delay10 = np.where( delay10 == 0, np.nan, delay10)


pd.DataFrame(delay1)
#%%
plt.plot(t1, delay1, label='1')
plt.plot(t2, delay2, label='2')
plt.plot(t3, delay3, label='3')
plt.plot(t4, delay4, label='4')
plt.plot(t5, delay5, label='5')
plt.plot(t6, delay6, label='6')
plt.plot(t7, delay7, label='7')
plt.plot(t8, delay8, label='8')
plt.plot(t9, delay9, label='9')
plt.plot(t10, delay10, label='10')
plt.title('Delay rate')
plt.xlabel('Tempo(s)')
plt.ylabel('Delay(ms)')
plt.legend(loc='upper left',
           bbox_to_anchor=(1,1),
           ncol=1,
           fontsize='medium',
           title='Users',
           title_fontsize='large',
)


plt.show()
# %%
