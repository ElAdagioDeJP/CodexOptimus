import numpy as np
from scipy.optimize import linear_sum_assignment

class ServerAllocationSolver:
    def __init__(self, cost_matrix, capacities, priorities):
        """
        cost_matrix: lista de listas de tamaño S x R, C[i][j] = tiempo si j→i
        capacities: lista de tamaño S, recursos (unidades) disponibles en cada servidor
        priorities: lista de tamaño R, prioridad (mayor = más urgente) de cada solicitud
        """
        self.cost_matrix = np.array(cost_matrix, dtype=float)
        self.capacities = capacities
        self.priorities = np.array(priorities, dtype=float)
        self.S, self.R = self.cost_matrix.shape

    def solve(self):
        # 1) Ponderar costos por prioridad (más prioridad ⇒ costo efectivo menor)
        #    Aquí dividimos C[i,j] / priority[j]
        weighted = self.cost_matrix / self.priorities

        # 2) Replicar cada servidor tantas veces como unidades de capacidad tenga
        replicated_rows = []
        server_map = []  # para volver de la fila replicada al índice original
        for i, cap in enumerate(self.capacities):
            for _ in range(cap):
                replicated_rows.append(weighted[i])
                server_map.append(i)
        W = np.vstack(replicated_rows)  # matriz M x R, M = sum(capacities)

        # 3) Aplicar el Método Húngaro sobre W para asignación uno-a-uno
        row_ind, col_ind = linear_sum_assignment(W)

        # 4) Construir resultado
        assignments = {}            # req_idx → server_idx
        workload = {i: 0 for i in range(self.S)}
        total_time = 0.0
        details = []  # lista de tuplas (req, serv, raw_cost, priority)

        for r, j in zip(row_ind, col_ind):
            if j < self.R:  # descartamos posibles "columnas de relleno" si R < M
                s_idx = server_map[r]
                # registrar asignación
                assignments[j] = s_idx
                workload[s_idx] += 1
                # sumar tiempo real (sin ponderar)
                total_time += self.cost_matrix[s_idx, j]
                details.append((j, s_idx,
                                self.cost_matrix[s_idx, j],
                                self.priorities[j]))

        # 5) Verificar que no excedemos capacidades
        for i, used in workload.items():
            if used > self.capacities[i]:
                raise ValueError(f"Servidor {i} sobrecargado: "
                                 f"use {used} > cap {self.capacities[i]}")

        # 6) Ordenar detalles por prioridad descendente para validación
        details.sort(key=lambda x: -x[3])

        return {
            'assignments': assignments,
            'total_time': total_time,
            'workload': workload,
            'details': details
        }
