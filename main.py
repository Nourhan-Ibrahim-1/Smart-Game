import tkinter as tk
from tkinter import messagebox, scrolledtext
from map import generate_map
from utils import create_distance_matrix
from aco import aco
from pso import PSO
from perceptron import extract_features, train_perceptron, predict_dangerous_cells

CELL_SIZE = 30  # حجم كل خلية في الكانفاس

def draw_map(grid, start_point, delivery_points, danger_cells):
    canvas.delete("all")  # نمسح أي رسم قديم

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            x1 = c * CELL_SIZE
            y1 = r * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE

            if (r, c) == start_point:
                color = "green"  # Start point
            elif (r, c) in delivery_points:
                color = "blue"   # delivery points
            elif (r, c) in danger_cells:
                color = "red"    # danger cells
            elif grid[r][c] == -1:
                color = "black"  # barriers
            else:
                color = "white"  # normal cells

            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")
    
    # Grid lines
    for r in range(rows + 1):
        canvas.create_line(0, r * CELL_SIZE, cols * CELL_SIZE, r * CELL_SIZE, fill="lightgray")
    for c in range(cols + 1):
        canvas.create_line(c * CELL_SIZE, 0, c * CELL_SIZE, rows * CELL_SIZE, fill="lightgray")

def run_algorithm():
    algorithm = algo_var.get()

    grid, start_point, delivery_points = generate_map()
    points = [start_point] + delivery_points
    dist_matrix = create_distance_matrix(points)

    if algorithm == 'aco':
        path, length = aco(points, dist_matrix)
    elif algorithm == 'pso':
        pso_solver = PSO(points)
        path, length = pso_solver.optimize()
    else:
        messagebox.showerror("Error", "Please select a valid algorithm")
        return

    # Perceptron part
    X, y = extract_features(grid)
    model = train_perceptron(X, y)
    danger_cells = predict_dangerous_cells(grid, model)

    # Clear previous results
    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)

    # Show results nicely formatted
    result_text.insert(tk.END, f"Best Path (indices): {path}\n\n")
    result_text.insert(tk.END, "Ordered Points:\n")
    for idx in path:
        result_text.insert(tk.END, f"-> {points[idx]}  ")
    result_text.insert(tk.END, f"\n\nTotal Distance: {length:.2f}\n\n")

    result_text.insert(tk.END, "Predicted Dangerous Cells:\n")
    for cell in danger_cells:
        result_text.insert(tk.END, f"({cell[0]}, {cell[1]})  ")

    result_text.config(state=tk.DISABLED)  # Make text box read-only after inserting

    # Draw the map with updated info
    draw_map(grid, start_point, delivery_points, danger_cells)

# Main window setup
root = tk.Tk()
root.title("Smart Game AI")
root.geometry("900x650")  

# Heading label
heading = tk.Label(root, text="Smart Game AI - Choose Algorithm and Run", font=("Helvetica", 16, "bold"))
heading.pack(pady=10)

# Frame for algorithm selection
frame_algo = tk.Frame(root)
frame_algo.pack(pady=5)

algo_var = tk.StringVar(value="aco")
tk.Label(frame_algo, text="Select AI Algorithm:", font=("Helvetica", 12)).pack(side=tk.LEFT, padx=5)
algo_menu = tk.OptionMenu(frame_algo, algo_var, "aco", "pso")
algo_menu.config(width=10)
algo_menu.pack(side=tk.LEFT)

# Run button
run_button = tk.Button(root, text="Run Algorithm", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=run_algorithm)
run_button.pack(pady=15)

# Frame to hold canvas and results side by side
frame_content = tk.Frame(root)
frame_content.pack(padx=10, pady=10)

# Canvas for drawing the map
canvas = tk.Canvas(frame_content, width=300, height=300, bg="white")
canvas.pack(side=tk.LEFT, padx=10)

# Scrollable text box for results
result_text = scrolledtext.ScrolledText(frame_content, height=20, width=60, font=("Courier New", 10))
result_text.pack(side=tk.LEFT, padx=10)
result_text.config(state=tk.DISABLED)


root.mainloop()
