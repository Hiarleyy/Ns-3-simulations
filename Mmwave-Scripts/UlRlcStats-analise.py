#%%
import pandas as pd
import matplotlib.pyplot as plt
#%%
df = pd.read_csv("UlRlcStats.txt", delimiter=r'\s+')
df

#%%
user_color = {1:'darkred',
                2:'aqua',
                3:'darkorange',
                4:'fuchsia',
                5:'red',
                6:'black',
                7:'blue',
                8:'yellow',
                9:'gray',
                10:'lime'}

grouped_df = df.groupby('IMSI')[["LCID", 
"nTxPDUs", "TxBytes", "nRxPDUs", 
"RxBytes"]].agg(['mean', 'max', 'min'])
grouped_df
# %%
# Plotting the data
grouped_df.plot(kind='bar', y=[("nTxPDUs", "mean"), 
("nTxPDUs", "max"), ("nTxPDUs", "min"), ("TxBytes", "mean"), 
("TxBytes", "max"), ("TxBytes", "min"), ("nRxPDUs", "mean"), 
("nRxPDUs", "max"), ("nRxPDUs", "min"), ("RxBytes", "mean"), 
("RxBytes", "max"), ("RxBytes", "min")], color=['darkred', 'aqua', 'darkorange', 'fuchsia', 'red', 'black', 'blue', 'yellow', 'gray', 'lime'])
plt.xlabel('IMSI')
plt.ylabel('Value')
plt.title('Parameters per IMSI')
plt.legend(["nTxPDUs (mean)", "nTxPDUs (max)", "nTxPDUs (min)", "TxBytes (mean)", 
"TxBytes (max)", "TxBytes (min)", "nRxPDUs (mean)", "nRxPDUs (max)", "nRxPDUs (min)"], bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()

# %%
