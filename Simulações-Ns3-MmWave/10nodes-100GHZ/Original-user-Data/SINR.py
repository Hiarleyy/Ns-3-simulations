
#%%
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('RxPacketTrace.txt', sep='\s+')
df
# Função para filtrar DataFrame por rnti
def filter_by_rnti(df, rnti_values):
    return {rnti: df[df['rnti'] == rnti] for rnti in rnti_values}
#%%
# Exemplo de uso
rnti_values = range(1, 11)  # p/ 10 usuaŕios
filtered_dfs = filter_by_rnti(df, rnti_values)
#%%
# Plotando os gráficos
plt.figure(figsize=(10, 6))

for rnti in rnti_values:
    user_df = filtered_dfs[rnti]
    plt.plot(user_df['time'], user_df['SINR(dB)'], label=str(rnti))

plt.title('SINR rate (10 users)')
plt.xlabel('time(s)')
plt.ylabel('SINR(dB)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1, fontsize='medium', title='Users', title_fontsize='large')
plt.tight_layout()
plt.show()
# %%

def func_prioridade(rnti):
    if rnti in [1, 4, 5]:
        return 'high'
    elif rnti in [3, 7]:
        return 'medium'
    elif rnti in [2, 6, 8, 9, 10]:
        return 'low'
    return None  # Caso o RNTI não esteja em nenhuma das categorias acima

df['priority'] = df['rnti'].apply(func_prioridade)

df
# %%
## Media dos user baixa prioridade
user_low_priority = df[df['priority']=='low']
user_medium_priority = df[df['priority']=='medium']
user_high_priority = df[df['priority']=='high']
# %%
df.groupby(['rnti'])['SINR(dB)'].mean() #media de SINR(dB) dos 10 users 
#%%
df['SINR(dB)'].unique()
# %%
df.groupby(["priority"])[['SINR(dB)']].mean()

# %%
df.to_csv('RxPacketTrace_original.csv',sep=';')
# %%
import pandas as pd
df = pd.read_csv('RxPacketTrace+.csv',sep=';')
df
# %%
