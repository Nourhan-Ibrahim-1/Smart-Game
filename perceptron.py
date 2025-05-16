# perceptron.py
import numpy as np
from sklearn.linear_model import Perceptron

def extract_features(grid):
    X = []
    y = []
    size = grid.shape[0]

    for i in range(size):
        for j in range(size):
            val = grid[i, j]
            features = [i, j, val]
            X.append(features)
            # Dangerous only if -1
            label = 1 if val == -1 else 0
            y.append(label)

    return np.array(X), np.array(y)

def train_perceptron(X, y):
    model = Perceptron()
    model.fit(X, y)
    return model

def predict_dangerous_cells(grid, model):
    X, _ = extract_features(grid)
    preds = model.predict(X)
    dangerous_cells = []

    index = 0
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if preds[index] == 1:
                dangerous_cells.append((i, j))
            index += 1
    return dangerous_cells
