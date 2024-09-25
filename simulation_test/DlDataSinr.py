#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%%
df = pd.read_csv("DlDataSinr.csv", sep=',')
df

#%%
# Agrupar os dados pelo CellId e calcular a média do SINR(dB) para cada tempo
df_grouped = df.groupby(['Time', 'CellId'])['SINR(dB)'].mean().unstack()

# Plotar o comportamento do CellId em função do tempo para a coluna SINR(dB)
df_grouped.plot(figsize=(10, 6))
plt.title('Comportamento do CellId em função do Tempo para SINR(dB)')
plt.xlabel('Tempo')
plt.ylabel('SINR(dB)')
plt.legend(title='CellId')
plt.grid(True)
plt.show()
# %%

df_filtered = df[(df['Time'] >= 0.430) & (df['Time'] <= 0.435)]

df_filtered
# %%
# Identificar as trocas de RNTI para cada CellId
df_shifted = df[['Time', 'CellId', 'RNTI']].shift(1)
df_shifted.columns = ['Time_prev', 'CellId_prev', 'RNTI_prev']
df_combined = pd.concat([df, df_shifted], axis=1)

# Filtrar as linhas onde o RNTI mudou para um CellId específico
df_changes = df_combined[df_combined['RNTI'] != df_combined['RNTI_prev']]

# Plotar as trocas de RNTI para cada CellId
plt.figure(figsize=(10, 6))
for cell_id in df_changes['CellId'].unique():
    df_cell = df_changes[df_changes['CellId'] == cell_id]
    plt.plot(df_cell['Time'], df_cell['RNTI'], marker='o', linestyle='', label=f'CellId {cell_id}')

plt.title('Trocas de RNTI para cada CellId ao longo do Tempo')
plt.xlabel('Tempo')
plt.ylabel('RNTI')
plt.legend(title='CellId')
plt.grid(True)
plt.show()
# %%
