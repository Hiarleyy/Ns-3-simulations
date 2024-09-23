#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

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
    
    return scat, *lines, antenna_scat

# Inputs do usuário
num_vectors = int(input("Digite o número de vetores: "))
min_x = float(input("Digite o valor mínimo para x: "))
max_x = float(input("Digite o valor máximo para x: "))
min_y = float(input("Digite o valor mínimo para y: "))
max_y = float(input("Digite o valor máximo para y: "))
simulation_time = int(input("Digite o tempo de simulação: "))

# Inputs para antenas
num_antennas = int(input("Digite o número de antenas: "))
antenna_positions = []
for i in range(num_antennas):
    antenna_x = float(input(f"Digite a posição x da antena {i+1}: "))
    antenna_y = float(input(f"Digite a posição y da antena {i+1}: "))
    antenna_positions.append((antenna_x, antenna_y))
antenna_positions = np.array(antenna_positions)

# Definir área e gerar velocidades aleatórias
area = (min_x, max_x, min_y, max_y)
velocities = generate_random_velocities(num_vectors, -3, 3, 0.3)

# Gerar coordenadas iniciais
coords = generate_random_coordinates(num_vectors, area)

# Configurar animação
fig, ax = plt.subplots()
scat = ax.scatter(coords[:, 0], coords[:, 1])
antenna_scat = ax.scatter(antenna_positions[:, 0], antenna_positions[:, 1], color='red', marker='x', label='Antenas')
trajectories = [coords.copy()]

# Criar linhas para trajetórias
lines = [ax.plot([], [], alpha=0.5)[0] for _ in range(num_vectors)]

time = 0
ani = animation.FuncAnimation(fig, animate, fargs=(scat, coords, velocities, trajectories, lines, antenna_scat), frames=simulation_time, interval=100, repeat=False)

plt.xlim(min_x, max_x)
plt.ylim(min_y, max_y)
plt.legend()
plt.show()

# Plotar gráfico final com trajetórias dos vetores
fig, ax = plt.subplots()

# Desenhar trajetórias com cores diferentes
colors = plt.cm.jet(np.linspace(0, 1, num_vectors))
for j in range(num_vectors):
    traj = np.array([t[j] for t in trajectories])
    ax.plot(traj[:, 0], traj[:, 1], color=colors[j])

# Mostrar antenas no gráfico final
ax.scatter(antenna_positions[:, 0], antenna_positions[:, 1], color='red', marker='x', label='Antenas')

plt.xlim(min_x, max_x)
plt.ylim(min_y, max_y)
plt.title('Trajetórias dos Vetores')
plt.legend()
plt.show()

# Calcular posições finais
final_coords = update_positions(coords, velocities, simulation_time)

# Criar DataFrame com as informações solicitadas
data = {
    'Nome do Vetor': [f'Vetor {i+1}' for i in range(num_vectors)],
    'Posição Inicial X (m)': coords[:, 0],
    'Posição Inicial Y (m)': coords[:, 1],
    'Velocidade X (m/s)': velocities[:, 0],
    'Velocidade Y (m/s)': velocities[:, 1],
    'Posição Final X (m)': final_coords[:, 0],
    'Posição Final Y (m)': final_coords[:, 1]
}

df = pd.DataFrame(data)

# Arredondar valores para duas casas decimais
df = df.round(2)

print(df)

df.to_csv('simulacao.csv', sep=';' , index=False)
# %%