#%%
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
#%%
# Gerando dados simulados para a localização de usuários
n_users =12
np.random.seed(10) ## NAO TIRAR A SEED PELO AMOR DE DEUS
#👆👆👆👆👆👆👆
# Lendo os dados dos usuários a partir de um arquivo CSV
user_positions_df = pd.read_csv('user_positions.csv')
x_users = user_positions_df['POSICAO_X'].values
y_users = user_positions_df['POSICAO_Y'].values
user_locations = np.array(list(zip(x_users, y_users)))

#definindo as posições iniciais das antenas
antenna_positions_before = np.array([[0,4],[0,2]])
# Número de ante    nas (clusters desejados)
n_antennas = 2
# Aplicando k-means para encontrar os clusters
kmeans = KMeans(n_clusters=n_antennas)
kmeans.fit(user_locations)

# Coordenadas dos centros das antenas (clusters)
antenna_positions_after = kmeans.cluster_centers_
labels = kmeans.labels_

print('Posicionamento das antenas antes da otimização:')
for i, pos in enumerate(antenna_positions_before):
    print(f'Antena {i+1}: {pos}')
print('=====================================')
print('Posicionamento otimizado das antenas:')
for i, pos in enumerate(antenna_positions_after):
    print(f'Antena {i+1}: {pos}')
#%%
plt.figure(figsize=(10, 8))
plt.scatter(x_users, y_users, c=labels, cmap='viridis', s=50, label="Usuários")

# Adicionando o título para cada usuário
for i, (x, y) in enumerate(zip(x_users, y_users)):
    plt.text(x, y, f'UE {i+1}', fontsize=9, ha='right')

# Visualizando os resultados
plt.figure(figsize=(10, 8))
# Plotando os usuários
plt.scatter(x_users, y_users, c=labels, cmap='viridis', s=50, label="Usuários")
# Adicionando o título para cada usuário
for i, (x, y) in enumerate(zip(x_users, y_users)):
    plt.text(x, y, f'UE {i+1}', fontsize=9, ha='right')
# Plotando as antenas iniciais
plt.scatter(antenna_positions_before[:, 0], antenna_positions_before[:, 1], edgecolors='black', c='blue', s=200, marker='o', label="Antenas Iniciais")
# Adicionando o título para cada antena inicial
for i, (x, y) in enumerate(antenna_positions_before):
    plt.text(x, y, f'ENB {i+1}', fontsize=9, ha='right')
# Plotando as antenas otimizadas
plt.scatter(antenna_positions_after[:, 0], antenna_positions_after[:, 1], edgecolors='black', c='red', s=200, marker='o', label="Antenas Otimizadas")
# Adicionando o título para cada antena otimizada
for i, (x, y) in enumerate(antenna_positions_after):
    plt.text(x, y, f'ENB {i+1}', fontsize=9, ha='right')

# Plotando vetores das antenas iniciais para as antenas otimizadas
for i in range(len(antenna_positions_before)):
    plt.arrow(antenna_positions_before[i, 0], antenna_positions_before[i, 1],
              antenna_positions_after[i, 0] - antenna_positions_before[i, 0],
              antenna_positions_after[i, 1] - antenna_positions_before[i, 1],
              color='black', linestyle='-', linewidth=0.5, head_width=0.5, head_length=0.7)

# Melhorando o visual
plt.title("Otimização de Antenas com K-Means", fontsize=16)
plt.xlabel("X", fontsize=12)
plt.ylabel("Y", fontsize=12)
plt.legend(fontsize=12)
plt.grid(True)
plt.show()

plt.show()
# %%
