class TransportationSolver:
    def __init__(self, cost_matrix, supply, demand):
        self.cost_matrix = cost_matrix
        self.supply = supply
        self.demand = demand
        self.n = len(supply)
        self.m = len(demand)
        self.validate_data()

    # Metodo para validar los datos de entrada
    def validate_data(self):
        if sum(self.supply) < sum(self.demand):
            raise ValueError("La oferta total debe ser mayor o igual a la demanda.")

    # Metodo de Esquina Noroeste
    def northwest_corner(self):
        solution = [[0] * self.m for _ in range(self.n)]
        i = j = 0
        while i < self.n and j < self.m:
            quantity = min(self.supply[i], self.demand[j])
            solution[i][j] = quantity
            self.supply[i] -= quantity
            self.demand[j] -= quantity
            if self.supply[i] == 0:
                i += 1
            else:
                j += 1
        return solution
    
    # Método: Costo Mínimo
    def minimum_cost_method(self):
        supply = self.supply.copy()
        demand = self.demand.copy()
        cost = [row.copy() for row in self.cost_matrix]
        solution = [[0] * self.m for _ in range(self.n)]

        while any(s > 0 for s in supply) and any(d > 0 for d in demand):
            min_cost = float('inf')
            min_cell = (-1, -1)

            for i in range(self.n):
                for j in range(self.m):
                    if supply[i] > 0 and demand[j] > 0 and cost[i][j] < min_cost:
                        min_cost = cost[i][j]
                        min_cell = (i, j)

            i, j = min_cell
            quantity = min(supply[i], demand[j])
            solution[i][j] = quantity
            supply[i] -= quantity
            demand[j] -= quantity

        return solution

    # Método: Aproximación de Vogel
    def vogel_approximation_method(self):
        supply = self.supply.copy()
        demand = self.demand.copy()
        cost = [row.copy() for row in self.cost_matrix]
        solution = [[0] * self.m for _ in range(self.n)]

        while any(s > 0 for s in supply) and any(d > 0 for d in demand):
            penalties = []

            # Penalizaciones de filas
            for i in range(self.n):
                if supply[i] > 0:
                    row = [(cost[i][j], j) for j in range(self.m) if demand[j] > 0]
                    if len(row) >= 2:
                        row.sort()
                        penalty = row[1][0] - row[0][0]
                    elif len(row) == 1:
                        penalty = row[0][0]
                    else:
                        continue
                    penalties.append(('row', i, penalty))

            # Penalizaciones de columnas
            for j in range(self.m):
                if demand[j] > 0:
                    col = [(cost[i][j], i) for i in range(self.n) if supply[i] > 0]
                    if len(col) >= 2:
                        col.sort()
                        penalty = col[1][0] - col[0][0]
                    elif len(col) == 1:
                        penalty = col[0][0]
                    else:
                        continue
                    penalties.append(('col', j, penalty))

            penalties.sort(key=lambda x: -x[2])
            kind, index, _ = penalties[0]

            if kind == 'row':
                i = index
                min_cost = float('inf')
                j_selected = -1
                for j in range(self.m):
                    if demand[j] > 0 and cost[i][j] < min_cost:
                        min_cost = cost[i][j]
                        j_selected = j
                j = j_selected
            else:
                j = index
                min_cost = float('inf')
                i_selected = -1
                for i in range(self.n):
                    if supply[i] > 0 and cost[i][j] < min_cost:
                        min_cost = cost[i][j]
                        i_selected = i
                i = i_selected

            quantity = min(supply[i], demand[j])
            solution[i][j] = quantity
            supply[i] -= quantity
            demand[j] -= quantity

        return solution

    # Cálculo del costo total
    def calculate_total_cost(self, solution):
        return sum(solution[i][j] * self.cost_matrix[i][j] for i in range(self.n) for j in range(self.m))

    # Solución principal
    def solve(self, method='northwest'):
        if method == 'northwest':
            initial_solution = self.northwest_corner()
        elif method == 'min_cost':
            initial_solution = self.minimum_cost_method()
        elif method == 'vogel':
            initial_solution = self.vogel_approximation_method()
        else:
            raise ValueError("Método no reconocido. Usa 'northwest', 'min_cost' o 'vogel'.")
        
        return initial_solution, self.calculate_total_cost(initial_solution)

    # Reporte detallado
    def generate_detailed_report(self, solution):
        print("\n Reporte Detallado de Asignación:")
        total_cost = 0
        for i in range(self.n):
            for j in range(self.m):
                if solution[i][j] > 0:
                    cost = self.cost_matrix[i][j]
                    subtotal = cost * solution[i][j]
                    total_cost += subtotal
                    print(f"  - Programador {i+1} → Tarea {j+1} | {solution[i][j]} unidad(es) x Costo {cost} = {subtotal}")
        print(f"\n Costo Total Confirmado: {total_cost}")
