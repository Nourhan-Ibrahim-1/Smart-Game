import numpy as np
import math

def distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

def create_distance_matrix(points):
    n = len(points)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = distance(points[i], points[j])
    return dist_matrix
def calculate_total_distance(points, order):
    
    total_distance = 0.0
    for i in range(len(order) - 1):
        p1 = points[order[i]]
        p2 = points[order[i + 1]]
        dist = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
        total_distance += dist
    return total_distance