import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('RxPacketTrace.txt', sep='\s+', usecols=['DL/UL', 'time', 'rnti', 'SINR(dB)'])
# Função para filtrar DataFrame por rnti
def filter_by_rnti(df, rnti_values):
    return {rnti: df[df['rnti'] == rnti] for rnti in rnti_values}

# Exemplo de uso
rnti_values = range(1, 11)  # p/ 10 usuaŕios
filtered_dfs = filter_by_rnti(df, rnti_values)
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
