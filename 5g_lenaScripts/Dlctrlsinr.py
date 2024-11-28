#%%
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#%%
df = pd.read_csv('DlCtrlSinr.csv', sep=',')

df
#%%
df['']
# %%
# Função para filtrar DataFrame por Cellid
def filter_by_CellId(df, CellId_values):
    return {CellId: df[df['CellId'] == CellId] for CellId in CellId_values}

CellId_values = [2, 4]  # Apenas os valores de CellId 2 e 4
filtered_dfs = filter_by_CellId(df, CellId_values)


plt.figure(figsize=(12, 8))

colors = ['b', 'g']  # Define colors for each user
markers = ['o', 's']  # Define markers for each user
linestyles = ['-', '--']  # Define line styles for each user

for i, CellId in enumerate(CellId_values):
    user_df = filtered_dfs[CellId]
    plt.plot(user_df['Time'], user_df['SINR(dB)'], label=f'CellId {CellId}', color=colors[i], marker=markers[i], linestyle=linestyles[i], markersize=1, linewidth=1.5, alpha=0.7)

plt.title('SINR over Time for CellIds 2 and 4', fontsize=16)
plt.xlabel('Time (sec)', fontsize=14)
plt.ylabel('SINR (dB)', fontsize=14)
plt.legend(title='CellIds', fontsize=12, title_fontsize='13')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.minorticks_on()
plt.tight_layout()
plt.show()


#%%
# Clean plot
plt.figure(figsize=(12, 8))

colors = ['b', 'g']  # Define colors for each user
markers = ['o', 's']  # Define markers for each user
linestyles = ['-', '--']  # Define line styles for each user

for i, CellId in enumerate(CellId_values):
    user_df = filtered_dfs[CellId]
    plt.plot(user_df['Time'], user_df['SINR(dB)'], label=f'CellId {CellId}', color=colors[i], marker=markers[i], linestyle=linestyles[i], markersize=5, linewidth=1.5)

plt.title('Clean SINR over Time for CellIds 2 and 4', fontsize=16)
plt.xlabel('Time (sec)', fontsize=14)
plt.ylabel('SINR (dB)', fontsize=14)
plt.legend(title='CellIds', fontsize=12, title_fontsize='13')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.minorticks_on()
plt.tight_layout()
plt.show()

# Heatmap plot using seaborn
#%%
fig, axs = plt.subplots(len(CellId_values), 1, figsize=(12, 8), sharex=True)

for i, CellId in enumerate(CellId_values):
    user_df = filtered_dfs[CellId]
    
    # Remover duplicatas agregando pela média
    user_df = user_df.groupby(['Time', 'CellId'], as_index=False).mean()
    
    pivot_table = user_df.pivot(index="Time", columns="CellId", values="SINR(dB)")
    sns.heatmap(pivot_table, ax=axs[i], cmap="YlGnBu", cbar=True)
    
    axs[i].set_title(f'SINR Heatmap for CellId {CellId}', fontsize=14)
    axs[i].set_ylabel('Time (sec)', fontsize=12)

axs[-1].set_xlabel('CellId', fontsize=12)

plt.tight_layout()
plt.show()


# %%
grouped_df = df.groupby('CellId')['SINR(dB)'].describe()
grouped_df
# %%
