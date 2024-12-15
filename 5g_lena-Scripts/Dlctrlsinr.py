
#%%
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from pkg_resources import dist_factory
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
# Calculate the percentage difference for each CellId at the start and end of the Time column
percentage_diff = {}

# Get unique RNTI values
rnti_values = df['RNTI'].unique()

for CellId in CellId_values:
    percentage_diff[CellId] = {}
    for RNTI in rnti_values:
        user_df = filtered_dfs[CellId][filtered_dfs[CellId]['RNTI'] == RNTI]
        if not user_df.empty:
            start_time = user_df['Time'].min()
            end_time = user_df['Time'].max()
            
            start_sinr = user_df[user_df['Time'] == start_time]['SINR(dB)'].values[0]
            end_sinr = user_df[user_df['Time'] == end_time]['SINR(dB)'].values[0]
            
            percentage_diff[CellId][RNTI] = ((end_sinr - start_sinr) / start_sinr) * 100

# Plot the percentage difference for each CellId and RNTI
for CellId in CellId_values:
    fig, ax = plt.subplots(figsize=(12, 8))
    rnti_diff = percentage_diff[CellId]
    bars = ax.bar(rnti_diff.keys(), rnti_diff.values(), color=[colors[CellId_values.index(CellId) % len(colors)] for _ in range(len(rnti_diff))], edgecolor='black')
    
    # Add value labels on top of each bar
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2f}%', ha='center', va='bottom' if yval >= 0 else 'top', fontsize=10, color='black')
    
    ax.axhline(0, color='black', linewidth=0.8)  # Add a horizontal line at y=0
    ax.set_ylim(min(rnti_diff.values()) - 5, max(rnti_diff.values()) + 5)  # Adjust y-axis limits with a margin
    ax.set_title(f'Percentage Difference in SINR for CellId {CellId}', fontsize=14)
    ax.set_ylabel('Percentage Difference (%)', fontsize=12)
    ax.set_xlabel('RNTI', fontsize=12)
    ax.grid(True, linestyle='--', linewidth=0.5, axis='y')
    ax.set_xticks(list(rnti_diff.keys()))
    ax.set_xticklabels([int(rnti) for rnti in rnti_diff.keys()], fontsize=12)
    plt.tight_layout()
    plt.show()

#%%
# %%
# Calculate the average percentage difference for each CellId
average_percentage_diff = {CellId: np.mean(list(rnti_diff.values())) for CellId, rnti_diff in percentage_diff.items()}

# Plot the average percentage difference for each CellId
fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.bar(average_percentage_diff.keys(), average_percentage_diff.values(), color=[colors[CellId_values.index(CellId) % len(colors)] for CellId in average_percentage_diff.keys()], edgecolor='black')

# Add value labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2f}%', ha='center', va='bottom' if yval >= 0 else 'top', fontsize=10, color='black')

ax.axhline(0, color='black', linewidth=0.8)  # Add a horizontal line at y=0
ax.set_ylim(min(average_percentage_diff.values()) - 5, max(average_percentage_diff.values()) + 5)  # Adjust y-axis limits with a margin
ax.set_title('Average Percentage Difference in SINR for Each CellId', fontsize=14)
ax.set_ylabel('Average Percentage Difference (%)', fontsize=12)
ax.set_xlabel('CellId', fontsize=12)
ax.grid(True, linestyle='--', linewidth=0.5, axis='y')
ax.set_xticks(list(average_percentage_diff.keys()))
ax.set_xticklabels([int(cellid) for cellid in average_percentage_diff.keys()], fontsize=12)
plt.tight_layout()
plt.show()
# %%
# Create a DataFrame to store the first and last Time values for each RNTI and CellId
time_values = []

for CellId in CellId_values:
    for RNTI in rnti_values:
        user_df = filtered_dfs[CellId][filtered_dfs[CellId]['RNTI'] == RNTI]
        if not user_df.empty:
            start_time = user_df['Time'].min()
            end_time = user_df['Time'].max()
            start_sinr = user_df[user_df['Time'] == start_time]['SINR(dB)'].values[0]
            end_sinr = user_df[user_df['Time'] == end_time]['SINR(dB)'].values[0]
            time_values.append({'CellId': CellId, 'RNTI': RNTI, 'Start Time': start_time, 'End Time': end_time, 'Start SINR': start_sinr, 'End SINR': end_sinr})

time_df = pd.DataFrame(time_values)
time_df
# %%
# Plot SINR variation over time for each RNTI, separated by CellId
for CellId in CellId_values:
    plt.figure(figsize=(12, 8))
    for RNTI in rnti_values:
        user_df = filtered_dfs[CellId][filtered_dfs[CellId]['RNTI'] == RNTI]
        if not user_df.empty:
            plt.plot(user_df['Time'], user_df['SINR(dB)'], label=f'RNTI {RNTI}', linestyle='-', linewidth=1.5, alpha=0.5)  # Set alpha to 0.5 for translucency
    
    plt.title(f'SINR Variation over Time for CellId {CellId}', fontsize=16)
    plt.xlabel('Time (sec)', fontsize=14)
    plt.ylabel('SINR (dB)', fontsize=14)
    plt.legend(title='RNTI', fontsize=12, title_fontsize='13')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.minorticks_on()
    plt.tight_layout()
    plt.show()
# %%
# Plot SINR variation over time for each RNTI, showing differences by CellId
for RNTI in rnti_values:
    plt.figure(figsize=(12, 8))
    for CellId in CellId_values:
        user_df = filtered_dfs[CellId][filtered_dfs[CellId]['RNTI'] == RNTI]
        if not user_df.empty:
            plt.plot(user_df['Time'], user_df['SINR(dB)'], label=f'CellId {CellId}', linestyle='-', linewidth=1.5, alpha=0.5)  # Set alpha to 0.5 for translucency
    
    plt.title(f'SINR Variation over Time for RNTI {RNTI}', fontsize=16)
    plt.xlabel('Time (sec)', fontsize=14)
    plt.ylabel('SINR (dB)', fontsize=14)
    plt.legend(title='CellId', fontsize=12, title_fontsize='13')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.minorticks_on()
    plt.tight_layout()
    plt.show()
# %%
df['RNTI'].value_counts()
# %%
# %%
