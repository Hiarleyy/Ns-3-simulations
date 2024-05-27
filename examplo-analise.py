#%%
import pandas as pd
# %%
df = pd.read_csv('DlRlcStats.csv',usecols=['% start', 'RNTI', 'delay'	] , sep=';')
type(df)
#%%
df['RNTI'].value_counts()
#%%
df1 = df[df['RNTI'] == 1]
df2 = df[df['RNTI'] ==2]
df3 = df[df['RNTI']==3]
# %%

# %%
