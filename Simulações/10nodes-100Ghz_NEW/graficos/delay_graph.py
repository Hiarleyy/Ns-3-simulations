#%%
#_____________________Original-data_________________________
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
rnti_values = range(1, 11)
times, delays = filter_and_prepare_data(df, rnti_values)
# Plotando os gráficos
plt.figure(figsize=(10, 6))
plt.plot(times[1], delays[1], label=str(1), color='darkred')
plt.plot(times[2], delays[2], label=str(2), color='aqua')
plt.plot(times[3], delays[3], label=str(3), color='darkorange')
plt.plot(times[4], delays[4], label=str(4), color='fuchsia')
plt.plot(times[5], delays[5], label=str(5), color='red')
plt.plot(times[6], delays[6], label=str(6), color='navy')
plt.plot(times[7], delays[7], label=str(7), color='blue')
plt.plot(times[8], delays[8], label=str(8), color='teal')
plt.plot(times[9], delays[9], label=str(9) , color='black')
plt.plot(times[10], delays[10], label=str(10), color='lime')
plt.title('Delay Original rate')
plt.xlabel('Time(s)')
plt.ylabel('Delay(ms)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1, fontsize='medium', title='Users', title_fontsize='large')
plt.tight_layout()
plt.show()

#%%
#_____________________Optmized-data_________________________
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
plt.plot(times[6], delays[6], label=str(6), color='navy')
plt.plot(times[7], delays[7], label=str(7), color='blue')
plt.plot(times[8], delays[8], label=str(8), color='teal')
plt.plot(times[9], delays[9], label=str(9) , color='black')
plt.plot(times[10], delays[10], label=str(10), color='lime')
plt.title('Delay Opt rate')
plt.xlabel('Time(s)')
plt.ylabel('Delay(ms)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1, fontsize='medium', title='Users', title_fontsize='large')
plt.tight_layout()
plt.show()
