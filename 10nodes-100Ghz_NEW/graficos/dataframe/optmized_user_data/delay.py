#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('dataframe\optmized_user_data\DlRlcStats.csv', sep=',')
pd.Series(df['delay'].unique()).value_counts().sum()
#%%
df['delay'].describe()
#%%
def filter_and_prepare_data(df2, rnti_values):
    filtered_dfs = {rnti: df2[df2['RNTI'] == rnti] for rnti in rnti_values}
    times = {rnti: filtered_dfs[rnti]['% start'] for rnti in rnti_values}
    delays = {rnti: filtered_dfs[rnti]['delay'] for rnti in rnti_values}
    return times, delays

#%%
# Valores de RNTI de 1 a 10
rnti_values = range(1, 11)
times, delays = filter_and_prepare_data(df, rnti_values)
#%%
# Plotando os gráficos
plt.figure(figsize=(10, 6))

for rnti in rnti_values:
    plt.plot(times[rnti], delays[rnti], label=str(rnti))

plt.title('Delay rate')
plt.xlabel('Tempo(s)')
plt.ylabel('Delay(ms)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1, fontsize='medium', title='Users', title_fontsize='large')
plt.tight_layout()
plt.show()
# %%
## definindo as prioridades

#df = df.drop(columns=['prioridade'])



rnti_values = range(1, 11)
times, delays = filter_and_prepare_data(df2, rnti_values)
def func_prioridade(rnti):
    if rnti in [1,9,10]:
        return 'high'
    elif rnti in [5,7,8]:
        return 'medium'
    elif rnti in [2,3,4,6]:
        return 'low'
    return None # Caso o RNTI não esteja em nenhuma das categorias acima

df['priority'] = df['RNTI'].apply(func_prioridade)
user_low_priority = df[df['priority']=='low']
user_medium_priority = df[df['priority']=='medium']
user_high_priority = df[df['priority']=='high']

media_delay_users = df.groupby(['RNTI'])['delay'].mean() #media de delay dos 10 users 
media_delay_users
# %%
df.groupby(["priority"])[['delay']].mean()
# %%