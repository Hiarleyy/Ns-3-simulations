#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Função para gerar coordenadas aleatórias
def generate_random_coordinates(num_vectors, area):
    x_coords = np.random.uniform(area[0], area[1], num_vectors)
    y_coords = np.random.uniform(area[2], area[3], num_vectors)
    return np.column_stack((x_coords, y_coords))

# Função para gerar velocidades aleatórias
def generate_random_velocities(num_vectors, min_val, max_val, step):
    velocities = np.random.choice(np.arange(min_val, max_val + step, step), (num_vectors, 2))
    return velocities

# Função para atualizar as posições dos vetores
def update_positions(coords, velocities, time_step):
    new_coords = coords + velocities * time_step
    return new_coords

# Função de animação
def animate(i, scat, coords, velocities, trajectories, lines, antenna_scat):
    global time
    time += 1
    new_coords = update_positions(coords, velocities, time)
    trajectories.append(new_coords.copy())
    scat.set_offsets(new_coords)
    
    # Atualizar trajetórias
    for j, line in enumerate(lines):
        traj = np.array([t[j] for t in trajectories])
        line.set_data(traj[:, 0], traj[:, 1])

# Perguntar ao usuário se ele prefere valores interativos ou estáticos
use_static_params = input("Você prefere usar parâmetros estáticos? (s/n): ").strip().lower() == 's'

if use_static_params:
    # Parâmetros estáticos
    static_params = {
        'antenna1': (0, 0), 
        'antenna2': (0, 80),
        'num_vectors': 5,
        'min_x': -300,
        'max_x': 300,
        'min_y': -300,
        'max_y': 300,
        'simulation_time': 60,
        'UE_1': (-18, -18, -3, -5),
        'UE_2': (2, 6, -4, -3),
        'UE_3': (-6, 44, -3, -3),
        'UE_4': (15, -31, -2, -4),
        'UE_5': (-49, -45, -3, -4),
    }

    # Converter posições das antenas para numpy array
    antenna_positions = np.array([static_params['antenna1'], static_params['antenna2']])

    # Definir área e gerar velocidades aleatórias
    area = (static_params['min_x'], static_params['max_x'], static_params['min_y'], static_params['max_y'])
    
    # Extrair coordenadas e velocidades dos usuários
    coords = np.array([static_params['UE_1'][:2], static_params['UE_2'][:2], static_params['UE_3'][:2], static_params['UE_4'][:2], static_params['UE_5'][:2]])
    velocities = np.array([static_params['UE_1'][2:], static_params['UE_2'][2:], static_params['UE_3'][2:], static_params['UE_4'][2:], static_params['UE_5'][2:]])

    # Configurar animação
    fig, ax = plt.subplots()
    colors = plt.cm.jet(np.linspace(0, 1, static_params['num_vectors']))
    scat = ax.scatter(coords[:, 0], coords[:, 1], c=colors)
    antenna_scat = ax.scatter(antenna_positions[:, 0], antenna_positions[:, 1], color='red', marker='x', label='Antenas')
    trajectories = [coords.copy()]

    # Criar linhas para trajetórias
    lines = [ax.plot([], [], color=colors[j], alpha=0.5)[0] for j in range(static_params['num_vectors'])]

    time = 0
    ani = animation.FuncAnimation(fig, animate, fargs=(scat, coords, velocities, trajectories, lines, antenna_scat), frames=static_params['simulation_time'], interval=100, repeat=False)

    plt.xlim(static_params['min_x'], static_params['max_x'])
    plt.ylim(static_params['min_y'], static_params['max_y'])

    # Adicionar legendas para os vetores
    for i in range(static_params['num_vectors']):
        plt.scatter([], [], color=colors[i], label=f'Vetor {i+1}')
    plt.legend()
    plt.show()

    # Plotar gráfico final com trajetórias dos vetores
    fig, ax = plt.subplots()

    # Desenhar trajetórias com cores diferentes
    for j in range(static_params['num_vectors']):
        traj = np.array([t[j] for t in trajectories])
        ax.plot(traj[:, 0], traj[:, 1], color=colors[j], label=f'Vetor {j+1}')

    # Mostrar antenas no gráfico final
    ax.scatter(antenna_positions[:, 0], antenna_positions[:, 1], color='red', marker='x', label='Antenas')

    plt.xlim(static_params['min_x'], static_params['max_x'])
    plt.ylim(static_params['min_y'], static_params['max_y'])
    plt.title('Trajetórias dos Vetores')
    plt.legend()
    plt.show()

else:
    # Código interativo original
    num_antennas = int(input("Digite o número de antenas: "))
    antenna_positions = []
    for i in range(num_antennas):
        antenna_x = float(input(f"Digite a posição x da antena {i+1}: "))
        antenna_y = float(input(f"Digite a posição y da antena {i+1}: "))
        antenna_positions.append((antenna_x, antenna_y))
    
    num_vectors = int(input("Digite o número de vetores: "))
    min_x = float(input("Digite o valor mínimo de x: "))
    max_x = float(input("Digite o valor máximo de x: "))
    min_y = float(input("Digite o valor mínimo de y: "))
    max_y = float(input("Digite o valor máximo de y: "))
    simulation_time = int(input("Digite o tempo de simulação: "))
    
    velocities = []
    for i in range(num_vectors):
        vel_x = float(input(f"Digite a velocidade em x do vetor {i+1}: "))
        vel_y = float(input(f"Digite a velocidade em y do vetor {i+1}: "))
        velocities.append((vel_x, vel_y))
    
    antenna_positions = np.array(antenna_positions)
    area = (min_x, max_x, min_y, max_y)
    velocities = np.array(velocities)
    coords = generate_random_coordinates(num_vectors, area)

    fig, ax = plt.subplots()
    colors = plt.cm.jet(np.linspace(0, 1, num_vectors))
    scat = ax.scatter(coords[:, 0], coords[:, 1], c=colors)
    antenna_scat = ax.scatter(antenna_positions[:, 0], antenna_positions[:, 1], color='red', marker='x', label='Antenas')
    trajectories = [coords.copy()]

    lines = [ax.plot([], [], color=colors[j], alpha=0.5)[0] for j in range(num_vectors)]

    time = 0
    ani = animation.FuncAnimation(fig, animate, fargs=(scat, coords, velocities, trajectories, lines, antenna_scat), frames=simulation_time, interval=100, repeat=False)

    plt.xlim(min_x, max_x)
    plt.ylim(min_y, max_y)

    # Adicionar legendas para os vetores
    for i in range(num_vectors):
        plt.scatter([], [], color=colors[i], label=f'Vetor {i+1}')
    plt.legend()
    plt.show()

    fig, ax = plt.subplots()
    for j in range(num_vectors):
        traj = np.array([t[j] for t in trajectories])
        ax.plot(traj[:, 0], traj[:, 1], color=colors[j], label=f'Vetor {j+1}')

    ax.scatter(antenna_positions[:, 0], antenna_positions[:, 1], color='red', marker='x', label='Antenas')

    plt.xlim(min_x, max_x)
    plt.ylim(min_y, max_y)
    plt.title('Trajetórias dos Vetores')
    plt.legend()
    plt.show()
# %%
