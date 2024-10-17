import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sklearn.cluster import AgglomerativeClustering
import csv

# Parâmetros da área e antenas
x_min, x_max = -300, 300
y_min, y_max = -300, 300
antena1 = np.array([-200, -200], dtype=np.float64)
antena2 = np.array([200, 200], dtype=np.float64)
antena3 = np.array([0, 0], dtype=np.float64)
antena4 = np.array([-200, 200], dtype=np.float64)

# Gerar posições aleatórias para os usuários
num_usuarios = 10
np.random.seed(0)  # Para reprodutibilidade
posicoes_aleatorias = np.random.uniform(low=[x_min, y_min], high=[x_max, y_max], size=(num_usuarios, 2))

# Dicionário de usuários (posição_x, posição_y)
usuarios = {f'UE{i}': tuple(posicoes_aleatorias[i]) for i in range(num_usuarios)}

# Configuração inicial
tempo_simulacao = 60  # segundos
passo_tempo = 1       # passo de tempo de 1 segundo

# Inicializar posições como arrays de float64
posicoes = {nome: np.array([x, y], dtype=np.float64) for nome, (x, y) in usuarios.items()}

# Calcular distâncias de cada usuário para cada antena
distancias = {nome: [np.linalg.norm(posicoes[nome] - antena1),
                     np.linalg.norm(posicoes[nome] - antena2),
                     np.linalg.norm(posicoes[nome] - antena3),
                     np.linalg.norm(posicoes[nome] - antena4)] for nome in usuarios}

# Atribuir usuários às antenas com base na menor distância
usuarios_antena1 = []
usuarios_antena2 = []
usuarios_antena3 = []
usuarios_antena4 = []

for nome, dists in distancias.items():
    min_dist = min(dists)
    if dists[0] == min_dist:
        usuarios_antena1.append(nome)
    elif dists[1] == min_dist:
        usuarios_antena2.append(nome)
    elif dists[2] == min_dist:
        usuarios_antena3.append(nome)
    else:
        usuarios_antena4.append(nome)

# Garantir distribuição homogênea
todos_usuarios = usuarios_antena1 + usuarios_antena2 + usuarios_antena3 + usuarios_antena4
num_usuarios = len(todos_usuarios)
usuarios_antena1 = todos_usuarios[:num_usuarios//4]
usuarios_antena2 = todos_usuarios[num_usuarios//4:2*num_usuarios//4]
usuarios_antena3 = todos_usuarios[2*num_usuarios//4:3*num_usuarios//4]
usuarios_antena4 = todos_usuarios[3*num_usuarios//4:]

# Calcular velocidades para mover os usuários em direção às antenas atribuídas
velocidades = {}
for nome in usuarios_antena1:
    direcao = antena1 - posicoes[nome]
    velocidades[nome] = direcao / np.linalg.norm(direcao)

for nome in usuarios_antena2:
    direcao = antena2 - posicoes[nome]
    velocidades[nome] = direcao / np.linalg.norm(direcao)

for nome in usuarios_antena3:
    direcao = antena3 - posicoes[nome]
    velocidades[nome] = direcao / np.linalg.norm(direcao)

for nome in usuarios_antena4:
    direcao = antena4 - posicoes[nome]
    velocidades[nome] = direcao / np.linalg.norm(direcao)

# Inicializar CSV
with open('trajectories.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Time', 'User', 'Pos_X', 'Pos_Y', 'Vel_X', 'Vel_Y', 'Dist_Ant1', 'Dist_Ant2', 'Dist_Ant3', 'Dist_Ant4'])

# Função para atualizar a posição dos usuários
def atualizar(frame):
    with open('trajectories.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        for nome in posicoes:
            if np.linalg.norm(posicoes[nome] - antena1) > 1e-2 and nome in usuarios_antena1:
                posicoes[nome] += velocidades[nome] * passo_tempo
            elif np.linalg.norm(posicoes[nome] - antena2) > 1e-2 and nome in usuarios_antena2:
                posicoes[nome] += velocidades[nome] * passo_tempo
            elif np.linalg.norm(posicoes[nome] - antena3) > 1e-2 and nome in usuarios_antena3:
                posicoes[nome] += velocidades[nome] * passo_tempo
            elif np.linalg.norm(posicoes[nome] - antena4) > 1e-2 and nome in usuarios_antena4:
                posicoes[nome] += velocidades[nome] * passo_tempo

            dist_ant1 = np.linalg.norm(posicoes[nome] - antena1)
            dist_ant2 = np.linalg.norm(posicoes[nome] - antena2)
            dist_ant3 = np.linalg.norm(posicoes[nome] - antena3)
            dist_ant4 = np.linalg.norm(posicoes[nome] - antena4)
            writer.writerow([frame, nome, posicoes[nome][0], posicoes[nome][1], velocidades[nome][0], velocidades[nome][1], dist_ant1, dist_ant2, dist_ant3, dist_ant4])

            pontos[nome].set_data(posicoes[nome][0], posicoes[nome][1])
            if nome in usuarios_antena1:
                linhas[nome].set_data([antena1[0], posicoes[nome][0]], [antena1[1], posicoes[nome][1]])
            elif nome in usuarios_antena2:
                linhas[nome].set_data([antena2[0], posicoes[nome][0]], [antena2[1], posicoes[nome][1]])
            elif nome in usuarios_antena3:
                linhas[nome].set_data([antena3[0], posicoes[nome][0]], [antena3[1], posicoes[nome][1]])
            else:
                linhas[nome].set_data([antena4[0], posicoes[nome][0]], [antena4[1], posicoes[nome][1]])
    return list(linhas.values()) + list(pontos.values())

# Função de inicialização
def init():
    for linha in linhas.values():
        linha.set_data([], [])
    for ponto in pontos.values():
        ponto.set_data([], [])
    return list(linhas.values()) + list(pontos.values())

# Configuração da figura e dos eixos
fig, ax = plt.subplots()
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.plot(antena1[0], antena1[1], 'ro', label='Antena 1')  # Antena 1
ax.plot(antena2[0], antena2[1], 'ro', label='Antena 2')  # Antena 2
ax.plot(antena3[0], antena3[1], 'ro', label='Antena 3')  # Antena 3
ax.plot(antena4[0], antena4[1], 'ro', label='Antena 4')  # Antena 4

# Inicializar linhas e pontos
linhas = {nome: ax.plot([], [], 'b-')[0] for nome in usuarios}
pontos = {nome: ax.plot([], [], 'bo')[0] for nome in usuarios}
labels = {nome: ax.text(posicoes[nome][0], posicoes[nome][1], nome, fontsize=9, ha='right') for nome in usuarios}

# Adicionar grid
ax.grid(True)

# Criando a animação
anim = FuncAnimation(fig, atualizar, frames=np.arange(0, tempo_simulacao, passo_tempo),
                     init_func=init, blit=True, repeat=False)

plt.title("Movimento dos Usuários em Direção às Antenas")
plt.xlabel("Posição X")
plt.ylabel("Posição Y")

# Exibindo a animação
plt.show()

# Gráfico de dispersão dos clusters
fig, ax = plt.subplots()
cores = ['blue' if nome in usuarios_antena1 else 'green' if nome in usuarios_antena2 else 'purple' if nome in usuarios_antena3 else 'orange' for nome in usuarios]
dados = np.array(list(posicoes.values()))
ax.scatter(dados[:, 0], dados[:, 1], c=cores, marker='o', label='Usuários')
ax.plot(antena1[0], antena1[1], 'ro', label='Antena 1')
ax.plot(antena2[0], antena2[1], 'ro', label='Antena 2')
ax.plot(antena3[0], antena3[1], 'ro', label='Antena 3')
ax.plot(antena4[0], antena4[1], 'ro', label='Antena 4')

# Adicionar rótulos de usuários
for nome in usuarios:
    ax.text(posicoes[nome][0], posicoes[nome][1], nome, fontsize=9, ha='right')

# Adicionar grid
ax.grid(True)

ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
plt.title("Distribuição dos Usuários")
plt.xlabel("Posição X")
plt.ylabel("Posição Y")
plt.legend()
plt.show()

#%%
import pandas as pd

df = pd.read_csv('trajectories.csv')

df

#%%

df = df.round(2)
Init_sim = df[df['Time']==0]
Init_sim[['User','Dist_Ant1','Dist_Ant2','Dist_Ant3','Dist_Ant4']]

#%%

grouped = df.groupby('User')[['Dist_Ant1', 'Dist_Ant2', 'Dist_Ant3', 'Dist_Ant4']].min()
# %%
