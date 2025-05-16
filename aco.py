import numpy as np
import random

def aco(points, distance_matrix, n_ants=10, n_iterations=100, alpha=1, beta=2, evaporation=0.5, Q=100):
    n = len(points)
    pheromone = np.ones((n, n))
    best_path = None
    best_length = float('inf')

    for _ in range(n_iterations):
        all_paths = []
        for _ in range(n_ants):
            path = [0]
            visited = set(path)

            while len(path) < n:
                current = path[-1]
                probabilities = []
                for j in range(n):
                    if j not in visited:
                        tau = pheromone[current][j] ** alpha
                        eta = (1 / distance_matrix[current][j]) ** beta
                        probabilities.append((j, tau * eta))
                total = sum(p for _, p in probabilities)
                probs = [(j, p / total) for j, p in probabilities]
                next_point = random.choices([j for j, _ in probs], [p for _, p in probs])[0]
                path.append(next_point)
                visited.add(next_point)

            length = sum(distance_matrix[path[i]][path[i+1]] for i in range(n-1))
            all_paths.append((path, length))

            if length < best_length:
                best_length = length
                best_path = path

        pheromone *= (1 - evaporation)
        for path, length in all_paths:
            for i in range(n - 1):
                a, b = path[i], path[i+1]
                pheromone[a][b] += Q / length
                pheromone[b][a] += Q / length

    return best_path, best_length
