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
def animate(i, scat, coords, velocities, trajectories, lines):
    global time
    time += 1
    new_coords = update_positions(coords, velocities, time)
    trajectories.append(new_coords.copy())
    scat.set_offsets(new_coords)
    
    # Atualizar trajetórias
    for j, line in enumerate(lines):
        traj = np.array([t[j] for t in trajectories])
        line.set_data(traj[:, 0], traj[:, 1])
    
    return scat, *lines

# Inputs do usuário
num_vectors = int(input("Digite o número de vetores: "))
min_x = float(input("Digite o valor mínimo para x: "))
max_x = float(input("Digite o valor máximo para x: "))
min_y = float(input("Digite o valor mínimo para y: "))
max_y = float(input("Digite o valor máximo para y: "))
simulation_time = int(input("Digite o tempo de simulação: "))

# Definir área e gerar velocidades aleatórias
area = (min_x, max_x, min_y, max_y)
velocities = generate_random_velocities(num_vectors, -3, 3, 0.3)

# Gerar coordenadas iniciais
coords = generate_random_coordinates(num_vectors, area)

# Configurar animação
fig, ax = plt.subplots()
scat = ax.scatter(coords[:, 0], coords[:, 1])
trajectories = [coords.copy()]

# Criar linhas para trajetórias
lines = [ax.plot([], [], alpha=0.5)[0] for _ in range(num_vectors)]

time = 0
ani = animation.FuncAnimation(fig, animate, fargs=(scat, coords, velocities, trajectories, lines), frames=simulation_time, interval=100, repeat=False)

plt.xlim(min_x, max_x)
plt.ylim(min_y, max_y)
plt.show()

# Plotar gráfico final com trajetórias dos vetores
fig, ax = plt.subplots()

# Desenhar trajetórias com cores diferentes
colors = plt.cm.jet(np.linspace(0, 1, num_vectors))
for j in range(num_vectors):
    traj = np.array([t[j] for t in trajectories])
    ax.plot(traj[:, 0], traj[:, 1], color=colors[j])

plt.xlim(min_x, max_x)
plt.ylim(min_y, max_y)
plt.title('Trajetórias dos Vetores')
plt.show()

# Calcular posições finais
final_coords = update_positions(coords, velocities, simulation_time)

# Criar DataFrame com as informações solicitadas
data = {
    'Nome do Vetor': [f'Vetor {i+1}' for i in range(num_vectors)],
    'Posição Inicial X': coords[:, 0],
    'Posição Inicial Y': coords[:, 1],
    'Velocidade X': velocities[:, 0],
    'Velocidade Y': velocities[:, 1],
    'Posição Final X': final_coords[:, 0],
    'Posição Final Y': final_coords[:, 1]
}

df = pd.DataFrame(data)

# Arredondar valores para duas casas decimais
df = df.round(2)

df

# %%
