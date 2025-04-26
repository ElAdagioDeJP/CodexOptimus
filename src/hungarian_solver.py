# hungarian_solver.py
from scipy.optimize import linear_sum_assignment
import numpy as np

class HungarianSolver:
    def __init__(self, cost_matrix):
        """
        cost_matrix: lista de listas (n x m) con los costes.
        """
        self.cost_matrix = cost_matrix

    def solve(self):
        """
        Devuelve:
          - assignments: dict donde cada clave i (programador) apunta
            a una lista con la tarea asignada [j].
          - total_cost: coste mínimo total (int).
        """
        # Convertimos a array de NumPy
        cost = np.array(self.cost_matrix)

        # linear_sum_assignment acepta matrices rectangulares n≤m
        row_ind, col_ind = linear_sum_assignment(cost)

        # Construimos el dict de asignaciones
        assignments = {int(i): [int(j)] for i, j in zip(row_ind, col_ind)}

        # Sumamos los costes óptimos
        total_cost = int(cost[row_ind, col_ind].sum())

        return assignments, total_cost
