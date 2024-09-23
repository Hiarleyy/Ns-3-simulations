#%%
import pandas as pd
#%%
df = pd.read_csv('dataframe/optmized_user_data/DlRlcStats.csv')
df
# %%
df['RNTI'].value_counts()
# %%
df.groupby(df['RNTI'])['delay'].mean().sort_values(ascending=False)

# %%
df.groupby(df['RNTI'])['nRxPDUs']
#%%
df.groupby(df['RNTI'])['nRxPDUs'].mean().sort_values(ascending=False)


df.groupby(df['RNTI'])['RxBytes'].mean().sort_values(ascending=False)
#%%
df.groupby(df['RNTI'])['stdDev'].describe()
#%%
#%%
df.groupby(df['RNTI'])['delay'].mean().sort_values(ascending=False)
#%%
df.groupby(df['RNTI'])['nTxPDUs'].unique()
#%%
df.groupby(df['RNTI'])['nTxPDUs'].mean().sort_values(ascending=False)
# %%
df.groupby(df['RNTI'])['PduSize'].unique()
#%%
df.groupby(df['RNTI'])['PduSize'].mean().sort_values(ascending=False)
# %%

# %%
df.groupby(df['RNTI'])['min'].mean().sort_values(ascending=False)
# %%
df.groupby(df['RNTI'])['max'].mean().sort_values(ascending=False)
# %%
df.groupby(df['RNTI'])['nRxPDUs'].value_counts()
# %%
# %%
df.groupby(["RNTI"])[['nRxPDUs', 'delay', 'min', 
                      'max', 'PduSize','nTxPDUs',
                        'RxBytes','stdDev.1']].mean()
#%%

df.groupby(['RNTI'])['LCID'].unique()
df.groupby(['RNTI'])['PduSize'].unique()
# %%

df.groupby(['RNTI'])['stdDev.1'].mean()
# %%
# AMPLITUDE
filtro = df[df['delay']!= 0]
(filtro.groupby(['RNTI'])['delay'].max()) - filtro.groupby(['RNTI'])['delay'].min() 
# %%
filtro.groupby(['RNTI'])['delay'].max()
# %%
filtro.groupby(['RNTI'])['delay'].min()

#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%%
df2 = pd.read_csv('dataframe/optmized_user_data/correlacao-data.csv',
                   sep=',')
df2 = df2.drop(['stdDev.1'],axis=1)
# Gerar a matriz de correlação
#%%
corr_matrix = df2.corr()
corr_matrix
#%%
# Verificar se há valores nulos na matriz de correlação
print(corr_matrix.isnull().sum().sum())

# Criar a figura
plt.figure(figsize=(15, 10))

# Plotar o heatmap com ajustes adicionais
sns.heatmap(corr_matrix,
            annot=True,         # Mostrar os valores na célula
            linewidths=0.5,     # Espessura das linhas
            fmt=".2f",          # Formatação dos valores
            cmap="YlGnBu",      # Mapa de cores
            vmin=-1, vmax=1, 
            annot_kws={"size":10},   
            cbar_kws={"shrink": .75},  # Ajustar o tamanho da barra de cores
            mask=corr_matrix.isnull()) # Máscara para valores nulos

# Ajustar os rótulos para melhor legibilidade
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

# Mostrar o gráfico
plt.show()
# %%