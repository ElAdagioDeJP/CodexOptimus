class TransportationSolver:
    def __init__(self, cost_matrix, supply, demand):
        self.cost_matrix = cost_matrix
        self.supply = supply
        self.demand = demand
        self.n = len(supply)
        self.m = len(demand)
        self.validate_data()

    def validate_data(self):
        if sum(self.supply) < sum(self.demand):
            raise ValueError("La oferta total debe ser mayor o igual a la demanda.")

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

    def calculate_total_cost(self, solution):
        return sum(solution[i][j] * self.cost_matrix[i][j] for i in range(self.n) for j in range(self.m))

    def solve(self, method='northwest'):
        if method == 'northwest':
            initial_solution = self.northwest_corner()
        # Implementar otros métodos...
        return initial_solution, self.calculate_total_cost(initial_solution)