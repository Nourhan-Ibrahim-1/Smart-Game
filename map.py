import numpy as np
import random

def generate_map(size=10, num_deliveries=4, num_obstacles=10):
    grid = np.zeros((size, size), dtype=int)

    # Delivery points = 2
    delivery_points = []
    for _ in range(num_deliveries):
        while True:
            x, y = random.randint(0, size - 1), random.randint(0, size - 1)
            if grid[x, y] == 0:
                grid[x, y] = 2
                delivery_points.append((x, y))
                break

    # Obstacles = -1
    for _ in range(num_obstacles):
        while True:
            x, y = random.randint(0, size - 1), random.randint(0, size - 1)
            if grid[x, y] == 0:
                grid[x, y] = -1
                break

    # Start point = 1
    grid[0, 0] = 1
    start_point = (0, 0)

    return grid, start_point, delivery_points
