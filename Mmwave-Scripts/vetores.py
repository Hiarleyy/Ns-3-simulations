#%%
import matplotlib.pyplot as plt
import numpy as np

# Solicitar a quantidade de vetores
num_vetores = int(input("Digite a quantidade de vetores: "))

# Inicializar listas para armazenar os dados dos vetores
posicoes_iniciais_x = []
posicoes_iniciais_y = []
velocidades_x = []
velocidades_y = []

# Solicitar os dados dos vetores
for i in range(num_vetores):
    pos_x = float(input(f"Digite a posição inicial em x do vetor {i+1}: "))
    pos_y = float(input(f"Digite a posição inicial em y do vetor {i+1}: "))
    vel_x = float(input(f"Digite a velocidade em x do vetor {i+1}: "))
    vel_y = float(input(f"Digite a velocidade em y do vetor {i+1}: "))
    
    posicoes_iniciais_x.append(pos_x)
    posicoes_iniciais_y.append(pos_y)
    velocidades_x.append(vel_x)
    velocidades_y.append(vel_y)

# Solicitar a quantidade de antenas
num_antenas = int(input("Digite a quantidade de antenas: "))

# Inicializar listas para armazenar as posições das antenas
posicoes_antenas_x = []
posicoes_antenas_y = []

# Solicitar os dados das antenas
for i in range(num_antenas):
    antena_x = float(input(f"Digite a posição em x da antena {i+1}: "))
    antena_y = float(input(f"Digite a posição em y da antena {i+1}: "))
    
    posicoes_antenas_x.append(antena_x)
    posicoes_antenas_y.append(antena_y)

# Solicitar a área total
area_x_min = float(input("Digite o valor mínimo da área em x: "))
area_x_max = float(input("Digite o valor máximo da área em x: "))
area_y_min = float(input("Digite o valor mínimo da área em y: "))
area_y_max = float(input("Digite o valor máximo da área em y: "))

# Solicitar o tempo de simulação
tempo_simulacao = float(input("Digite o tempo de simulação: "))

# Criar o gráfico
plt.figure(figsize=(10, 10))
plt.xlim(area_x_min, area_x_max)
plt.ylim(area_y_min, area_y_max)

# Definir cores para os vetores
cores = plt.cm.tab10(np.linspace(0, 1, num_vetores))

# Plotar os vetores e suas trajetórias
for i in range(num_vetores):
    # Calcular a posição final
    pos_final_x = posicoes_iniciais_x[i] + velocidades_x[i] * tempo_simulacao
    pos_final_y = posicoes_iniciais_y[i] + velocidades_y[i] * tempo_simulacao
    
    # Plotar a trajetória
    plt.plot([posicoes_iniciais_x[i], pos_final_x], [posicoes_iniciais_y[i], pos_final_y], color=cores[i], linestyle='--')
    
    # Plotar o vetor inicial
    plt.quiver(posicoes_iniciais_x[i], posicoes_iniciais_y[i], velocidades_x[i], velocidades_y[i], angles='xy', scale_units='xy', scale=1, color=cores[i])

    # Marcar a posição final
    plt.scatter(pos_final_x, pos_final_y, color=cores[i], label=f'Vetor {i+1}')

# Plotar as antenas
plt.scatter(posicoes_antenas_x, posicoes_antenas_y, color='black', marker='^', s=100, label='Antena')

# Configurar o gráfico
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Visualização de Vetores com Trajetórias e Antenas')
plt.legend()
plt.grid()
plt.show()

# Resumo dos parâmetros de entrada
print("\nResumo dos parâmetros de entrada:")
print(f"Quantidade de vetores: {num_vetores}")
for i in range(num_vetores):
    print(f"Vetor {i+1}: Posição inicial ({posicoes_iniciais_x[i]}, {posicoes_iniciais_y[i]}), Velocidade ({velocidades_x[i]}, {velocidades_y[i]})")
print(f"Quantidade de antenas: {num_antenas}")
for i in range(num_antenas):
    print(f"Antena {i+1}: Posição ({posicoes_antenas_x[i]}, {posicoes_antenas_y[i]})")
print(f"Área total: X de {area_x_min} a {area_x_max}, Y de {area_y_min} a {area_y_max}")
print(f"Tempo de simulação: {tempo_simulacao}")

#%%
# Gráfico de Linhas
plt.figure(figsize=(10, 10))
for i in range(num_vetores):
    pos_final_x = posicoes_iniciais_x[i] + velocidades_x[i] * tempo_simulacao
    pos_final_y = posicoes_iniciais_y[i] + velocidades_y[i] * tempo_simulacao
    plt.plot([posicoes_iniciais_x[i], pos_final_x], [posicoes_iniciais_y[i], pos_final_y], label=f'Vetor {i+1}')
plt.scatter(posicoes_antenas_x, posicoes_antenas_y, color='black', marker='^', s=100, label='Antenas')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfico de Linhas das Trajetórias dos Vetores')
plt.legend()
plt.grid()
plt.show()
