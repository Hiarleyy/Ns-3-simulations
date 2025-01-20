#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%%
df = pd.read_csv("datasets\csv\RxPacketTrace.csv", sep=',')
df

#%%
df['rnti'].value_counts()

#%%
df['Time']
# %%
# Função para filtrar DataFrame por rnti
def filter_by_rnti(df, rnti_values):
    return {rnti: df[df['rnti'] == rnti] for rnti in rnti_values}

rnti_values = range(1,3)  # p/ 2 usuarios
filtered_dfs = filter_by_rnti(df, rnti_values)

plt.figure(figsize=(10, 6))

for rnti in rnti_values:
    user_df = filtered_dfs[rnti]
    plt.plot(user_df['Time'], user_df['SINR(dB)'], label=str(rnti))

plt.title('SINR rate (2 users)')
plt.xlabel('time(s)')
plt.ylabel('SINR(dB)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1, fontsize='medium', title='Users', title_fontsize='large')
plt.tight_layout()
plt.show()
# %%
plt.figure(figsize=(10, 6))

rnti_values = df['rnti'].unique()
for rnti in rnti_values:
    user_df = df[df['rnti'] == rnti]
    plt.plot(user_df['Time'], user_df['CQI'], label=f'RNTI {rnti}')

plt.title('CQI over time')
plt.xlabel('time(s)')
plt.ylabel('CQI')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1)
plt.tight_layout()
plt.show()
# %%
df1_cqi = df.loc[df['cellId'] == 1, 'CQI']
df2_cqi = df.loc[df['cellId'] == 3, 'CQI']

min_cqi_1, max_cqi_1 = df1_cqi.min(), df1_cqi.max()
min_cqi_3, max_cqi_3 = df2_cqi.min(), df2_cqi.max()

labels = ['CellID 1', 'CellID 3']
min_values = [min_cqi_1, min_cqi_3]
max_values = [max_cqi_1, max_cqi_3]

x = np.arange(len(labels))
width = 0.35

plt.figure(figsize=(7, 5))
plt.bar(x - width/2, min_values, width, label='Min CQI',color='red')
plt.bar(x + width/2, max_values, width, label='Max CQI',color='blue')  

plt.xticks(x, labels)
plt.title('Min & Max CQI for each Cell ID')
plt.xlabel('Cell ID')
plt.ylabel('CQI')
plt.legend()
plt.tight_layout()
plt.show()
# %%
