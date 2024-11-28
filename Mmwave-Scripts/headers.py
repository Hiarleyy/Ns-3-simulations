#%%
from re import M
import pandas as pd
#%%
CellIdStats = pd.read_csv('CellIdStats.txt', delimiter=r'\s+', header=None)
CellIdStats
#%%
# Rename the columns
CellIdStats.columns = ['Time', 'IMSI', 'CellId', 'RNTI']
CellIdStats
#%%
# Save the DataFrame to a CSV file
CellIdStats.to_csv('CellIdStats.csv', sep=';', index=False)

#------------------------------------------------------------
#%%
MmWaveSinrTime = pd.read_csv('MmWaveSinrTime.txt', delimiter=r'\s+', header=None)
MmWaveSinrTime
# %%
MmWaveSinrTime.columns = ['Time', 'IMSI', 'CellId', "SINR[dB]"]
MmWaveSinrTime

# %%
MmWaveSinrTime.to_csv('MmWaveSinrTime.csv', sep=';', index=False)
#------------------------------------------------------------
#%%
MmWaveSwitchStats= pd.read_csv('MmWaveSwitchStats.txt', delimiter=r'\s+', header=None)
MmWaveSwitchStats
# %%
MmWaveSwitchStats.columns = ['Text','Time', 'IMSI', 'CellId', "RNTI"]
MmWaveSwitchStats

# %%
MmWaveSwitchStats.to_csv('MmWaveSwitchStats.csv', sep=';', index=False)
#------------------------------------------------------------

# %%
