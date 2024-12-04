#%%
import pandas as pd 
import matplotlib.pyplot as plt

#%%
df = pd.read_csv('datasets/DlPathlossTrace.txt', sep='\t')
print(df.columns)  # Print the columns to verify the names
df # Count the number of occurrences of each value in the 'IMSI' column

# %%
# Função para filtrar DataFrame por rnti
def filter_by_rnti(df, imsi_values):
    return {imsi: df[df['IMSI'] == imsi] for imsi in imsi_values}

imsi_values = range(1,4)  # p/ 2 usuarios
filtered_dfs = filter_by_rnti(df, imsi_values)


#%%
plt.figure(figsize=(12, 8))

colors = ['b', 'g', 'r']  # Define colors for each user
markers = ['o', 's', 'D']  # Define markers for each user

for i, imsi in enumerate(imsi_values):
    user_df = filtered_dfs[imsi]
    plt.plot(user_df['Time(sec)'], user_df['pathLoss(dB)'], label=f'imsi {imsi}', color=colors[i], marker=markers[i], linestyle='-', markersize=1)

plt.title('Path Loss DlPathlossTrace')
plt.xlabel('Time (sec)')
plt.ylabel('Path Loss (dB)')
plt.legend(title='Users')
plt.grid(True)
plt.show()


#%%
fig, axs = plt.subplots(len(imsi_values), 1, figsize=(12, 8), sharex=True)

colors = ['b', 'g', 'r']  # Define colors for each user
markers = ['o', 's', 'D']  # Define markers for each user

for i, imsi in enumerate(imsi_values):
    user_df = filtered_dfs[imsi]
    axs[i].plot(user_df['Time(sec)'], user_df['pathLoss(dB)'], label=f'imsi {imsi}', color=colors[i], marker=markers[i], linestyle='-', markersize=1)
    axs[i].set_title(f'Path Loss DlPathlossTrace {imsi}')
    axs[i].set_ylabel('Path Loss (dB)')
    axs[i].legend()
    axs[i].grid(True)
    # Adjust y-axis to show smaller variations
    axs[i].set_ylim(user_df['pathLoss(dB)'].min() - 0.5, user_df['pathLoss(dB)'].max() + 0.5)

axs[-1].set_xlabel('Time (sec)')

plt.tight_layout()
plt.show()

# %%
grouped_df = df.groupby('IMSI')['pathLoss(dB)'].describe()
grouped_df
# %%
fig, axs = plt.subplots(len(imsi_values), 1, figsize=(12, 8), sharex=True)

colors = ['b', 'g', 'r']  # Define colors for each user
markers = ['o', 's', 'D']  # Define markers for each user

for i, imsi in enumerate(imsi_values):
    user_df = filtered_dfs[imsi]
    axs[i].plot(user_df['Time(sec)'], user_df['pathLoss(dB)'], label=f'imsi {imsi}', color=colors[i], marker=markers[i], linestyle='-', markersize=1)
    axs[i].set_title(f'Path Loss DlPathlossTrace {imsi}')
    axs[i].set_ylabel('Path Loss (dB)')
    axs[i].legend()
    axs[i].grid(True)
    # Adjust y-axis to show smaller variations
    axs[i].set_ylim(user_df['pathLoss(dB)'].min() - 0.5, user_df['pathLoss(dB)'].max() + 0.5)

axs[-1].set_xlabel('Time (sec)')

plt.tight_layout()
plt.show()

# %%
df_grouped = df.groupby('IMSI')['pathLoss(dB)'].describe()

df_grouped
# %%
