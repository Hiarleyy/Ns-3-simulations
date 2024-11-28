#%%
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
#%%
df = pd.read_csv("DlPdcpStats.txt", delimiter=r'\s+')
df
# %%
df['RNTI'].value_counts()
# %%
df['IMSI'].value_counts()
# %%
def filter_by_IMSI(df, rnti_values):
    return {imsi: df[df['IMSI'] == imsi] for imsi in imsi_values}

imsi_values = range(1,3)  # p/ 2 usuarios
filtered_dfs = filter_by_IMSI(df, imsi_values)

plt.figure(figsize=(10, 6))

for rnti in imsi_values:
    user_df = filtered_dfs[rnti]
    plt.plot(user_df['%'], user_df['delay'], label=str(rnti))

plt.title('delay rate (2 users)')
plt.xlabel('time(s)')
plt.ylabel('delay')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1, fontsize='medium', title='Users', title_fontsize='large')
plt.tight_layout()
plt.show()

# %%
