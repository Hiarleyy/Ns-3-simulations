#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%%
data = pd.read_csv('DlRlcStats.csv', sep=';', 
                   usecols=['% start', 'delay'])
df = pd.DataFrame(data)
df
# %%
tempo = df["% start"]
tempo
#%%
delay = df['delay']
delay.value_counts()
#%%
delay = delay.unique()
delay
# %%
tempo = np.linspace(0, 60)
delay1 = np.full_like(tempo, delay[0])
#delay2 = np.full_like(tempo, delay[1])

#%%
plt.plot(tempo, delay1)
#plt.plot(tempo, delay2)
plt.title('Delay rate (150m)')
plt.xlabel('Tempo(s)')
plt.ylabel('Delay(ms)')
plt.show

# %%
