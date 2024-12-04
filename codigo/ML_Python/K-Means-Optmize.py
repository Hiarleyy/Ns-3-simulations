#%%
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
#%%
# Gerando dados simulados para a localização de usuários
np.random.seed(11)
n_users = 100
x_users = np.random.uniform(0, 100, n_users)  # Coordenada X dos usuários
y_users = np.random.uniform(0, 100, n_users)  # Coordenada Y dos usuários
user_locations = np.array(list(zip(x_users, y_users)))
antenna_positions_before = np.array([[10, 10], [10, 90], [90, 10], [90, 90]])
# Número de antenas (clusters desejados)
n_antennas = 4

# Aplicando k-means para encontrar os clusters
kmeans = KMeans(n_clusters=n_antennas, random_state=42)
kmeans.fit(user_locations)

# Coordenadas dos centros das antenas (clusters)
antenna_positions_after = kmeans.cluster_centers_
labels = kmeans.labels_

#%%
plt.figure(figsize=(10, 8))
plt.scatter(x_users, y_users, c=labels, cmap='viridis', s=50, label="Usuários")
plt.scatter(antenna_positions_before[:, 0], antenna_positions_after[:, 1], c='red', s=200, marker='o', label="Antenas")
plt.title("Disposição de antenas manual", fontsize=16)
plt.xlabel("X", fontsize=12)
plt.ylabel("Y", fontsize=12)
plt.legend(fontsize=12)
plt.grid(True)
plt.show()
# Visualizando os resultados
plt.figure(figsize=(10, 8))
# Plotando os usuários
plt.scatter(x_users, y_users, c=labels, cmap='viridis', s=50, label="Usuários")
# Plotando as antenas
plt.scatter(antenna_positions_after[:, 0], antenna_positions_after[:, 1], c='red', s=200, marker='X', label="Antenas")
# Melhorando o visual
plt.title("Otimização de Antenas com K-Means", fontsize=16)
plt.xlabel("X", fontsize=12)
plt.ylabel("Y", fontsize=12)
plt.legend(fontsize=12)
plt.grid(True)
plt.show()

# %%
