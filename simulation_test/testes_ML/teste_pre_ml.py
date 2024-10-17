import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parâmetros da área e antenas
x_min, x_max = -300, 300
y_min, y_max = -300, 300
antena1 = np.array([200, -200], dtype=np.float64)
antena2 = np.array([200, 200], dtype=np.float64)

# Dicionário de usuários (posição_x, posição_y, velocidade_x, velocidade_y)
usuarios = {
    'UE0': (23, -74),
    'UE1': (33, 15),
    'UE2': (-71, 61),
    'UE3': (-30, -21),
    'UE4': (-20, -14),
    'UE5': (11, -72),
    'UE6': (-58, 10),
    'UE7': (67, 15),
    'UE8': (22, -62),
    'UE9': (33, -24),
    'UE10': (-11, 13),
}

# Configuração inicial
tempo_simulacao = 60  # segundos
passo_tempo = 0.1      # passo de tempo de 1 segundo

# Inicializar posições como arrays de float64
posicoes = {nome: np.array([x, y], dtype=np.float64) for nome, (x, y) in usuarios.items()}

# Calcular distâncias para as antenas
distancias_antena1 = {nome: np.linalg.norm(pos - antena1) for nome, pos in posicoes.items()}
distancias_antena2 = {nome: np.linalg.norm(pos - antena2) for nome, pos in posicoes.items()}

# Ordenar usuários por distância relativa às antenas
usuarios_ordenados = sorted(usuarios.keys(), key=lambda nome: distancias_antena1[nome] - distancias_antena2[nome])

# Dividir usuários igualmente entre as antenas
usuarios_antena1 = usuarios_ordenados[:len(usuarios_ordenados) // 2]
usuarios_antena2 = usuarios_ordenados[len(usuarios_ordenados) // 2:]

# Calcular velocidades para mover os usuários em direção às antenas atribuídas
velocidades = {}
for nome in usuarios_antena1:
    direcao = antena1 - posicoes[nome]
    velocidades[nome] = direcao / np.linalg.norm(direcao)

for nome in usuarios_antena2:
    direcao = antena2 - posicoes[nome]
    velocidades[nome] = direcao / np.linalg.norm(direcao)

# Função para atualizar a posição dos usuários
def atualizar(frame):
    for nome in posicoes:
        posicoes[nome] += velocidades[nome]  # Atualiza a posição de acordo com a velocidade
        pontos[nome].set_data(posicoes[nome][0], posicoes[nome][1])
        if nome in usuarios_antena1:
            linhas[nome].set_data([antena1[0], posicoes[nome][0]], [antena1[1], posicoes[nome][1]])
        else:
            linhas[nome].set_data([antena2[0], posicoes[nome][0]], [antena2[1], posicoes[nome][1]])
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
ax.plot(antena1[0], antena1[1], 'ro')  # Antena 1
ax.plot(antena2[0], antena2[1], 'ro')  # Antena 2

# Inicializar linhas e pontos
linhas = {nome: ax.plot([], [], 'b-')[0] for nome in usuarios}
pontos = {nome: ax.plot([], [], 'bo')[0] for nome in usuarios}

# Criando a animação
anim = FuncAnimation(fig, atualizar, frames=np.arange(0, tempo_simulacao, passo_tempo),
                     init_func=init, blit=True, repeat=False)

plt.title("Movimento dos Usuários em Direção às Antenas")
plt.xlabel("Posição X")
plt.ylabel("Posição Y")

# Exibindo a animação
plt.show()