#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#%%
df = pd.read_csv('NrDlPdcpStatsE2E.csv')
df['RNTI'].value_counts()
# %%
