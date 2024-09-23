#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%%
# Carregando os dados
sinr = pd.read_csv('RxPacketTrace.txt',sep='\t',usecols=['rnti','DL/UL','SINR(dB)','time'])
sinr
# %%
sinr_grouped_1 = sinr[(sinr['rnti'] == 1)]
user1_mean = sinr_grouped_1['SINR(dB)'].mean()
user1_mean = user1_mean.__round__(2)
# %%
sinr_grouped_2 = sinr[(sinr['rnti'] == 2)]
user2_mean = sinr_grouped_2['SINR(dB)'].mean()
user2_mean = user2_mean.__round__(2)
#%%
sinr_grouped_3 = sinr[(sinr['rnti'] == 3)]
user3_mean = sinr_grouped_3['SINR(dB)'].mean()
user3_mean = user3_mean.__round__(2)
#%%
df = pd.read_csv('distance-trace.txt',sep='\t',usecols=['UE Id','DistanceX','DistanceY','Time'])
df['rnti'] = df['UE Id']
df.drop('UE Id', axis=1, inplace=True)
df['rnti'] = df['rnti'].replace({0: 1, 1: 2, 2: 3})
df

#%%
def func_prioridade(rnti):
    if rnti in [1]:
        return user1_mean 
    elif rnti in [2]:
        return user2_mean
    elif rnti in [3]:
        return user3_mean
    return None  # Caso o RNTI não esteja em nenhuma das categorias acima

df['sinr'] = df['rnti'].apply(func_prioridade)
df

# %%
df['time_interval']= (df['Time']//0.1)*0.1
df
#%%
df_grouped = df.groupby('time_interval').mean().reset_index()
df_grouped
#%% _______________________
# treinamento do modelo
'''class Environment:
    def __init__(self, width, height, antenna_position):
        self.width = width
        self.height = height
        self.antenna_position = antenna_position
    
    def calculate_sinr(self, position):
        distance = np.sqrt((position[0] - self.antenna_position[0])**2 + (position[1] - self.antenna_position[1])**2)
        sinr = np.exp(-distance / (0.1 * self.width))  # Função exponencial inversa
        return sinr
    
    def get_reward(self, position):
        sinr = self.calculate_sinr(position)
        return sinr if sinr > 0.7 else 0
    
    def is_terminal_state(self, position):
        return self.calculate_sinr(position) >= 0.7

# Implementar o Q-Learning
class QLearningAgent:
    def __init__(self, env, learning_rate=0.1, discount_factor=0.9, exploration_rate=1.0, exploration_decay=0.99):
        self.env = env
        self.lr = learning_rate
        self.df = discount_factor
        self.er = exploration_rate
        self.ed = exploration_decay
        self.q_table = np.zeros((env.width, env.height, 4))
        self.actions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Up, Right, Down, Left
    
    def choose_action(self, state):
        if np.random.random() < self.er:
            return np.random.choice(len(self.actions))
        return np.argmax(self.q_table[state[0], state[1]])
    
    def update_q_table(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.q_table[next_state[0], next_state[1]])
        td_target = reward + self.df * self.q_table[next_state[0], next_state[1], best_next_action]
        td_error = td_target - self.q_table[state[0], state[1], action]
        self.q_table[state[0], state[1], action] += self.lr * td_error
    
    def train(self, episodes):
        for episode in range(episodes):
            state = (np.random.randint(0, self.env.width), np.random.randint(0, self.env.height))
            while not self.env.is_terminal_state(state):
                action = self.choose_action(state)
                next_state = (state[0] + self.actions[action][0], state[1] + self.actions[action][1])
                next_state = (max(0, min(next_state[0], self.env.width - 1)), max(0, min(next_state[1], self.env.height - 1)))
                reward = self.env.get_reward(next_state)
                self.update_q_table(state, action, reward, next_state)
                state = next_state
            self.er *= self.ed
    
    def get_best_path(self, start_state):
        path = [start_state]
        state = start_state
        while not self.env.is_terminal_state(state):
            action = np.argmax(self.q_table[state[0], state[1]])
            next_state = (state[0] + self.actions[action][0], state[1] + self.actions[action][1])
            next_state = (max(0, min(next_state[0], self.env.width - 1)), max(0, min(next_state[1], self.env.height - 1)))
            path.append(next_state)
            state = next_state
        return path

# Configurações do ambiente
width = 10
height = 10
antenna_position = (width // 2, height // 2)
env = Environment(width, height, antenna_position)

# Treinamento do agente
agent = QLearningAgent(env)
agent.train(1000)

# Trajetória aleatória
def get_random_path(start_state, env):
    path = [start_state]
    state = start_state
    while not env.is_terminal_state(state):
        action = np.random.choice(len(agent.actions))
        next_state = (state[0] + agent.actions[action][0], state[1] + agent.actions[action][1])
        next_state = (max(0, min(next_state[0], env.width - 1)), max(0, min(next_state[1], env.height - 1)))
        path.append(next_state)
        state = next_state
    return path

start_state = (0, 0)
random_path = get_random_path(start_state, env)
best_path = agent.get_best_path(start_state)

# Plotar as trajetórias
plt.figure(figsize=(10, 10))
plt.plot(*zip(*random_path), marker='o', color='r', label='Trajetória Aleatória')
plt.plot(*zip(*best_path), marker='o', color='b', label='Trajetória ML')
plt.scatter(*antenna_position, color='g', s=200, label='Antena')
plt.xlim(-1, width)
plt.ylim(-1, height)
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Trajetórias de Movimentação do Usuário')
plt.grid()
plt.show()'''


'''# %%
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Carregar os dados
df = pd.read_csv('distance-trace.txt', sep='\t', usecols=['UE Id', 'DistanceX', 'DistanceY', 'Time'])
df['rnti'] = df['UE Id']
df.drop('UE Id', axis=1, inplace=True)
df['rnti'] = df['rnti'].replace({0: 1, 1: 2, 2: 3})

# Agrupar os dados por rnti e Time
grouped = df.groupby(['rnti', 'Time']).mean().reset_index()

# Função para treinar o modelo e prever as trajetórias
def train_and_predict_trajectory(df, rnti):
    user_data = df[df['rnti'] == rnti]
    X = user_data[['Time']]
    y = user_data[['DistanceX', 'DistanceY']]
    
    model = LinearRegression()
    model.fit(X, y)
    
    predictions = model.predict(X)
    return user_data, predictions

# Treinar e prever para cada usuário
user1_data, user1_predictions = train_and_predict_trajectory(grouped, 1)
user2_data, user2_predictions = train_and_predict_trajectory(grouped, 2)
user3_data, user3_predictions = train_and_predict_trajectory(grouped, 3)

# Função para plotar as trajetórias bidimensionais
def plot_trajectories_2d(user_data, predictions, rnti):
    plt.figure(figsize=(10, 10))
    plt.plot(user_data['DistanceX'], user_data['DistanceY'], label='Original Trajectory')
    plt.plot(predictions[:, 0], predictions[:, 1], label='Predicted Trajectory', linestyle='--')
    plt.scatter(0, 0, color='red', label='Point (0,0)')
    plt.xlim(user_data['DistanceX'].min(), user_data['DistanceX'].max())
    plt.ylim(user_data['DistanceY'].min(), user_data['DistanceY'].max())
    plt.title(f'2D Trajectories for User {rnti}')
    plt.xlabel('DistanceX')
    plt.ylabel('DistanceY')
    plt.legend()
    plt.grid(True)
    plt.show()

# Plotar as trajetórias bidimensionais antes e depois do treinamento
plot_trajectories_2d(user1_data, user1_predictions, 1)
plot_trajectories_2d(user2_data, user2_predictions, 2)
plot_trajectories_2d(user3_data, user3_predictions, 3)
'''
#%%
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Carregar os dados
df = pd.read_csv('distance-trace.txt', sep='\t', usecols=['UE Id', 'DistanceX', 'DistanceY', 'Time'])
df['rnti'] = df['UE Id']
df.drop('UE Id', axis=1, inplace=True)
df['rnti'] = df['rnti'].replace({0: 1, 1: 2, 2: 3})

# Agrupar os dados por rnti e Time
grouped = df.groupby(['rnti', 'Time']).mean().reset_index()

# Função para treinar o modelo e prever as trajetórias
def train_and_predict_trajectory(df, rnti):
    user_data = df[df['rnti'] == rnti]
    X = user_data[['Time']]
    y = user_data[['DistanceX', 'DistanceY']]
    
    model = LinearRegression()
    model.fit(X, y)
    
    predictions = model.predict(X)
    return user_data, predictions

# Treinar e prever para cada usuário
user1_data, user1_predictions = train_and_predict_trajectory(grouped, 1)
user2_data, user2_predictions = train_and_predict_trajectory(grouped, 2)
user3_data, user3_predictions = train_and_predict_trajectory(grouped, 3)

# Função para plotar as trajetórias bidimensionais de múltiplos usuários
def plot_trajectories_2d(users_data, users_predictions):
    plt.figure(figsize=(10, 10))
    
    colors = ['blue', 'green', 'orange']
    for i, (user_data, predictions, rnti) in enumerate(users_data):
        plt.plot(user_data['DistanceX'], user_data['DistanceY'], label=f'Original Trajectory User {rnti}', color=colors[i])
        plt.plot(predictions[:, 0], predictions[:, 1], label=f'Predicted Trajectory User {rnti}', linestyle='--', color=colors[i])
    
    plt.scatter(0, 0, color='red', label='Point (0,0)')
    
    # Definir limites dos eixos com base nos valores das colunas
    all_distances_x = pd.concat([user_data['DistanceX'] for user_data, _, _ in users_data])
    all_distances_y = pd.concat([user_data['DistanceY'] for user_data, _, _ in users_data])
    plt.xlim(all_distances_x.min(), all_distances_x.max())
    plt.ylim(all_distances_y.min(), all_distances_y.max())
    
    plt.title('2D Trajectories for All Users')
    plt.xlabel('DistanceX')
    plt.ylabel('DistanceY')
    plt.legend()
    plt.grid(True)
    plt.show()

# Plotar as trajetórias bidimensionais antes e depois do treinamento para todos os usuários
users_data = [(user1_data, user1_predictions, 1), (user2_data, user2_predictions, 2), (user3_data, user3_predictions, 3)]
plot_trajectories_2d(users_data, [user1_predictions, user2_predictions, user3_predictions])
# %%
