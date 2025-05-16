import numpy as np
from utils import calculate_total_distance

class Particle:
    def __init__(self, num_points):
        self.position = np.random.permutation(num_points)
        self.velocity = np.zeros(num_points, dtype=int)
        self.best_position = np.copy(self.position)
        self.best_score = float('inf')

class PSO:
    def __init__(self, points, num_particles=30, max_iter=100, w=0.5, c1=1.5, c2=1.5):
        self.points = points
        self.num_points = len(points)
        self.num_particles = num_particles
        self.max_iter = max_iter
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.particles = [Particle(self.num_points) for _ in range(self.num_particles)]
        self.global_best_position = None
        self.global_best_score = float('inf')

    def optimize(self):
        for iteration in range(self.max_iter):
            for particle in self.particles:
                score = calculate_total_distance(self.points, particle.position)

                if score < particle.best_score:
                    particle.best_score = score
                    particle.best_position = np.copy(particle.position)

                if score < self.global_best_score:
                    self.global_best_score = score
                    self.global_best_position = np.copy(particle.position)

            for particle in self.particles:
                new_position = self._update_position(particle)
                particle.position = new_position

        return self.global_best_position, self.global_best_score

    def _update_position(self, particle):
        new_position = np.copy(particle.position)
        if np.random.rand() < 0.5:
            i, j = np.random.choice(self.num_points, 2, replace=False)
            new_position[i], new_position[j] = new_position[j], new_position[i]
        return new_position

