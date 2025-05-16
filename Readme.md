# Smart Game 

An intelligent game-based platform that combines multiple AI algorithms to determine the optimal delivery path while avoiding predicted dangerous zones. Designed for research, learning, and experimentation in smart decision-making systems using modern AI techniques.

---

## 📚 Table of Contents
- [🚀 Features](#-features)
- [📦 Project Structure](#-project-structure)
- [🧰 Tech Stack](#-tech-stack)

---

## 🚀 Features
- 🧠 **Multiple AI Algorithms:** Choose between ACO (Ant Colony Optimization) and PSO (Particle Swarm Optimization) to find the best delivery route.
- 🛡️ **Risk Prediction:** Uses a trained Perceptron model to predict and highlight dangerous zones on the map.
- 🗺️ **Interactive Map Visualization:** Visual display of the map including start point, delivery points, obstacles, and predicted dangers.
- 🧪 **Custom Map Generation:** Randomized intelligent map generation with realistic delivery and danger scenarios.
- 🖥️ **User-Friendly GUI:** Simple and intuitive interface to select algorithm, view results, and visualize predictions.

---

## 📦 Project Structure
Smart-Game/

├── aco.py # Ant Colony Optimization logic

├── pso.py # Particle Swarm Optimization logic

├── perceptron.py # Perceptron model for danger prediction

├── utils.py # Utility functions (distance, features, etc.)

├── map.py # Grid/map generation and configuration

├── gui.py # Tkinter-based graphical interface

├── requirements.txt # List of required Python packages

└── README.md # Project documentation


---

## 🧰 Tech Stack
- **AI Algorithms:** Ant Colony Optimization, Particle Swarm Optimization, Perceptron
- **Programming Language:** Python 
- **GUI Framework:** Tkinter
- **Data Handling:** NumPy, scikit-learn
- **Visualization:** Tkinter Canvas (for grid/map rendering)

---







