# Batman Algorithm  🦇 🦇 🦇

**Language / Idioma:** [🇺🇸 English](bat_ENG.md) | [🇧🇷 Português](bat.md)

The [code](https://github.com/Hiarleyy/Ns-3-simulations/blob/main/batman.py) implements a simplified version of the BAT (Bat Algorithm) for optimizing user positioning in an internet network, considering the presence of an antenna and user movement. Let's analyze what each part of the code does:

### Imports and Constant Definition
```python
import numpy as np
import matplotlib.pyplot as plt
```

#### Defining constants
```python
NUM_USERS = 2
DIMENSIONS = 2  # x, y
BAT_POPULATION = 30
MAX_ITER = 1000
```
Here, the necessary libraries are imported and constants are defined for the number of users, space dimensions (2D), bat population size, and maximum number of iterations.

### Auxiliary Functions

#### Signal Intensity Function
```python
def signal_intensity(antenna_pos, user_pos):
    distance = np.linalg.norm(antenna_pos - user_pos, axis=1)
    return 1 / (distance ** 2)
```
This function calculates signal intensity based on the distance between the antenna and user positions.

#### Application Priority Function
```python
def application_priority(app_type):
    priorities = {'video': 1.0, 'voice': 0.8, 'data': 0.5}
    return priorities.get(app_type, 0.5)
```

This function assigns a priority for each application type (video, voice, data).

#### Fitness Function
```python
def fitness(antenna_pos, user_positions, user_apps):
    intensities = signal_intensity(antenna_pos, user_positions)
    priorities = np.array([application_priority(app) for app in user_apps])
    return np.sum(intensities * priorities)
```

The fitness function evaluates the quality of user positions based on signal intensity and application priority.

### Bat Initialization
```python
def initialize_bats(num_bats, num_users, dimensions, min_dist=300, max_dist=500):
    user_positions = []
    for _ in range(num_bats):
        user_positions.append(np.random.uniform(min_dist, max_dist, (num_users, dimensions)))
    return np.array(user_positions)
```

This function randomly initializes user positions within a defined range.

### Position Update

```python
def update_position(bats, best_bat, f_min, f_max, antenna_pos, app_priorities, separation_factor=0.8, lower_bound=0, upper_bound=500):
    beta = np.random.rand()
    freq = f_min + (f_max - f_min) * beta
    v = np.random.rand(*bats.shape) * (bats - best_bat)
    new_positions = bats + v * freq

    new_positions = np.clip(new_positions, lower_bound, upper_bound)

    for i in range(len(new_positions)):
        for j in range(len(new_positions[i])):
            original_distance = np.linalg.norm(antenna_pos - bats[i, j])
            new_distance = np.linalg.norm(antenna_pos - new_positions[i, j])
            if new_distance > original_distance:
                direction = (bats[i, j] - antenna_pos) / np.linalg.norm(bats[i, j] - antenna_pos)
                new_positions[i, j] = bats[i, j] + direction * (original_distance - new_distance) * separation_factor

    min_user_distance = 50
    for i in range(len(new_positions)):
        for j in range(len(new_positions[i])):
            for k in range(j + 1, len(new_positions[i])):
                distance = np.linalg.norm(new_positions[i, j] - new_positions[i, k])
                if distance < min_user_distance:
                    direction = (new_positions[i, j] - new_positions[i, k]) / distance
                    new_positions[i, j] += direction * (min_user_distance - distance) / 2
                    new_positions[i, k] -= direction * (min_user_distance - distance) / 2

    min_antenna_distance = 50
    for i in range(len(new_positions)):
        for j in range(len(new_positions[i])):
            distance_to_antenna = np.linalg.norm(new_positions[i, j] - antenna_pos)
            if distance_to_antenna < min_antenna_distance:
                direction = (new_positions[i, j] - antenna_pos) / distance_to_antenna
                new_positions[i, j] = antenna_pos + direction * min_antenna_distance

    return new_positions
```
This function updates bat (user) positions, ensuring that new positions respect certain conditions such as minimum distance from the antenna and between users.

### Main BAT Algorithm
```python
def bat_algorithm(antenna_pos, user_positions, user_apps, num_bats=BAT_POPULATION, max_iter=MAX_ITER):
    bats = initialize_bats(num_bats, NUM_USERS, DIMENSIONS, min_dist=50, max_dist=450)
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
```
This function implements the BAT algorithm for optimizing user positions, searching for the best position that maximizes the fitness function.

### Plotting and Usage Example
```python
def plot_results(antenna_pos, original_user_pos, new_user_pos):
    plt.figure(figsize=(10, 10))

    plt.scatter(*antenna_pos, color='red', label='Antenna', s=100)
    plt.scatter(*original_user_pos.T, color='blue', label='Original Users', s=50)

    for i in range(len(new_user_pos)):
        plt.scatter(new_user_pos[i, 0], new_user_pos[i, 1], color='green', label='Optimized Users' if i == 0 else '')

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
```
# Usage Example
```python
antenna_pos = np.array([250, 250])
user_positions = initialize_bats(1, NUM_USERS, DIMENSIONS, min_dist=50, max_dist=450)[0]
user_apps = np.random.choice(['low', 'medium', 'high'], NUM_USERS)

new_user_positions, fitness_history = bat_algorithm(antenna_pos, user_positions, user_apps)
plot_results(antenna_pos, user_positions, new_user_positions)

print("Antenna Position:", antenna_pos)
print("Original User Positions:")
for i, (pos, app) in enumerate(zip(user_positions, user_apps)):
    print(f"User {i+1}: Position: {pos}, Application Priority: {app}")
print("Optimized User Positions:")
for i, (pos, app) in enumerate(zip(new_user_positions, user_apps)):
    print(f"User {i+1}: Position: {pos}, Application Priority: {app}")
print("Optimized user displacement:")
for i in range(NUM_USERS):
    displacement = np.linalg.norm(new_user_positions[i] - user_positions[i])
    print(f"User {i+1}: Displacement: {displacement:.2f}")
print("User distance relative to antenna:")
for i in range(NUM_USERS):
    distance_before = np.linalg.norm(user_positions[i] - antenna_pos)
    distance_after = np.linalg.norm(new_user_positions[i] - antenna_pos)
    print(f"User {i+1}: Before: {distance_before:.2f}, After: {distance_after:.2f}")
```
The plot_results function plots user positions before and after optimization. The usage example initializes user positions, executes the BAT algorithm for optimization, and plots the results, while also printing user positions and displacements.

### Summary
The code simulates a scenario where network users move relative to an antenna, optimizing their positions to improve signal intensity and prioritize certain types of applications. It uses the BAT algorithm for this optimization, ensuring that new positions are adequate and respect necessary minimum distances.
