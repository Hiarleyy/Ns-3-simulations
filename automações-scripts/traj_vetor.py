#!/usr/bin/env python3
#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

# Função para atualizar as posições dos vetores
def update_positions(coords, velocities, time_step):
    new_coords = coords + velocities[:, :2] * time_step  # Garantir que velocities tenha a forma correta
    return new_coords

# Função de animação
def animate(i, scat, coords, velocities, trajectories, lines, antenna_scat, highlighted_vectors):
    new_coords = update_positions(coords, velocities, i)  # Use o índice do frame como time_step
    trajectories.append(new_coords.copy())
    scat.set_offsets(new_coords)
    
    # Atualizar trajetórias
    for j, line in enumerate(lines):
        traj = np.array([t[j] for t in trajectories])
        line.set_data(traj[:, 0], traj[:, 1])
        if j in highlighted_vectors:
            line.set_linewidth(2.5)  # Destacar vetor
            line.set_linestyle('--')  # Linha tracejada
        else:
            line.set_linewidth(1.0)
            line.set_linestyle('-')  # Linha contínua

# Função para perguntar sobre vetores a serem destacados
def ask_for_highlighted_vectors(ue_params):
    highlighted_vectors = []
    vector_names = list(ue_params.keys())
    vector_indices = {name: i for i, name in enumerate(vector_names)}
    
    while True:
        highlight = input("Deseja destacar algum vetor? (s/n): ").strip().lower()
        if highlight == 'n':
            break
        elif highlight == 's':
            print("Vetores disponíveis para destaque:")
            for name in vector_names:
                if vector_indices[name] not in highlighted_vectors:
                    print(f"{name}: índice {vector_indices[name] + 1}")
            vector_number = int(input("Digite o número do vetor a ser destacado: ").strip())
            vector_name = f'UE{vector_number}'
            if vector_name in vector_indices and vector_indices[vector_name] not in highlighted_vectors:
                highlighted_vectors.append(vector_indices[vector_name])
                vector_names.remove(vector_name)  # Remover vetor selecionado da lista
            else:
                print("Número do vetor inválido ou já selecionado. Tente novamente.")
        else:
            print("Resposta inválida. Por favor, responda 's' ou 'n'.")
    return highlighted_vectors

# Parâmetros estáticos
static_params = {
    'antenna1': (0, 0), 
    'antenna2': (0, 80),
    'min_x': -300,
    'max_x': 300,
    'min_y': -300,
    'max_y': 300,
    'simulation_time': 60,
}

# Parâmetros dos usuários UE
ue_params = {
    'UE0': (23, -74, -30, -1),
    'UE1': (33, 15, -2, -2),
    'UE2': (-71, 61, -2, -1),
    'UE3': (-30, -21, -1, -2),
    'UE4': (-20, -14, -2, -2),
    'UE5': (11, -72, -1, -1),
    'UE6': (-58, 10, -2, -1),
    'UE7': (67, 15, -1, -2),
    'UE8': (22, -62, -1, -1),
    'UE9': (33, -24, -1, -2),
    'UE10': (-11, 13, -1, -1),
    'UE11': (-56, 57, -2, -2),
    'UE12': (-5, -30, -1, -2),
    'UE13': (11, -60, -2, -1),
    'UE14': (62, 50, -2, -1),
    'UE15': (-15, 45, -2, -1),
    'UE16': (-64, 25, -2, -1),
    'UE17': (-47, 17, -2, -1),
    'UE18': (-18, -15, -2, -1),
    'UE19': (-6, 44, -1, -2),
    'UE20': (-33, 8, -2, -2),
    'UE21': (28, 64, -1, -1),
    'UE22': (34, -1, -2, -2),
    'UE23': (-4, 8, -1, -2),
    'UE24': (-14, -54, -2, -1),
    'UE25': (75, 10, -2, -2),
    'UE26': (-53, -39, -1, -2),
    'UE27': (-43, 12, -2, -2),
    'UE28': (-59, 40, -2, -1),
    'UE29': (25, 9, -2, -1),
}

# Converter posições das antenas para numpy array
antenna_positions = np.array([static_params['antenna1'], static_params['antenna2']])

# Definir área e gerar velocidades aleatórias
area = (static_params['min_x'], static_params['max_x'], static_params['min_y'], static_params['max_y'])

# Extrair coordenadas e velocidades dos usuários
coords = np.array([ue_params[key][:2] for key in ue_params])
velocities = np.array([ue_params[key][2:] for key in ue_params])

# Perguntar sobre vetores a serem destacados
highlighted_vectors = ask_for_highlighted_vectors(ue_params)

# Configurar animação
fig, ax = plt.subplots()
colors = plt.cm.jet(np.linspace(0, 1, len(coords)))  # Ajustar para usar o comprimento de coords
scat = ax.scatter(coords[:, 0], coords[:, 1], c=colors)
antenna_scat = ax.scatter(antenna_positions[:, 0], antenna_positions[:, 1], color='red', marker='x', label='Antenas')
trajectories = [coords.copy()]

# Criar linhas para trajetórias
lines = [ax.plot([], [], color=colors[j], alpha=0.5)[0] for j in range(len(coords))]

ani = animation.FuncAnimation(fig, animate, fargs=(scat, coords, velocities, trajectories, lines, antenna_scat, highlighted_vectors), frames=static_params['simulation_time'], interval=100, repeat=False)

plt.xlim(static_params['min_x'], static_params['max_x'])
plt.ylim(static_params['min_y'], static_params['max_y'])

# Adicionar legendas para os vetores
for i in range(len(coords)):
    plt.scatter([], [], color=colors[i], label=f'Vetor {i+1}')
plt.legend()
plt.show()

# Plotar gráfico final com trajetórias dos vetores
fig, ax = plt.subplots()

# Desenhar trajetórias com cores diferentes
for j in range(len(coords)):
    traj = np.array([t[j] for t in trajectories])
    ax.plot(traj[:, 0], traj[:, 1], color=colors[j], label=f'Vetor {j+1}', linewidth=2.5 if j in highlighted_vectors else 1.0, linestyle='--' if j in highlighted_vectors else '-')

# Mostrar antenas no gráfico final
ax.scatter(antenna_positions[:, 0], antenna_positions[:, 1], color='red', marker='x', label='Antenas')

plt.xlim(static_params['min_x'], static_params['max_x'])
plt.ylim(static_params['min_y'], static_params['max_y'])
plt.title('Trajetórias dos Vetores')
plt.legend()
plt.show()

# Calcular o tempo que os vetores ficam dentro do range de espaço definido
def calculate_time_in_range(coords, velocities, area, simulation_time):
    num_vectors = len(coords)
    time_in_range = [0] * num_vectors
    time_step = 1  # Assumindo que cada frame representa 1 unidade de tempo

    for t in range(simulation_time):
        new_coords = update_positions(coords, velocities, time_step)
        for i, pos in enumerate(new_coords):
            if area[0] <= pos[0] <= area[1] and area[2] <= pos[1] <= area[3]:
                time_in_range[i] += time_step
        coords = new_coords  # Atualizar as coordenadas para o próximo passo de tempo

    return time_in_range

# Calcular o tempo que os vetores ficam dentro do range
time_in_range = calculate_time_in_range(coords.copy(), velocities, area, static_params['simulation_time'])

# Obter as posições finais dos vetores
final_positions = trajectories[-1]

# Criar DataFrame com as informações dos vetores
vector_data = {
    'Nome do Vetor': [f'Vetor {i+1}' for i in range(len(coords))],
    'Posição Inicial': [coords[i].tolist() for i in range(len(coords))],
    'Posição Final': [final_positions[i].tolist() for i in range(len(coords))],
    'Velocidade': [velocities[i].tolist() for i in range(len(coords))],
    'Tempo no Range': time_in_range
}

vector_df = pd.DataFrame(vector_data)

# Criar DataFrame com as informações das antenas
antenna_data = {
    'Nome da Antena': [f'Antenna {i+1}' for i in range(len(antenna_positions))],
    'Posição': [antenna_positions[i].tolist() for i in range(len(antenna_positions))],
    'Velocidade': [[0, 0] for _ in range(len(antenna_positions))]
}

antenna_df = pd.DataFrame(antenna_data)

# Salvar DataFrames em arquivos CSV
vector_df.to_csv('vector_data.csv', index=False)
antenna_df.to_csv('antenna_data.csv', index=False)

# Exibir DataFrames
print("Informações dos Vetores:")
print(vector_df)
print("\nInformações das Antenas:")
print(antenna_df)

# Função para calcular a distância entre dois pontos
def calculate_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Função para plotar gráficos de posições em relação às antenas
def plot_positions_vs_time(trajectories, antenna_positions, num_users_per_plot=5):
    num_users = len(trajectories[0])
    num_plots = (num_users + num_users_per_plot - 1) // num_users_per_plot  # Calcular o número de gráficos necessários

    for plot_idx in range(num_plots):
        fig, ax = plt.subplots()
        start_idx = plot_idx * num_users_per_plot
        end_idx = min(start_idx + num_users_per_plot, num_users)

        for user_idx in range(start_idx, end_idx):
            distances = {antenna_idx: [] for antenna_idx in range(len(antenna_positions))}
            for t in range(len(trajectories)):
                pos = trajectories[t][user_idx]
                for antenna_idx, antenna in enumerate(antenna_positions):
                    distance = calculate_distance(pos, antenna)
                    distances[antenna_idx].append(distance)

            for antenna_idx in distances:
                min_distance = min(distances[antenna_idx])
                max_distance = max(distances[antenna_idx])
                ax.plot(range(len(trajectories)), distances[antenna_idx], label=f'Vetor {user_idx+1} Antena {antenna_idx+1} (Min: {min_distance:.2f}, Max: {max_distance:.2f})')

        ax.set_xlabel('Tempo')
        ax.set_ylabel('Distância')
        ax.set_title(f'Posições em relação às Antenas (Usuários {start_idx+1} a {end_idx})')
        ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize='small')
        plt.tight_layout()
        plt.show()

# Plotar gráficos de posições em relação às antenas
plot_positions_vs_time(trajectories, antenna_positions, num_users_per_plot=5)
# %%
