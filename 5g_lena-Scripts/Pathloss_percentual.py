#%%
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'IMSI': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Change (%)': [-1.96, 9.01, -7.29, 8.03, 7.77, 3.92, 9.40, -3.43, 10.41, 4.03]
}

df = pd.DataFrame(data)
positive_change = df[df['Change (%)'] > 0].shape[0]
non_positive_change = df[df['Change (%)'] <= 0].shape[0]

labels = ['Change% > 0', 'Change% ≤ 0']
sizes = [positive_change, non_positive_change]
colors = ['#002041', '#e76f51']
explode = (0.05, 0)  

plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', startangle=90)
plt.title('Percentual de Mudanças por IMSI')
plt.show()

# %%
