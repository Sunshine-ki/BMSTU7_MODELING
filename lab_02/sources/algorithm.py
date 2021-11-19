import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

eps = 1e-3

def normalize(probs):
    s = sum(probs)
    for i in range(len(probs)):
        probs[i] /= s


def solve_ode(matrix, start_probs, dt, steady_states):
    matrix_to_solve = [
        [-sum(matrix[i]) if j == i else matrix[j][i] for j in range(len(matrix))]
        for i in range(len(matrix))]
    ts = np.arange(0, dt * 1000, dt)
    results = odeint(vectorfields, start_probs, ts,
                     args=(matrix_to_solve,), atol=1.0e-8, rtol=1.0e-6)
    results = np.transpose(results)
    steady_ts = []

    for i in range(len(results)):
        plt.plot(ts, results[i], label='p' + str(i))
        row = results[i]
        flag = True
        for j in range(len(row) - 1, -1, -1):
            if abs(steady_states[i] - row[j]) > eps:
                steady_ts.append(ts[j])
                flag = False
                break
        if flag:
            steady_ts.append(0)

    print("Времена достижения стабильного состояния:")
    for i in range(len(steady_ts)):
        print(f"t{str(i)} = {steady_ts[i]:.2f}; ", end='')
    print()

    plt.legend()
    plt.grid()
    plt.show()

def vectorfields(w, _, matrix_to_solve):
    """
    Defines the differential equations for the coupled spring-mass system.

    Arguments:
        w :  vector of the state variables:
                  w = [p1, p2, p3...]
        _ :  time
        matrix_to_solve :  vector of the parameters:
                  lambdas = [[lambda_ji for i in range(len(matrix))] for j in range(len(matrix))]
    """
    f = []
    for i in range(len(w)):
        f.append(0)
        for p, lambda_coeff in zip(w, matrix_to_solve[i]):
            f[i] += p * lambda_coeff

    return f

def solve(matrix, start_probs, dt):
    normalize(start_probs)
    b = [0 for _ in range(len(matrix) - 1)]
    b.append(1)
    matrix_to_solve = [
        [-sum(matrix[i]) if j == i else matrix[j][i] for j in range(len(matrix))]
        for i in range(len(matrix) - 1)]
    matrix_to_solve.append([1 for _ in range(len(matrix))])

    ps = np.linalg.solve(matrix_to_solve, b)
    print("Стабильное состояние:")
    for i in range(len(ps)):
        print(f"p{str(i)} = {ps[i]:.2f}; ", end='')
    print()
    max_lambda = max([max(matrix[i]) for i in range(len(matrix))])
    avg_lambda = sum([sum(matrix[i]) for i in range(len(matrix))]) / len(matrix) / (len(matrix) - 1)
    dt = (1 / (max_lambda + avg_lambda) * 2) * dt
    solve_ode(matrix, start_probs, dt, ps)
