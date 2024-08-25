#%%
import pandas as pd

def process_file(input_file, output_file, column_names):
    # Ler o arquivo
    df = pd.read_csv(input_file, delimiter=r'\s+', header=None)
    # Renomear as colunas
    df.columns = column_names
    # Salvar o DataFrame em um arquivo CSV
    df.to_csv(output_file, sep=';', index=False)
    return df

# Processar os arquivos
CellIdStats = process_file('CellIdStats.txt', 'CellIdStats.csv', ['Time', 'IMSI', 'CellId', 'RNTI'])
MmWaveSinrTime = process_file('MmWaveSinrTime.txt', 'MmWaveSinrTime.csv', ['Time', 'IMSI', 'CellId', "SINR[dB]"])
MmWaveSwitchStats = process_file('MmWaveSwitchStats.txt', 'MmWaveSwitchStats.csv', ['Text', 'Time', 'IMSI', 'CellId', "RNTI"])
X2Stats = process_file('X2Stats.txt','X2Stats.csv', ['Time', 'SourceCellId', 'TargetCellId', 'size', 'delay', 'arrumar'])
# Exibir os DataFrames
print(CellIdStats.head())
print(MmWaveSinrTime.head())
print(MmWaveSwitchStats.head())
print(X2Stats.head())

# %%
