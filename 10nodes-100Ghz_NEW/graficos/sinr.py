
#%%
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('dataframe\optmized_user_data\RxPacketTrace.txt', sep='\s+')
#%%
df['SINR(dB)'].describe()
#%%
#%%
pd.Series(df['SINR(dB)'].unique()).count() # 10 elementos
#%%
df[df['SINR(dB)'] == 13.008900].value_counts() #contagem dos valores minimos
#%%
df[df['SINR(dB)'] == 37.613400].value_counts() #contagem dos valores máximos
#%%
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
    if rnti in [1,9,10]:
        return 'high'
    elif rnti in [5,7,8]:
        return 'medium'
    elif rnti in [2,3,4,6]:
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
media_10users = df.groupby(['rnti'])['SINR(dB)'].mean() 
#media de SINR(dB) dos 10 users
media_10users 
#%%
df['SINR(dB)'].unique()
# %%
medias_priority = df.groupby(["priority"])[['SINR(dB)']].mean()

# %%
'''df.to_csv('RxPacketTrace_original.csv',sep=';')'''
# %%
'''import pandas as pd
df = pd.read_csv('RxPacketTrace+.csv',sep=';')
df'''

# %%
for rnti in rnti_values:
    user_df = filtered_dfs[rnti]
    plt.plot(user_df['time'], user_df['SINR(dB)'], label=str(rnti))

plt.title('Mean SINR rate (10 users)')
plt.xlabel('time(s)')
plt.ylabel('SINR(dB)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1, fontsize='medium', title='Users', title_fontsize='large')
plt.tight_layout()
plt.show()


# nesse caso a média é igual o valor original
# %%
# grafico para medias em prioridades
medias_priority
# %%
h = [28.669923] * 6
l = [28.958705] * 6
m = [31.398365] * 6
time_list = [ 10, 20 , 30 , 40, 50, 60]
priority_list = [h,l,m]

plt.plot(time_list, h, label='High')
plt.plot(time_list, l, label='Low')
plt.plot(time_list, m, label = 'Medium')
plt.title('Mean SINR priority')
plt.xlabel('time(s)')
plt.ylabel('SINR(dB)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1, fontsize='medium', title='Priority', title_fontsize='large')
plt.tight_layout()
plt.show()

# %%
lows_users= df[df['priority']=='low']
lows_users['SINR(dB)'].mean()
# %%