import math
import random
import tkinter as tk
import config as cfg
import tkinter.messagebox as mb
import matplotlib.pyplot as plt
import numpy as np
from algorithm import solve
import networkx as nx

root = tk.Tk()
root.title("Modeling 2")
root["bg"] = cfg.MAIN_COLOUR
root.geometry(str(cfg.WINDOW_WIDTH) + "x" + str(cfg.WINDOW_HEIGHT))
root.resizable(height=False, width=False)

data_frame = tk.Frame(root)
data_frame["bg"] = cfg.MAIN_COLOUR

matrix_frame = tk.Frame(root)
matrix_frame["bg"] = cfg.MAIN_COLOUR

data_frame.place(x=int(cfg.BORDERS_WIDTH), y=int(cfg.BORDERS_HEIGHT),
                 width=cfg.DATA_WIDTH,
                 height=cfg.DATA_HEIGHT)

matrix_frame.place(x=int(cfg.BORDERS_WIDTH * 2 + cfg.DATA_WIDTH), y=int(cfg.BORDERS_HEIGHT),
                 width=cfg.MATRIX_WIDTH,
                 height=cfg.DATA_HEIGHT)

def process():
    global matrix_entries, dt_entry, matrix_size_entry, start_probs_entries
    size = int(matrix_size_entry.get())
    matrix = [[float(matrix_entries[i][j].get()) for j in range(size)] for i in range(size)]
    start_probs = [float(start_probs_entries[i].get()) for i in range(size)]
    dt = float(dt_entry.get())
    solve(matrix, start_probs, dt)


def draw_graph():
    global matrix_entries, matrix_size_entry
    size = int(matrix_size_entry.get())
    matrix = [[float(matrix_entries[i][j].get()) for j in range(size)] for i in range(size)]

    G = nx.from_numpy_matrix(np.matrix(matrix), create_using=nx.DiGraph)
    layout = nx.circular_layout(G)
    nx.draw(G, layout, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=nx.get_edge_attributes(G,'weight'), label_pos=0.2)
    plt.show()


start_probs_entries = [
    tk.Entry(matrix_frame, bg=cfg.ADD_COLOUR, font=("Arial", 12), fg=cfg.MAIN_COLOUR, justify="center") 
    for i in range(cfg.MATRIX_MAX_SIZE)
]

for i in range(1, cfg.MATRIX_MAX_SIZE):
    start_probs_entries[i].insert(0, '0')
start_probs_entries[0].insert(0, '1')

matrix_entries = [
    [
        tk.Entry(matrix_frame, bg=cfg.ADD_COLOUR, font=("Arial", 12), fg=cfg.MAIN_COLOUR, justify="center")
        for i in range(cfg.MATRIX_MAX_SIZE)
    ]
    for j in range(cfg.MATRIX_MAX_SIZE)
]

for i in range(cfg.MATRIX_MAX_SIZE):
    for j in range(cfg.MATRIX_MAX_SIZE):
        matrix_entries[i][j].insert(0, '0')

def generate_random():
    global lambda_limit_entry, matrix_entries
    limit = float(lambda_limit_entry.get())
    for i in range(cfg.MATRIX_MAX_SIZE):
        for j in range(cfg.MATRIX_MAX_SIZE):
            matrix_entries[i][j].delete(0, len(matrix_entries[i][j].get()))
            matrix_entries[i][j].insert(0, '0' if i == j else f"{random.random() * limit:.2f}")

matrix_size_entry = tk.Entry(data_frame, bg=cfg.ADD_COLOUR, font=("Arial", 12),
                      fg=cfg.MAIN_COLOUR, justify="center")
matrix_size_entry.insert(0, '2')

dt_entry = tk.Entry(data_frame, bg=cfg.ADD_COLOUR, font=("Arial", 12),
                    fg=cfg.MAIN_COLOUR, justify="center")
dt_entry.insert(0, '0.1')

lambda_limit_entry = tk.Entry(data_frame, bg=cfg.ADD_COLOUR, font=("Arial", 12),
                    fg=cfg.MAIN_COLOUR, justify="center")
lambda_limit_entry.insert(0, '1.0')

lambda_limit_label = tk.Label(data_frame, text="Максимальное значение\nинтенсивности при генерации",
                       font=("Arial", 8), bg=cfg.MAIN_COLOUR,
                       fg=cfg.ADD_COLOUR, relief=tk.GROOVE)

start_probs_label = tk.Label(matrix_frame, text="Начальные вероятности\nсостояний",
                       font=("Arial", 12), bg=cfg.MAIN_COLOUR,
                       fg=cfg.ADD_COLOUR, relief=tk.GROOVE)

matrix_label = tk.Label(matrix_frame, text="Матрица интенсивностей\nпереходов состояний", font=("Arial", 12),
                        bg=cfg.MAIN_COLOUR, fg=cfg.ADD_COLOUR, relief=tk.GROOVE)

matrix_size_label = tk.Label(data_frame, text="Количество состояний", font=("Arial", 10),
                        bg=cfg.MAIN_COLOUR, fg=cfg.ADD_COLOUR, relief=tk.GROOVE)

dt_label = tk.Label(data_frame, text="параметр шага", font=("Arial", 12),
                        bg=cfg.MAIN_COLOUR, fg=cfg.ADD_COLOUR, relief=tk.GROOVE)

lambda_gen_button = tk.Button(data_frame, text="Сгенерировать\nинтенсивности", font=("Consolas", 14),
                      bg=cfg.MAIN_COLOUR, fg=cfg.ADD_COLOUR, command=generate_random,
                      activebackground=cfg.ADD_COLOUR, activeforeground=cfg.MAIN_COLOUR)
draw_graph_button = tk.Button(data_frame, text="Нарисовать граф", font=("Consolas", 14),
                      bg=cfg.MAIN_COLOUR, fg=cfg.ADD_COLOUR, command=draw_graph,
                      activebackground=cfg.ADD_COLOUR, activeforeground=cfg.MAIN_COLOUR)
solve_button = tk.Button(data_frame, text="Решить", font=("Consolas", 14),
                      bg=cfg.MAIN_COLOUR, fg=cfg.ADD_COLOUR, command=process,
                      activebackground=cfg.ADD_COLOUR, activeforeground=cfg.MAIN_COLOUR)



offset = 0
matrix_size_label.place(x=0, y=cfg.DATA_HEIGHT * offset // cfg.ROWS, width=cfg.DATA_WIDTH,
                  height=cfg.DATA_HEIGHT // cfg.ROWS)
offset += 1
matrix_size_entry.place(x=0, y=cfg.DATA_HEIGHT * offset // cfg.ROWS, width=cfg.DATA_WIDTH,
                  height=cfg.DATA_HEIGHT // cfg.ROWS)
offset += 1
dt_label.place(x=0, y=cfg.DATA_HEIGHT * offset // cfg.ROWS, width=cfg.DATA_WIDTH,
                  height=cfg.DATA_HEIGHT // cfg.ROWS)
offset += 1
dt_entry.place(x=0, y=cfg.DATA_HEIGHT * offset // cfg.ROWS, width=cfg.DATA_WIDTH,
                  height=cfg.DATA_HEIGHT // cfg.ROWS)
offset += 1
lambda_limit_label.place(x=0, y=cfg.DATA_HEIGHT * offset // cfg.ROWS, width=cfg.DATA_WIDTH,
                  height=cfg.DATA_HEIGHT // cfg.ROWS)
offset += 1
lambda_limit_entry.place(x=0, y=cfg.DATA_HEIGHT * offset // cfg.ROWS, width=cfg.DATA_WIDTH,
                  height=cfg.DATA_HEIGHT // cfg.ROWS)

offset = cfg.ROWS - 3
draw_graph_button.place(x=0, y=cfg.DATA_HEIGHT * offset // cfg.ROWS, width=cfg.DATA_WIDTH,
                  height=cfg.DATA_HEIGHT // cfg.ROWS)
offset += 1
lambda_gen_button.place(x=0, y=cfg.DATA_HEIGHT * offset // cfg.ROWS, width=cfg.DATA_WIDTH,
                  height=cfg.DATA_HEIGHT // cfg.ROWS)
offset += 1
solve_button.place(x=0, y=cfg.DATA_HEIGHT * offset // cfg.ROWS, width=cfg.DATA_WIDTH,
                  height=cfg.DATA_HEIGHT // cfg.ROWS)

offset = 0

start_probs_label.place(x=0, y=cfg.DATA_HEIGHT * offset // cfg.MATRIX_FRAME_ROWS, width=cfg.MATRIX_WIDTH,
                  height=cfg.DATA_HEIGHT // cfg.MATRIX_FRAME_ROWS)

offset += 1

for i in range(cfg.MATRIX_MAX_SIZE):
    start_probs_entries[i].place(x=int(i / cfg.MATRIX_MAX_SIZE * cfg.MATRIX_WIDTH), y=cfg.DATA_HEIGHT * offset // cfg.MATRIX_FRAME_ROWS,
                                 width=cfg.MATRIX_WIDTH // cfg.MATRIX_MAX_SIZE, height=cfg.DATA_HEIGHT // cfg.MATRIX_FRAME_ROWS)

offset += 1

matrix_label.place(x=0, y=cfg.DATA_HEIGHT * offset // cfg.MATRIX_FRAME_ROWS, width=cfg.MATRIX_WIDTH,
                  height=cfg.DATA_HEIGHT // cfg.MATRIX_FRAME_ROWS)

offset += 1

for i in range(cfg.MATRIX_MAX_SIZE):
    for j in range(cfg.MATRIX_MAX_SIZE):
        matrix_entries[i][j].place(x=int(j / cfg.MATRIX_MAX_SIZE * cfg.MATRIX_WIDTH),
                                   y=cfg.DATA_HEIGHT * (offset + i) // cfg.MATRIX_FRAME_ROWS,
                                   width=cfg.MATRIX_WIDTH // cfg.MATRIX_MAX_SIZE,
                                   height=cfg.DATA_HEIGHT // cfg.MATRIX_FRAME_ROWS)
root.mainloop()
