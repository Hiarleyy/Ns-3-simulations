
#%%
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

#%%
df = pd.read_csv('tratamento/files/csv/DlCtrlSinr.csv')

df
# %%
# Função para filtrar DataFrame por Cellid
def filter_by_CellId(df, CellId_values):
    return {CellId: df[df['CellId'] == CellId] for CellId in CellId_values}

CellId_values = [2, 4, 6, 8]  # Apenas os valores de CellId 2, 4, 6 e 8
filtered_dfs = filter_by_CellId(df, CellId_values)

plt.figure(figsize=(12, 8))

colors = ['b', 'g', 'r', 'c']  # Define colors for each user
markers = ['o', 's', 'o', 's']  # Define markers for each user
linestyles = ['-', '--', '--', '--']  # Define line styles for each user

for i, CellId in enumerate(CellId_values):
    user_df = filtered_dfs[CellId]
    plt.plot(user_df['Time'], user_df['SINR(dB)'], label=f'CellId {CellId}', color=colors[i], marker=markers[i], linestyle=linestyles[i], markersize=1, linewidth=1.5, alpha=0.5)  # Set alpha to 0.5 for translucency

plt.title('SINR over Time for CellIds 2, 4, 6, and 8', fontsize=16)
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

colors = ['b', 'g', 'r', 'c']  # Define colors for each user
markers = ['o', 's', 'd', '^']  # Define markers for each user
linestyles = ['-', '--', '-.', ':']  # Define line styles for each user

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

#%%
# 3D Density plot for each CellId

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

for i, CellId in enumerate(CellId_values):
    user_df = filtered_dfs[CellId]
    x = user_df['Time']
    y = user_df['SINR(dB)']
    z_stat = user_df['SINR(dB)'].mean()  # Calculate the mean SINR for each CellId
    z = np.zeros_like(x) + z_stat  # Use the mean SINR as the z-axis value
    
    ax.scatter(x, y, z, label=f'CellId {CellId}', color=colors[i % len(colors)], marker=markers[i % len(markers)], alpha=0.1)  # Set alpha to 0.1 for more translucency

# Add legend separately to avoid transparency
handles, labels = ax.get_legend_handles_labels()
for handle in handles:
    handle.set_alpha(1.0)  # Set alpha to 1.0 for legend items

ax.set_title('Gráfico de densidade (SINR) com média', fontsize=16)
ax.set_xlabel('Time (sec)', fontsize=11)
ax.set_ylabel('SINR (dB)', fontsize=11)
ax.legend(handles, labels, title='CellIds', fontsize=11, title_fontsize='11')
ax.view_init(elev=20., azim=-35)  # Adjust the elevation and angle for better visualization
plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.2)  # Adjust the plot to make space for the z-axis label
ax.set_zlabel('SINR MEAN', fontsize=11)
plt.show()






#%%
#%%
# Separate plots for each CellId
for i, CellId in enumerate(CellId_values):
    plt.figure(figsize=(12, 8))
    user_df = filtered_dfs[CellId]
    plt.plot(user_df['Time'], user_df['SINR(dB)'], label=f'CellId {CellId}', color=colors[i % len(colors)], marker=markers[i % len(markers)], linestyle=linestyles[i % len(linestyles)], markersize=5, linewidth=1.5)
    
    plt.title(f'SINR over Time for CellId {CellId}', fontsize=16)
    plt.xlabel('Time (sec)', fontsize=14)
    plt.ylabel('SINR (dB)', fontsize=14)
    plt.legend(title='CellId', fontsize=12, title_fontsize='13')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.minorticks_on()
    plt.tight_layout()
    plt.show()
    # Density plot for each CellId
    #%%
    for i, CellId in enumerate(CellId_values):
        plt.figure(figsize=(12, 8))
        user_df = filtered_dfs[CellId]
        sns.kdeplot(user_df['SINR(dB)'], label=f'CellId {CellId}', color=colors[i % len(colors)], linestyle=linestyles[i % len(linestyles)], linewidth=1.5)
        
        plt.title(f'Density Plot of SINR for CellId {CellId}', fontsize=16)
        plt.xlabel('SINR (dB)', fontsize=14)
        plt.ylabel('Density', fontsize=14)
        plt.legend(title='CellId', fontsize=12, title_fontsize='13')
        plt.grid(True, which='both', linestyle='--', linewidth=0.5)
        plt.tight_layout()
        plt.show()

#%%






#%%
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
