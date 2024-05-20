#%%
from matplotlib.ticker import MultipleLocator
import pandas as pd
import matplotlib.pyplot as plt
# %%
data = pd.read_csv('RxPacketTrace-100Ghz.txt', sep='\s+')
df = pd.DataFrame(data)
df
#%%
Time = df['time']
Time
#%%
db = df['SINR(dB)']
db.describe()
# %%
## criando o gráfico

fig, ax = plt.subplots()
ax.plot(Time, db)
plt.plot(Time, db, linewidth=1, linestyle='-',
          label='Sinr',
          markersize=2,marker='o', color = 'blue'
          )
plt.title('Signal rate (50m)')

plt.xlabel('Time (s)')
plt.xticks(range(0, 101, 10))
ax.set_xlim(0,101)
ax.set_ylim(46.6, 47.6)
ax.yaxis.set_major_locator(MultipleLocator(0.1))
plt.ylabel('SINR (dB)')
plt.legend()
plt.show()

# %%
