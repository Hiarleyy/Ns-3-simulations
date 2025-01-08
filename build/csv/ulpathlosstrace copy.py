#%%
import pandas as pd 
import matplotlib.pyplot as plt

#%%
df = pd.read_csv(r'C:\Users\Marcos Hiarley\Documents\GitHub\Ns-3-simulations\5g_lena-Scripts\datasets\csv\UlPathlossTrace.csv')
df = df[df['Time(sec)'] > 0.42]  # Filtra valores de 'Time(sec)' acima de 1
df['IMSI'].value_counts()

# %%
# Função para filtrar DataFrame por imsi
def filter_by_imsi(df, imsi_values):
    return {imsi: df[df['IMSI'] == imsi] for imsi in imsi_values}

imsi_values = range(1,6)  # p/ 2 usuarios
filtered_dfs = filter_by_imsi(df, imsi_values)

# %%
plt.figure(figsize=(15, 10))

# Define colors and markers for 10 users
colors = ['b', 'g', 'r', 'c', 'm']
markers = ['o', 's', 'D', '^', 'v']

for i, imsi in enumerate(imsi_values):
    user_df = filtered_dfs[imsi]
    user_df = user_df[user_df['Time(sec)'] > 1]  # Filtra valores de 'Time(sec)' acima de 1
    plt.plot(user_df['Time(sec)'], user_df['pathLoss(dB)'], label=f'imsi {imsi}', color=colors[i % len(colors)], marker=markers[i % len(markers)], linestyle='-', markersize=1)

plt.title('Path Loss UlPathlossTrace')
plt.xlabel('Time (sec)')
plt.ylabel('Path Loss (dB)')
plt.legend(title='Users')
plt.grid(True)
plt.show()

#%%
fig, axs = plt.subplots(len(imsi_values), 1, figsize=(15, 20), sharex=True)

for i, imsi in enumerate(imsi_values):
    user_df = filtered_dfs[imsi]
    axs[i].plot(user_df['Time(sec)'], user_df['pathLoss(dB)'], label=f'imsi {imsi}', linestyle='-', markersize=1)
    axs[i].set_title(f'Path Loss UlPathlossTrace {imsi}')
    axs[i].set_ylabel('Path Loss (dB)')
    axs[i].legend()
    axs[i].grid(True)
    # Adjust y-axis to show smaller variations

plt.xlabel('Time (sec)')
plt.tight_layout()
plt.show()

# %%
grouped_df = df.groupby('IMSI')['pathLoss(dB)'].describe()
grouped_df
# %%
df['CellId'].value_counts()

############################################################################################################

# %%
def filter_by_CellId(df, CellId_values):
    return {CellId: df[df['CellId'] == CellId] for CellId in CellId_values}

list = [1,3]
CellId_values = list   # p/ 2 usuarios
filtered_dfs = filter_by_CellId(df, CellId_values)

#%%
plt.figure(figsize=(15, 10))

# Define colors and markers for 10 users
colors = ['b', 'g', 'r', 'c', 'm']
markers = ['o', 's', 'D', '^', 'v']

for i, CellId in enumerate(CellId_values):
    user_df = filtered_dfs[CellId]
    plt.plot(user_df['Time(sec)'], user_df['pathLoss(dB)'], label=f'CellId {CellId}', color=colors[i % len(colors)], marker=markers[i % len(markers)], linestyle='-', markersize=1)

plt.title('Path Loss UlPathlossTrace')
plt.xlabel('Time (sec)')
plt.ylabel('Path Loss (dB)')
plt.legend(title='Users')
plt.grid(True)
plt.show()

#%%
fig, axs = plt.subplots(len(CellId_values), 1, figsize=(15, 20), sharex=True)

for i, CellId in enumerate(CellId_values):
    user_df = filtered_dfs[CellId]
    axs[i].plot(user_df['Time(sec)'], user_df['pathLoss(dB)'], label=f'CellId {CellId}', linestyle='-', markersize=1)
    axs[i].set_title(f'Path Loss UlPathlossTrace {CellId}')
    axs[i].set_ylabel('Path Loss (dB)')
    axs[i].legend()
    axs[i].grid(True)
    # Adjust y-axis to show smaller variations

plt.xlabel('Time (sec)')
plt.tight_layout()
plt.show()

# %%
grouped_df = df.groupby('CellId')['IMSI'].value_counts()
grouped_df
# %%
grouped_df = pd.DataFrame(grouped_df)

# %%
grouped_df 
# %%
df

# %%
