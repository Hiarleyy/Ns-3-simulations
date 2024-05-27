#%%
import pandas as pd
import numpy as np
# %%
df = pd.read_csv('DlRlcStats.csv', sep=';')
type(df)
#%%
devices = df['RNTI']
device1 = devices[devices == 1]
device2 = devices[devices == 2]
device3 = devices[devices == 3]
# %%
devices.value_counts()
# %%
