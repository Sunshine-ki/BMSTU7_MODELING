import math
import random
import tkinter as tk
import tkinter.messagebox as mb
import matplotlib.pyplot as plt
import numpy as np
from algorithm import solve
import networkx as nx

MAIN_COLOUR = "#000000"
ADD_COLOUR = "#ffffff"

WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 800

BORDERS_PART = 0.03
BORDERS_WIDTH = int(WINDOW_WIDTH * BORDERS_PART)
BORDERS_HEIGHT = int(WINDOW_HEIGHT * BORDERS_PART)

MATRIX_PART_WIDTH = 0.7
MATRIX_WIDTH = int(MATRIX_PART_WIDTH * WINDOW_WIDTH)

MATRIX_MAX_SIZE = 10

DATA_PART_WIDTH = 1 - MATRIX_PART_WIDTH - 3 * BORDERS_PART
DATA_PART_HEIGHT = 1 - 2 * BORDERS_PART
DATA_WIDTH = int(DATA_PART_WIDTH * WINDOW_WIDTH)
DATA_HEIGHT = int(DATA_PART_HEIGHT * WINDOW_HEIGHT)

ROWS = 12

MATRIX_FRAME_ROWS = 13

root = tk.Tk()
root.title("Modeling 2")
root["bg"] = MAIN_COLOUR
root.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
root.resizable(height=False, width=False)

data_frame = tk.Frame(root)
data_frame["bg"] = MAIN_COLOUR

matrix_frame = tk.Frame(root)
matrix_frame["bg"] = MAIN_COLOUR

data_frame.place(x=int(BORDERS_WIDTH), y=int(BORDERS_HEIGHT),
                 width=DATA_WIDTH,
                 height=DATA_HEIGHT)

matrix_frame.place(x=int(BORDERS_WIDTH * 2 + DATA_WIDTH), y=int(BORDERS_HEIGHT),
                 width=MATRIX_WIDTH,
                 height=DATA_HEIGHT)

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
    tk.Entry(matrix_frame, bg=ADD_COLOUR, font=("Arial", 12), fg=MAIN_COLOUR, justify="center") 
    for i in range(MATRIX_MAX_SIZE)
]

for i in range(1, MATRIX_MAX_SIZE):
    start_probs_entries[i].insert(0, '0')
start_probs_entries[0].insert(0, '1')

matrix_entries = [
    [
        tk.Entry(matrix_frame, bg=ADD_COLOUR, font=("Arial", 12), fg=MAIN_COLOUR, justify="center")
        for i in range(MATRIX_MAX_SIZE)
    ]
    for j in range(MATRIX_MAX_SIZE)
]

for i in range(MATRIX_MAX_SIZE):
    for j in range(MATRIX_MAX_SIZE):
        matrix_entries[i][j].insert(0, '0')

def generate_random():
    global lambda_limit_entry, matrix_entries
    limit = float(lambda_limit_entry.get())
    for i in range(MATRIX_MAX_SIZE):
        for j in range(MATRIX_MAX_SIZE):
            matrix_entries[i][j].delete(0, len(matrix_entries[i][j].get()))
            matrix_entries[i][j].insert(0, '0' if i == j else f"{random.random() * limit:.2f}")

matrix_size_entry = tk.Entry(data_frame, bg=ADD_COLOUR, font=("Arial", 12),
                      fg=MAIN_COLOUR, justify="center")
matrix_size_entry.insert(0, '2')

dt_entry = tk.Entry(data_frame, bg=ADD_COLOUR, font=("Arial", 12),
                    fg=MAIN_COLOUR, justify="center")
dt_entry.insert(0, '0.1')

lambda_limit_entry = tk.Entry(data_frame, bg=ADD_COLOUR, font=("Arial", 12),
                    fg=MAIN_COLOUR, justify="center")
lambda_limit_entry.insert(0, '1.0')

lambda_limit_label = tk.Label(data_frame, text="Максимальное значение\nинтенсивности при генерации",
                       font=("Arial", 8), bg=MAIN_COLOUR,
                       fg=ADD_COLOUR, relief=tk.GROOVE)

start_probs_label = tk.Label(matrix_frame, text="Начальные вероятности\nсостояний",
                       font=("Arial", 12), bg=MAIN_COLOUR,
                       fg=ADD_COLOUR, relief=tk.GROOVE)

matrix_label = tk.Label(matrix_frame, text="Матрица интенсивностей\nпереходов состояний", font=("Arial", 12),
                        bg=MAIN_COLOUR, fg=ADD_COLOUR, relief=tk.GROOVE)

matrix_size_label = tk.Label(data_frame, text="Количество состояний", font=("Arial", 10),
                        bg=MAIN_COLOUR, fg=ADD_COLOUR, relief=tk.GROOVE)

dt_label = tk.Label(data_frame, text="параметр шага", font=("Arial", 12),
                        bg=MAIN_COLOUR, fg=ADD_COLOUR, relief=tk.GROOVE)

lambda_gen_button = tk.Button(data_frame, text="Сгенерировать\nинтенсивности", font=("Consolas", 14),
                      bg=MAIN_COLOUR, fg=ADD_COLOUR, command=generate_random,
                      activebackground=ADD_COLOUR, activeforeground=MAIN_COLOUR)
draw_graph_button = tk.Button(data_frame, text="Нарисовать граф", font=("Consolas", 14),
                      bg=MAIN_COLOUR, fg=ADD_COLOUR, command=draw_graph,
                      activebackground=ADD_COLOUR, activeforeground=MAIN_COLOUR)
solve_button = tk.Button(data_frame, text="Решить", font=("Consolas", 14),
                      bg=MAIN_COLOUR, fg=ADD_COLOUR, command=process,
                      activebackground=ADD_COLOUR, activeforeground=MAIN_COLOUR)



offset = 0
matrix_size_label.place(x=0, y=DATA_HEIGHT * offset // ROWS, width=DATA_WIDTH,
                  height=DATA_HEIGHT // ROWS)
offset += 1
matrix_size_entry.place(x=0, y=DATA_HEIGHT * offset // ROWS, width=DATA_WIDTH,
                  height=DATA_HEIGHT // ROWS)
offset += 1
dt_label.place(x=0, y=DATA_HEIGHT * offset // ROWS, width=DATA_WIDTH,
                  height=DATA_HEIGHT // ROWS)
offset += 1
dt_entry.place(x=0, y=DATA_HEIGHT * offset // ROWS, width=DATA_WIDTH,
                  height=DATA_HEIGHT // ROWS)
offset += 1
lambda_limit_label.place(x=0, y=DATA_HEIGHT * offset // ROWS, width=DATA_WIDTH,
                  height=DATA_HEIGHT // ROWS)
offset += 1
lambda_limit_entry.place(x=0, y=DATA_HEIGHT * offset // ROWS, width=DATA_WIDTH,
                  height=DATA_HEIGHT // ROWS)

offset = ROWS - 3
draw_graph_button.place(x=0, y=DATA_HEIGHT * offset // ROWS, width=DATA_WIDTH,
                  height=DATA_HEIGHT // ROWS)
offset += 1
lambda_gen_button.place(x=0, y=DATA_HEIGHT * offset // ROWS, width=DATA_WIDTH,
                  height=DATA_HEIGHT // ROWS)
offset += 1
solve_button.place(x=0, y=DATA_HEIGHT * offset // ROWS, width=DATA_WIDTH,
                  height=DATA_HEIGHT // ROWS)

offset = 0

start_probs_label.place(x=0, y=DATA_HEIGHT * offset // MATRIX_FRAME_ROWS, width=MATRIX_WIDTH,
                  height=DATA_HEIGHT // MATRIX_FRAME_ROWS)

offset += 1

for i in range(MATRIX_MAX_SIZE):
    start_probs_entries[i].place(x=int(i / MATRIX_MAX_SIZE * MATRIX_WIDTH), y=DATA_HEIGHT * offset // MATRIX_FRAME_ROWS,
                                 width=MATRIX_WIDTH // MATRIX_MAX_SIZE, height=DATA_HEIGHT // MATRIX_FRAME_ROWS)

offset += 1

matrix_label.place(x=0, y=DATA_HEIGHT * offset // MATRIX_FRAME_ROWS, width=MATRIX_WIDTH,
                  height=DATA_HEIGHT // MATRIX_FRAME_ROWS)

offset += 1

for i in range(MATRIX_MAX_SIZE):
    for j in range(MATRIX_MAX_SIZE):
        matrix_entries[i][j].place(x=int(j / MATRIX_MAX_SIZE * MATRIX_WIDTH),
                                   y=DATA_HEIGHT * (offset + i) // MATRIX_FRAME_ROWS,
                                   width=MATRIX_WIDTH // MATRIX_MAX_SIZE,
                                   height=DATA_HEIGHT // MATRIX_FRAME_ROWS)
root.mainloop()
