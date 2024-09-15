#%%
# Importações
import numpy as np
import matplotlib.pyplot as plt
#%%
# Definindo constantes
NUM_USERS = 2
DIMENSIONS = 2  # x, y
BAT_POPULATION = 30
MAX_ITER = 1000 #número máximo de iterações

# Função de intensidade de sinal (simplificada)
def signal_intensity(antenna_pos, user_pos):
    distance = np.linalg.norm(antenna_pos - user_pos, axis=1)
    return 1 / (distance ** 2)

# Função de tipo de aplicação (simplificada)
def application_priority(app_type):
    priorities = {'video': 1.0, 'voice': 0.8, 'data': 0.5}
    return priorities.get(app_type, 0.5)

# Função de fitness
def fitness(antenna_pos, user_positions, user_apps):
    intensities = signal_intensity(antenna_pos, user_positions)
    priorities = np.array([application_priority(app) for app in user_apps])
    return np.sum(intensities * priorities)

# Inicialização
def initialize_bats(num_bats, num_users, dimensions, min_dist=300, max_dist=500):
    # Distribuir os usuários de forma mais espaçada
    user_positions = []
    for _ in range(num_bats):
        user_positions.append(np.random.uniform(min_dist, max_dist, (num_users, dimensions)))
    return np.array(user_positions)

# Atualização de posição
def update_position(bats, best_bat, f_min, f_max, antenna_pos, app_priorities, 
                    separation_factor=0.8, lower_bound=0, upper_bound=500):
    beta = np.random.rand()
    freq = f_min + (f_max - f_min) * beta
    v = np.random.rand(*bats.shape) * (bats - best_bat)
    new_positions = bats + v * freq

    # Garantir que as posições estejam dentro dos limites
    new_positions = np.clip(new_positions, lower_bound, upper_bound)


    # Garantir que as novas posições estejam mais afastadas da antena do que as originais
    for i in range(len(new_positions)):
        for j in range(len(new_positions[i])):
            original_distance = np.linalg.norm(antenna_pos - bats[i, j])
            new_distance = np.linalg.norm(antenna_pos - new_positions[i, j])
            if new_distance > original_distance:
                direction = (bats[i, j] - antenna_pos) / np.linalg.norm(bats[i, j] - antenna_pos)
                new_positions[i, j] = bats[i, j] + direction * (original_distance - new_distance) * separation_factor


    # Adicionar uma pequena margem de distância entre os usuários otimizados
    min_user_distance = 50  # Distância mínima entre os usuários otimizados
    for i in range(len(new_positions)):
        for j in range(len(new_positions[i])):
            for k in range(j + 1, len(new_positions[i])):
                distance = np.linalg.norm(new_positions[i, j] - new_positions[i, k])
                if distance < min_user_distance:
                    direction = (new_positions[i, j] - new_positions[i, k]) / distance
                    new_positions[i, j] += direction * (min_user_distance - distance) / 2
                    new_positions[i, k] -= direction * (min_user_distance - distance) / 2



    # Garantir que os usuários otimizados não fiquem em cima da antena
    min_antenna_distance = 50  # Distância mínima entre os usuários otimizados e a antena
    for i in range(len(new_positions)):
        for j in range(len(new_positions[i])):
            distance_to_antenna = np.linalg.norm(new_positions[i, j] - antenna_pos)
            if distance_to_antenna < min_antenna_distance:
                direction = (new_positions[i, j] - antenna_pos) / distance_to_antenna
                new_positions[i, j] = antenna_pos + direction * min_antenna_distance

    return new_positions

# Algoritmo BAT
def bat_algorithm(antenna_pos, user_positions, user_apps, num_bats=BAT_POPULATION, max_iter=MAX_ITER):
    bats = initialize_bats(num_bats, NUM_USERS, DIMENSIONS, min_dist=50, max_dist=450)  # Usuários mais espalhados
    best_bat = bats[0]
    best_fitness = -np.inf

    fitness_history = []

    for _ in range(max_iter):
        new_bats = update_position(bats, best_bat, 0, 2, antenna_pos, user_apps)
        for i in range(num_bats):
            current_fitness = fitness(antenna_pos, new_bats[i], user_apps)
            if current_fitness > best_fitness:
                best_fitness = current_fitness
                best_bat = new_bats[i]
        bats = new_bats
        fitness_history.append(best_fitness)

    return best_bat, fitness_history


# Plotando os resultados
def plot_results(antenna_pos, original_user_pos, new_user_pos):
    plt.figure(figsize=(10, 10))

    # Plot 2D das posições dos usuários
    plt.scatter(*antenna_pos, color='red', label='Antenna', s=100)
    plt.scatter(*original_user_pos.T, color='blue', label='Original Users', s=50)

    # Plotar usuários otimizados em verde
    for i in range(len(new_user_pos)):
        plt.scatter(new_user_pos[i, 0], new_user_pos[i, 1], color='green', label='Optimized Users' if i == 0 else '')

    # Adicionando numeração dos usuários
    for i in range(NUM_USERS):
        plt.text(original_user_pos[i, 0], original_user_pos[i, 1], f'U{i+1}', color='blue', fontsize=12, ha='right')
        plt.text(new_user_pos[i, 0], new_user_pos[i, 1], f'U{i+1}', color='green', fontsize=12, ha='right')

    plt.xlim(0, 500)
    plt.ylim(0, 500)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend(loc='upper left')
    plt.title('User Positions')
    plt.grid(True)
    plt.show()


# Exemplo de uso
antenna_pos = np.array([250, 250])
user_positions = initialize_bats(1, NUM_USERS, DIMENSIONS, min_dist=50, max_dist=450)[0]  # Usuários mais espalhados
user_apps = np.random.choice(['low', 'medium', 'high'], NUM_USERS)

new_user_positions, fitness_history = bat_algorithm(antenna_pos, user_positions, user_apps)
plot_results(antenna_pos, user_positions, new_user_positions)



# Imprimindo as posições
print("Antenna Position:", antenna_pos)
print("Original User Positions:")
for i, (pos, app) in enumerate(zip(user_positions, user_apps)):
    print(f"User {i+1}: Position: {pos}, Application Priority: {app}")
print("Optimized User Positions:")
for i, (pos, app) in enumerate(zip(new_user_positions, user_apps)):
    print(f"User {i+1}: Position: {pos}, Application Priority: {app}")


# Calculando e imprimindo o deslocamento de cada usuário
print("Deslocamento dos usuários otimizados:")
for i in range(NUM_USERS):
    displacement = np.linalg.norm(new_user_positions[i] - user_positions[i])
    print(f"Usuário {i+1}: Deslocamento: {displacement:.2f}")


# Calculando e imprimindo a distância de cada usuário em relação à antena antes e depois da otimização
print("Distância dos usuários em relação à antena:")
for i in range(NUM_USERS):
    distance_before = np.linalg.norm(user_positions[i] - antenna_pos)
    distance_after = np.linalg.norm(new_user_positions[i] - antenna_pos)
    print(f"Usuário {i+1}: Antes: {distance_before:.2f}, Depois: {distance_after:.2f}")

# %%
