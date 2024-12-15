
#%%
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import matplotlib.pyplot as plt
#%%
df = pd.read_csv('tratamento/files/csv/RxedGnbPhyCtrlMsgsTrace.csv')
df
# %%
df['nodeId'].unique()
# %%
df['Slot'].unique()
# %%
df['bwpId'].unique()
# %%

# %%
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(df['Time'], df['nodeId'], df['bwpId'], c=df['bwpId'], cmap='viridis', marker='o')
fig.colorbar(scatter, ax=ax, label='bwpId')

ax.set_xlabel('Time')
ax.set_ylabel('nodeId')
ax.set_zlabel('bwpId')

ax.set_title('3D Scatter Plot of Time, nodeId, and bwpId')
ax.view_init(elev=20., azim=120)  # Adjust the elevation and angle for better visualization

# Ensure all nodeId values are displayed
ax.set_yticks(df['nodeId'].unique())

plt.show()
# %%
df['nodeId'].value_counts()

#%%
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Time', hue='bwpId', multiple='stack', palette='viridis', bins=50)

plt.xlabel('Time')
plt.ylabel('Count')
plt.title('Variation of nodeId with bwpId over Time')
plt.legend(title='bwpId')
plt.show()