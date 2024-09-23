#%%
import pandas as pd
import numpy as py
#%%
df = pd.read_csv('dataframe\original_user_data\DlRlcStats.csv', sep= ',')
# %%
nTxPDUs = df.groupby(['RNTI'])['nRxPDUs'].unique()
nTxPDUs
# %%
#%%
df2 = pd.read_csv('dataframe\optmized_user_data\DlRlcStats.csv', sep= ',')
# %%
nTxPDUs2 = df2.groupby(['RNTI'])['nRxPDUs'].unique()
nTxPDUs2

# %%
