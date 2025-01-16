#%%
import pandas as pd
import matplotlib.pyplot as plt
#%%
df_first = pd.read_csv('10UE2ENB(2S)/First/DlCtrlSinr.txt', sep='\s+')
df_first
#%%
df_last = pd.read_csv('10UE2ENB(2S)/Last/DlCtrlSinr.txt', sep='\s+')
df_last
# %%
cellID_value = 4  # Defina o cellID a ser filtrado

df_first_filtered = df_first[df_first['CellId'] == cellID_value]
df_last_filtered = df_last[df_last['CellId'] == cellID_value]

# Obter os valores mínimo e máximo
min_first = df_first_filtered['SINR(dB)'].min()
max_first = df_first_filtered['SINR(dB)'].max()
min_last = df_last_filtered['SINR(dB)'].min()
max_last = df_last_filtered['SINR(dB)'].max()

# Criar DataFrame para plot
df_plot = pd.DataFrame({
    'Tabela': ['First', 'First', 'Last', 'Last'],
    'Estatística': ['Min', 'Max', 'Min', 'Max'],
    'SINR(dB)': [min_first, max_first, min_last, max_last]
})

# Plot do gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(df_plot['Tabela'] + '_' + df_plot['Estatística'], df_plot['SINR(dB)'], alpha=0.7)
plt.xlabel('Tabela_Estatística')
plt.ylabel('SINR(dB)')
plt.title(f'Comparação de Min e Max de SINR_CTRL filtrado por cellID = {cellID_value}')
plt.grid(True)
plt.show()

# %%
df_first = pd.read_csv('10UE2ENB(2S)/First/DlDataSinr.txt', sep='\s+')
df_first
#%%
df_last = pd.read_csv('10UE2ENB(2S)/Last/DlDataSinr.txt', sep='\s+')
df_last
#%%
cellID_value = 2  # Defina o cellID a ser filtrado

df_first_filtered = df_first[df_first['CellId'] == cellID_value]
df_last_filtered = df_last[df_last['CellId'] == cellID_value]

# Obter os valores mínimo e máximo
min_first = df_first_filtered['SINR(dB)'].min()
max_first = df_first_filtered['SINR(dB)'].max()
min_last = df_last_filtered['SINR(dB)'].min()
max_last = df_last_filtered['SINR(dB)'].max()

# Criar DataFrame para plot
df_plot = pd.DataFrame({
    'Tabela': ['First', 'First', 'Last', 'Last'],
    'Estatística': ['Min', 'Max', 'Min', 'Max'],
    'SINR(dB)': [min_first, max_first, min_last, max_last]
})

# Plot do gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(df_plot['Tabela'] + '_' + df_plot['Estatística'], df_plot['SINR(dB)'], alpha=0.7)
plt.xlabel('Tabela_Estatística')
plt.ylabel('SINR(dB)')
plt.title(f'Comparação de Min e Max de SINR_CTRL filtrado por cellID = {cellID_value}')
plt.grid(True)
plt.show()

# %%
df_first = pd.read_csv('10UE2ENB(2S)/First/DlPathLossTrace.txt', sep='\s+')
df_first
#%%
df_last = pd.read_csv('10UE2ENB(2S)/Last/DlPathLossTrace.txt', sep='\s+')
df_last
#%%
cellID_value = 6  # Defina o cellID a ser filtrado

df_first_filtered = df_first[df_first['CellId'] == cellID_value]
df_last_filtered = df_last[df_last['CellId'] == cellID_value]

# Obter os valores mínimo e máximo
min_first = df_first_filtered['pathLoss(dB)'].min()
max_first = df_first_filtered['pathLoss(dB)'].max()
min_last = df_last_filtered['pathLoss(dB)'].min()
max_last = df_last_filtered['pathLoss(dB)'].max()

# Criar DataFrame para plot
df_plot = pd.DataFrame({
    'Tabela': ['First', 'First', 'Last', 'Last'],
    'Estatística': ['Min', 'Max', 'Min', 'Max'],
    'pathLoss(dB)': [min_first, max_first, min_last, max_last]
})
# %%
plt.figure(figsize=(10, 6))
plt.bar(df_plot['Tabela'] + '_' + df_plot['Estatística'], df_plot['pathLoss(dB)'], alpha=0.7)
plt.xlabel('Tabela_Estatística')
plt.ylabel('SINR(dB)')
plt.title(f'Comparação de Min e Max de SINR_CTRL filtrado por cellID = {cellID_value}')
plt.grid(True)
plt.show()
# %%
