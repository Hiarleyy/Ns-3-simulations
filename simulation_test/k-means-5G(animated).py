import numpy as np
import matplotlib.pyplot as plt#
from matplotlib.animation import FuncAnimation
from scipy.spatial import distance_matrix

# Coordenadas fixas das antenas
antenas = np.array([
    [-23.5, -46.6],
    [-23.55, -46.65],
    [-23.52, -46.52]
])

# Gerar posições iniciais aleatórias para os usuários
np.random.seed(1)
latitude = np.random.uniform(-23.6, -23.4, 100)
longitude = np.random.uniform(-46.7, -46.5, 100)
user_locations = np.column_stack((latitude, longitude))

# Parâmetros de movimentação
step_size = 0.05  # Tamanho do passo (fração da distância para a antena)
min_distance = 0.01  # Distância mínima para a antena

# Preparação para a animação
fig, ax = plt.subplots(figsize=(10, 6))
scat_users = ax.scatter(user_locations[:, 0], user_locations[:, 1], c='blue', label="Usuários")
scat_antennas = ax.scatter(antenas[:, 0], antenas[:, 1], c='red', marker='x', s=100, label="Antenas (fixas)")
ax.set_xlim(-23.6, -23.4)
ax.set_ylim(-46.7, -46.5)
ax.set_xlabel("Latitude")
ax.set_ylabel("Longitude")
ax.set_title("Movimento dos Usuários em Direção às Antenas")
ax.legend()

# Função de atualização para a animação
def update(frame):
    global user_locations
    
    # Calcular distância de cada usuário para cada antena
    dist_matrix = distance_matrix(user_locations, antenas)
    
    # Encontrar a antena mais próxima de cada usuário
    nearest_antennas = np.argmin(dist_matrix, axis=1)
    distances_to_nearest = dist_matrix[np.arange(len(user_locations)), nearest_antennas]
    
    # Mover cada usuário em direção à antena mais próxima
    for i, antenna_idx in enumerate(nearest_antennas):
        if distances_to_nearest[i] > min_distance:  # Mover apenas se estiver longe da antena
            direction_vector = antenas[antenna_idx] - user_locations[i]
            normalized_vector = direction_vector / np.linalg.norm(direction_vector)
            user_locations[i] += step_size * normalized_vector * distances_to_nearest[i]
        
    
    # Atualizar a posição dos usuários no gráfico
    scat_users.set_offsets(user_locations)
    return scat_users,

# Criar a animação
ani = FuncAnimation(fig, update, frames=range(50), interval=200, blit=True)
ani.save("movimento_usuarios.gif", writer="imagemagick")
plt.show()

# ani.save("movimento_usuarios.mp4", writer="ffmpeg")
