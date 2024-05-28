#%%
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
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
delay

#%%
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(tempo, delay)
plt.plot(tempo, delay, 
        
         linewidth=1, linestyle='-',
          color = 'blue')

plt.title('Delay rate (500m)')
plt.xlabel('Tempo(s)')
plt.ylabel('Delay(ms)')
plt.xticks(range(0, 61, 10)) # intervalo no eixo x
ax.set_xlim(0,61) # tamanho do eixo x
ax.set_ylim(0.0006, 0.00081) # variação em y
ax.yaxis.set_major_locator(MultipleLocator(0.00005)) # PA em y
plt.show
# %%

# %%
