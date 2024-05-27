
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('DlRlcStats.csv', usecols=['% start', 'RNTI', 'delay'], sep=';')

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

for rnti in rnti_values:
    plt.plot(times[rnti], delays[rnti], label=str(rnti))

plt.title('Delay rate')
plt.xlabel('Tempo(s)')
plt.ylabel('Delay(ms)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1, fontsize='medium', title='Users', title_fontsize='large')
plt.tight_layout()
plt.show()
