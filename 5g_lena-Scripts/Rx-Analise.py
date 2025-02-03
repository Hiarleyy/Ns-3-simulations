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
CQI_medio1 = df[df['cellId'] == 1].groupby('rnti')['CQI'].mean().reset_index()
CQI_medio1
#%%
CQI_medio2 = df[df['cellId'] == 3].groupby('rnti')['CQI'].mean().reset_index()
CQI_medio2
#%%
plt.plot(df['Time'], df['CQI']) 
plt.title('CQI over time')
plt.xlabel('time(s)')
plt.ylabel('CQI')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1)
plt.tight_layout()
plt.show()
#%%
df = pd.DataFrame(CQI_medio1)

otimo = df[(df['CQI'] > 20)].shape[0]
bom = df[(df['CQI'] > 15)& (df['CQI'] < 25)].shape[0]

labels = ['BOM(>15)','ÓTIMO(>20)']
sizes = [bom,otimo]
explode = (0.05, 0)  

plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('CQI MEDIO POR RNTI - ENB1')
plt.show()
#%%
df = pd.DataFrame(CQI_medio2)

otimo = df[(df['CQI'] > 20)].shape[0]
bom = df[(df['CQI'] > 15)& (df['CQI'] < 25)].shape[0]
medio = df[(df['CQI'] < 15) & (df['CQI'] > 10)].shape[0]

labels = ['BOM(>15)', 'MÉDIO(15-10)','ÓTIMO(>20)']
sizes = [bom,medio,otimo]
explode = (0.05, 0)  

plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('CQI MÉDIO POR RNTI - ENB2')
plt.show()
# %%
