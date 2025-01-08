#%%
import random

import matplotlib.pyplot as plt

# Configurações do grid
grid_size = 200
num_users = 20
users_per_quadrant = 5
quadrant_distance = 100  # Ajuste a distância entre os quadrantes
user_distance = 10

# Função para gerar posições dos usuários
def generate_positions():
    positions = []
    for i in range(4):  # 4 quadrantes
        base_x = (i % 2) * quadrant_distance + (grid_size - quadrant_distance) / 2
        base_y = (i // 2) * quadrant_distance + (grid_size - quadrant_distance) / 2
        for j in range(users_per_quadrant):
            x = base_x + random.uniform(-user_distance, user_distance)
            y = base_y + random.uniform(-user_distance, user_distance)
            positions.append((x, y))
    return positions

# Gerar posições
positions = generate_positions()

# Plotar o grid
plt.figure(figsize=(8, 8))
for pos in positions:
    plt.scatter(pos[0], pos[1], c='blue')
    plt.text(pos[0], pos[1], f'({pos[0]:.2f}, {pos[1]:.2f})', fontsize=9)

plt.xlim(-10, grid_size + 10)
plt.ylim(-10, grid_size + 10)
plt.grid(True)
plt.title('Grid de Coordenadas Cartesianas')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# Imprimir posições
for idx, pos in enumerate(positions):
    print(f'Usuário {idx + 1}: x={pos[0]:.2f}, y={pos[1]:.2f}')
# %%
