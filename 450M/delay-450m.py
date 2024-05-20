#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%%
data = pd.read_csv('DlRlcStats.csv')
df = pd.DataFrame(data)
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
tempo = np.linspace(0, 60, 100)
delay1 = np.full_like(tempo, delay[0])
#delay2 = np.full_like(tempo, delay[1])
delay3 = np.full_like(tempo, delay[2])
#%%
plt.plot(tempo, delay1)
#plt.plot(tempo, delay2)
plt.plot(tempo, delay3)
plt.title('Delay rate (450m)')
plt.xlabel('Tempo(s)')
plt.ylabel('Delay(ms)')
plt.show

# %%