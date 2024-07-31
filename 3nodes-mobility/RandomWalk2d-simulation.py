#%%
# Random Walk 2D Mobility Model with Obstacles
import random
import matplotlib.pyplot as plt
import math

class RandomWalk2dMobilityModel:
    def __init__(self, x, y, step_size=2.0, bounds=(-50, 50, -50, 50), antenna_position=(0.0, 50.0), obstacles=[]):
        self.x = x
        self.y = y
        self.step_size = step_size
        self.bounds = bounds
        self.antenna_position = antenna_position
        self.obstacles = obstacles

    def move(self):
        # Calculate the angle towards the antenna
        dx = self.antenna_position[0] - self.x
        dy = self.antenna_position[1] - self.y
        angle = math.atan2(dy, dx)
        
        # Add some randomness to the movement
        angle += random.uniform(-0.5, 0.5)
        
        # Calculate the new position
        new_x = self.x + self.step_size * math.cos(angle)
        new_y = self.y + self.step_size * math.sin(angle)
        
        # Check for obstacles and adjust the movement if necessary
        for ox, oy in self.obstacles:
            if math.hypot(new_x - ox, new_y - oy) < self.step_size:
                # Move away from the obstacle
                angle += math.pi / 2  # Turn 90 degrees
                new_x = self.x + self.step_size * math.cos(angle)
                new_y = self.y + self.step_size * math.sin(angle)
                break
        
        # Ensure the node stays within bounds
        self.x = max(self.bounds[0], min(new_x, self.bounds[1]))
        self.y = max(self.bounds[2], min(new_y, self.bounds[3]))
        
        return self.x, self.y

def simulate_movement(nodes, steps=100):
    trajectories = [[] for _ in nodes]
    for _ in range(steps):
        for i, node in enumerate(nodes):
            x, y = node.move()
            trajectories[i].append((x, y))
    return trajectories

def plot_trajectories(trajectories, obstacles):
    for i, trajectory in enumerate(trajectories):
        x, y = zip(*trajectory)
        plt.plot(x, y, label=f'User {i+1}')
    plt.scatter([0], [50], c='red', marker='x', label='Antenna')
    ox, oy = zip(*obstacles)
    plt.scatter(ox, oy, c='black', marker='o', label='Obstacles')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('User Trajectories with Obstacles')
    plt.grid(True)
    plt.show()

# Create obstacles with random positions
obstacles = [(random.uniform(-50, 50), random.uniform(-50, 50)) for _ in range(20)]

# Create nodes for three users with random initial positions
nodes = [
    RandomWalk2dMobilityModel(
        x=random.uniform(-50, 50),
        y=random.uniform(-50, 50),
        obstacles=obstacles
    ) for _ in range(3)
]

# Simulate movement
trajectories = simulate_movement(nodes, steps=100)

# Plot the trajectories
plot_trajectories(trajectories, obstacles)
# %%

