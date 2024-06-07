#%%
#_+ coluna'priority' e gráficos de barras no final
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('dataframe\original_user_data\Original_RxPacketTrace.txt', sep='\s+')
df
#%%
df['SINR(dB)'].unique()
#%%
# Função para filtrar DataFrame por rnti
def filter_by_rnti(df, rnti_values):
    return {rnti: df[df['rnti'] == rnti] for rnti in rnti_values}
#%%
# Exemplo de uso
rnti_values = range(1, 11)  # p/ 10 usuaŕios
filtered_dfs = filter_by_rnti(df, rnti_values)
#%%
def filter_and_prepare_data(df, rnti_values):
    filtered_dfs = {rnti: df[df['rnti'] == rnti] for rnti in rnti_values}
    times = {rnti: filtered_dfs[rnti]['time'] for rnti in rnti_values}
    sinr = {rnti: filtered_dfs[rnti]['SINR(dB)']
    for rnti in rnti_values}
    #sinr = {rnti: np.where(filtered_dfs[rnti]['SINR(dB)'] == 0, np.nan, 
    return times, sinr
# Valores de RNTI de 1 a 10
rnti_values = range(1, 11)
times, sinr = filter_and_prepare_data(df, rnti_values)

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
for rnti in rnti_values:
    user_df = filtered_dfs[rnti]
    plt.plot(user_df['time'], user_df['SINR(dB)'], label=str(rnti))

# %%
# grafico para medias em prioridades
medias_priority
#%%
df2 = pd.read_csv('dataframe\optmized_user_data\Optmized_RxPacketTrace.txt', sep='\s+')

def func_prioridade(rnti):
    if rnti in [1,9,10]:
        return 'high'
    elif rnti in [5,7,8]:
        return 'medium'
    elif rnti in [2,3,4,6]:
        return 'low'
    return None  # Caso o RNTI não esteja em nenhuma das categorias acima

df2['priority'] = df2['rnti'].apply(func_prioridade)

df[df['SINR(dB)']>0]
# %%
lows_users= df[df['priority']=='low']
lows_users['SINR(dB)'].mean()
# %%
df1 =df
mean_sinr1 = df1.groupby('priority')['SINR(dB)'].mean()
mean_sinr2 = df2.groupby('priority')['SINR(dB)'].mean()

# Definir as cores
colors1 = ['red'] * len(mean_sinr1)
colors2 = ['blue'] * len(mean_sinr2)

# Ajustar a largura das barras para que sejam mais finas
width = 0.35

# Plotar os dados
fig, ax = plt.subplots(figsize=(12, 6))

# Ajustar as posições das barras para evitar que toquem as bordas
ind = range(len(mean_sinr1))  # índice para as barras

# Plotar os dados do primeiro dataframe
bars1 = ax.bar([x - width/2 for x in ind], mean_sinr1, width=width, color=colors1[:len(mean_sinr1)], label='Original')

# Plotar os dados do segundo dataframe
bars2 = ax.bar([x + width/2 for x in ind], mean_sinr2, width=width, color=colors2[:len(mean_sinr2)], label='Optimized')

# Adicionar rótulos de valores às barras do primeiro dataframe
for bar in bars1:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 6), ha='center', va='bottom', fontsize=10)

# Adicionar rótulos de valores às barras do segundo dataframe
for bar in bars2:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 6), ha='center', va='bottom', fontsize=10)

# Configurações adicionais do gráfico
plt.xlabel('Priority', fontsize=14)
plt.ylabel('Sinr(dB)', fontsize=12)
plt.title('Mean Sinr Comparison', fontsize=16)
plt.ylim(0, max(max(mean_sinr1), max(mean_sinr2)) * 1.1)
plt.legend()

# Adicionar linhas de grade
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Colocar os nomes no eixo X na horizontal e centralizar
ax.set_xticks(ind)
ax.set_xticklabels(mean_sinr1.index, rotation=0, ha='center')

# Adicionar espaçamento nas bordas
plt.xlim(-0.5, len(mean_sinr1) - 0.5)

# Exibir o gráfico
plt.show()
# %%

mean_sinr = df1.groupby('rnti')['SINR(dB)'].mean()
colors = ['darkred', 'aqua', 'darkorange', 'fuchsia', 'red',
          'black', 'blue', 'yellow', 'gray', 'lime'] * (len(mean_sinr) // 10 + 1)

plt.figure(figsize=(10, 6))
bars = mean_sinr.plot(kind='bar', color=colors[:len(mean_sinr)])

# Adicionar rótulos de valores às barras
for bar in bars.patches:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 6), ha='center', va='bottom')

# Adicionar título e rótulos aos eixos
plt.title('Mean SINR Original', fontsize=16)
plt.xlabel('Users(RNTI)', fontsize=14)
plt.ylabel('SINR(dB)', fontsize=12)

# Adicionar linhas de grade
plt.grid(axis='y', linestyle='--', alpha=1)

# Mostrar o gráfico
plt.show()
# %%
mean_sinr = df2.groupby('rnti')['SINR(dB)'].mean()
colors = ['darkred', 'aqua', 'darkorange', 'fuchsia', 'red',
          'black', 'blue', 'yellow', 'gray', 'lime'] * (len(mean_sinr) // 10 + 1)

plt.figure(figsize=(10, 6))
bars = mean_sinr.plot(kind='bar', color=colors[:len(mean_sinr)])

# Adicionar rótulos de valores às barras
for bar in bars.patches:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 6), ha='center', va='bottom')

# Adicionar título e rótulos aos eixos
plt.title('Mean SINR Optimized', fontsize=16)
plt.xlabel('Users(RNTI)', fontsize=14)
plt.ylabel('SINR(dB)', fontsize=12)

# Adicionar linhas de grade
plt.grid(axis='y', linestyle='--', alpha=1)

# Mostrar o gráfico
plt.show()

# %%
