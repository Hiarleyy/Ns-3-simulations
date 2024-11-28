import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.spatial import distance_matrix

# Coordenadas fixas das antenas
antenas = np.array([
    [50, -50],
])

# Gerar posições iniciais aleatórias para os usuários
np.random.seed(11)
num_users = 4
user_locations = np.random.rand(num_users, 2) * np.array([200, 200]) + np.array([-100, -100])

# Armazenar as posições iniciais
initial_user_locations = user_locations.copy()

# Parâmetros de movimentação
step_size = 0.05  # Tamanho do passo
min_distance = 15  # Distância mínima para a antena
time_per_frame = 0.2  # Intervalo entre frames (segundos)

# Parâmetros para repulsão entre usuários
min_user_distance = 7  # Distância mínima entre usuários
forca_repulsao = 0.05  # Força da repulsão

# Variáveis para rastrear o tempo
frames_to_finish = 0
all_users_reached = False

# Preparação para a animação
fig, ax = plt.subplots(figsize=(10, 6))
scat_users = ax.scatter(user_locations[:, 0], user_locations[:, 1], c='blue', label="Usuários")
scat_antennas = ax.scatter(antenas[:, 0], antenas[:, 1], c='red', marker='x', s=100, label="Antenas (fixas)")

ax.set_xlabel("Latitude")
ax.set_ylabel("Longitude")
ax.set_title("Movimento dos Usuários em Direção às Antenas")
ax.legend()

def update(frame):
    global user_locations, frames_to_finish, all_users_reached

    # Se todos os usuários já chegaram, parar de atualizar
    if all_users_reached:
        return scat_users,

    # Incrementar os frames processados
    frames_to_finish += 1

    # Calcular distâncias para as antenas
    dist_matrix = distance_matrix(user_locations, antenas)
    nearest_antennas = np.argmin(dist_matrix, axis=1)
    distances_to_nearest = dist_matrix[np.arange(len(user_locations)), nearest_antennas]

    # Inicializar vetor de movimento
    movement_vectors = np.zeros_like(user_locations)

    # Movimento em direção às antenas
    for i, antenna_idx in enumerate(nearest_antennas):
        direction_vector = antenas[antenna_idx] - user_locations[i]
        norm = np.linalg.norm(direction_vector)
        if norm > 0:
            normalized_vector = direction_vector / norm
            if distances_to_nearest[i] > min_distance:
                movement_vectors[i] += step_size * normalized_vector * distances_to_nearest[i]

    # Atualizar posições
    user_locations += movement_vectors

    # Verificar se todos os usuários estão dentro da distância mínima
    if np.all(distances_to_nearest <= min_distance):
        all_users_reached = True

    # Atualizar gráfico
    scat_users.set_offsets(user_locations)
    return scat_users,

# Criar a animação
ani = FuncAnimation(fig, update, frames=range(500), interval=200, blit=True)
ani.save("movimento_usuarios.gif", writer="imagemagick")
plt.show()

# Calcular o tempo total
total_time = frames_to_finish * time_per_frame

# Criar o DataFrame com as informações iniciais, finais e de deslocamento
deslocamento = user_locations - initial_user_locations
norma_deslocamento = np.linalg.norm(deslocamento, axis=1)
deslocamento_normalizado = deslocamento / norma_deslocamento[:, np.newaxis]

df = pd.DataFrame({
    'Usuario': np.arange(len(initial_user_locations)),
    'Posicao_Inicial_X': initial_user_locations[:, 0].round(5),
    'Posicao_Inicial_Y': initial_user_locations[:, 1].round(5),
    'Posicao_Final_X': user_locations[:, 0].round(5),
    'Posicao_Final_Y': user_locations[:, 1].round(5),
    'Deslocamento_X': deslocamento[:, 0].round(5),
    'Deslocamento_Y': deslocamento[:, 1].round(5),
    'Deslocamento_Normalizado_X': deslocamento_normalizado[:, 0].round(5),
    'Deslocamento_Normalizado_Y': deslocamento_normalizado[:, 1].round(5),
})

# Salvar em um arquivo CSV
df.to_csv('Posicoes.csv', index=False)

# Imprimir as informações no console
print("Posições Iniciais, Finais, Deslocamento e Deslocamento Normalizado:")
print(df)

# Exibir o tempo total
print(f"\nTempo total para os usuários alcançarem suas posições finais: {total_time:.2f} segundos")
