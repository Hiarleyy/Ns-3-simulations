#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# %%
data = pd.read_csv('DlRlcStats-500m.csv', usecols=["% start","delay"] , 
                   sep=';')
data

# %%
df = pd.DataFrame(data)
df
# %%
tempo = df['% start']
tempo # series
# %%
delay = df['delay']
delay.value_counts()
#%%
delay = delay.unique()
delay
# %%
tempo = np.linspace(0, 60)
delay1 = np.full_like(tempo, delay[0])
#delay2 = np.full_like(tempo, delay[1])
delay3 = np.full_like(tempo, delay[2])
delay4 = np.full_like(tempo, delay[3])
delay5 = np.full_like(tempo, delay[4])
#%%
plt.plot(tempo, delay1)
#plt.plot(tempo, delay2)
plt.plot(tempo, delay3)
plt.plot(tempo, delay4)
plt.plot(tempo, delay5)
plt.title('Delay rate (500m)')
plt.xlabel('Tempo(s)')
plt.ylabel('Delay(ms)')
plt.show
# %%

# %%
