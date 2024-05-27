#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# %%
df = pd.read_csv('DlRlcStats.csv',usecols=['% start', 'RNTI', 'delay'	] , sep=';')
type(df)
#%%
df['delay'].unique()
#%%
df1 = df[df['RNTI'] == 1]
df2 = df[df['RNTI'] ==2]
df3 = df[df['RNTI']==3]
# %%
# o tempo é o mesmo para todos
tempo = df1['% start']
# %%
delay1 = df1['delay']
delay1 = np.where( delay1 == 0, np.nan, delay1)
delay2 = df2['delay']
delay2 = np.where( delay2 == 0, np.nan, delay2)
delay3 = df3['delay']
delay3 = np.where( delay3 == 0, np.nan, delay3)
pd.DataFrame(delay1)
#%%
plt.plot(tempo, delay1, label='1')
plt.plot(tempo, delay2, label='2')
plt.plot(tempo, delay3, label='3')
plt.title('Delay rate')
plt.xlabel('Tempo(s)')
plt.ylabel('Delay(ms)')
plt.legend(loc='upper left',
           bbox_to_anchor=(1,1),
           ncol=1,
           fontsize='medium',
           title='Legenda',
           title_fontsize='large',
)


plt.show()
# %%
