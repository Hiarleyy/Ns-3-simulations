#%%
#______ Gráficos de delay para usuários(Linhas, barras e variação em linha)
#Original-data________________________
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('dataframe/original_user_data/DlRlcStats.csv', sep=',')
# Função para filtrar DataFrame por RNTI e preparar dados para plotagem
def filter_and_prepare_data(df, rnti_values):
    filtered_dfs = {rnti: df[df['RNTI'] == rnti] for rnti in rnti_values}
    times = {rnti: filtered_dfs[rnti]['% start'] for rnti in rnti_values}
    delays = {rnti: np.where(filtered_dfs[rnti]['delay'] == 0, np.nan, filtered_dfs[rnti]['delay']) for rnti in rnti_values}
    return times, delays
# Valores de RNTI de 1 a 10
rnti_values = range(1, 11)
times, delays = filter_and_prepare_data(df, rnti_values)
# Plotando os gráficos
plt.figure(figsize=(10, 6))

plt.plot(times[1], delays[1], label=str(1), color='darkred')
plt.plot(times[2], delays[2], label=str(2), color='aqua')
plt.plot(times[3], delays[3], label=str(3), color='darkorange')
plt.plot(times[4], delays[4], label=str(4), color='fuchsia')
plt.plot(times[5], delays[5], label=str(5), color='red')
plt.plot(times[6], delays[6], label=str(6), color='black')
plt.plot(times[7], delays[7], label=str(7), color='blue')
plt.plot(times[8], delays[8], label=str(8), color='yellow')
plt.plot(times[9], delays[9], label=str(9) , color='gray')
plt.plot(times[10], delays[10], label=str(10), color='lime')
plt.title('Delay Original rate')
plt.xlabel('Time(s)')
plt.ylabel('Delay(ms)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1, fontsize='medium', title='Users', title_fontsize='large')
plt.tight_layout()
plt.show()
#%%
mean_delays = df.groupby(['RNTI'])['delay'].mean()

# Criar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(mean_delays.index, mean_delays.values, color='blue', label='Média de Delay')

# Adicionar a legenda
plt.legend()

# Adicionar título e rótulos dos eixos
plt.title('Média de Delay por RNTI(ORIGINAL)')
plt.xlabel('RNTI')
plt.ylabel('Média de Delay')

# Encontrar as variações de delay
variations = df.groupby(['RNTI'])['delay'].std()
max_variations = variations.nlargest(7)

# Mostrar o gráfico
plt.show()


#%%
# Supondo que o dataframe df já esteja carregado com as colunas 'RNTI' e 'delay'
# Crie o gráfico de barras com cores personalizadas
mean_delay = df.groupby('RNTI')['delay'].mean()
colors = ['darkred', 'aqua', 'darkorange', 'fuchsia', 'red',
          'black', 'blue', 'yellow', 'gray', 'lime'] * (len(mean_delay) // 10 + 1)

plt.figure(figsize=(10, 6))
bars = mean_delay.plot(kind='bar', color=colors[:len(mean_delay)])

# Adicionar rótulos de valores às barras
for bar in bars.patches:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 6), ha='center', va='bottom')

# Adicionar título e rótulos aos eixos
plt.title('Mean Delay Original', fontsize=16)
plt.xlabel('Users(RNTI)', fontsize=14)
plt.ylabel('Delay(ms)', fontsize=12)

# Adicionar linhas de grade
plt.grid(axis='y', linestyle='--', alpha=1)

# Mostrar o gráfico
plt.show()
#%%
#Optmized-data________________________
df = pd.read_csv('dataframe/optmized_user_data/DlRlcStats.csv', sep=',')
def filter_and_prepare_data(df, rnti_values):
    filtered_dfs = {rnti: df[df['RNTI'] == rnti] for rnti in rnti_values}
    times = {rnti: filtered_dfs[rnti]['% start'] for rnti in rnti_values}
    delays = {rnti: np.where(filtered_dfs[rnti]['delay'] == 0, np.nan, filtered_dfs[rnti]['delay']) for rnti in rnti_values}
    return times, delays
# Valores de RNTI de 1 a 10
rnti_values = range(1, 11)
times, delays = filter_and_prepare_data(df, rnti_values)

rnti_values = range(1, 11)
times, delays = filter_and_prepare_data(df, rnti_values)
# Plotando os gráficos
plt.figure(figsize=(10, 6))
plt.plot(times[1], delays[1], label=str(1), color='darkred')
plt.plot(times[2], delays[2], label=str(2), color='aqua')
plt.plot(times[3], delays[3], label=str(3), color='darkorange')
plt.plot(times[4], delays[4], label=str(4), color='fuchsia')
plt.plot(times[5], delays[5], label=str(5), color='red')
plt.plot(times[6], delays[6], label=str(6), color='black')
plt.plot(times[7], delays[7], label=str(7), color='blue')
plt.plot(times[8], delays[8], label=str(8), color='yellow')
plt.plot(times[9], delays[9], label=str(9) , color='gray')
plt.plot(times[10], delays[10], label=str(10), color='lime')
plt.title('Delay Optimized rate')
plt.xlabel('Time(s)')
plt.ylabel('Delay(ms)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1, fontsize='medium', title='Users', title_fontsize='large')
plt.tight_layout()
plt.show()

# %%
mean_delay = df.groupby('RNTI')['delay'].mean()
colors = ['darkred', 'aqua', 'darkorange', 'fuchsia', 'red',
          'black', 'blue', 'yellow', 'gray', 'lime'] * (len(mean_delay) // 10 + 1)

plt.figure(figsize=(10, 6))
bars = mean_delay.plot(kind='bar', color=colors[:len(mean_delay)])

# Adicionar rótulos de valores às barras
for bar in bars.patches:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 6), ha='center', va='bottom')

# Adicionar título e rótulos aos eixos
plt.title('Mean Delay Optimized', fontsize=16)
plt.xlabel('Users(RNTI)', fontsize=14)
plt.ylabel('Delay(ms)', fontsize=12)

# Adicionar linhas de grade
plt.grid(axis='y', linestyle='--', alpha=1)

# Mostrar o gráfico
plt.show()
# %%
# Supondo que df já está definido
# Exemplo de DataFrame
# df = pd.DataFrame({
#     'RNTI': [1, 1, 1, 2, 2, 2, 3, 3, 3],
#     'delay': [10, 20, 15, 10, 30, 25, 5, 15, 10]
# })

# Agrupar por RNTI e calcular a média de delay
mean_delays = df.groupby(['RNTI'])['delay'].mean()

# Criar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(mean_delays.index, mean_delays.values, color='blue', label='Média de Delay')

# Adicionar a legenda
plt.legend()

# Adicionar título e rótulos dos eixos
plt.title('Média de Delay por RNTI(OTIMIZADO)')
plt.xlabel('RNTI')
plt.ylabel('Média de Delay')

# Destacar os pontos com as maiores variações de delay
# Encontrar as variações de delay
variations = df.groupby(['RNTI'])['delay'].std()
max_variations = variations.nlargest(0)

# Adicionar pontos para os maiores variações
plt.scatter(max_variations.index, mean_delays.loc[max_variations.index], color='red', zorder=5)

# Mostrar o gráfico
plt.show()
# %%
