class HungarianSolver:
    def __init__(self, cost_matrix):
        self.cost_matrix = cost_matrix
        self.n = len(cost_matrix)
        self.m = len(cost_matrix[0]) if self.n > 0 else 0
        self.row_covered = [False] * self.n
        self.col_covered = [False] * self.m
        self.marked = [[0] * self.m for _ in range(self.n)]
        self.path = []

    def reduce_matrix(self):
        # Reducción de filas y columnas
        for i in range(self.n):
            min_val = min(self.cost_matrix[i])
            for j in range(self.m):
                self.cost_matrix[i][j] -= min_val

        for j in range(self.m):
            min_val = min(self.cost_matrix[i][j] for i in range(self.n))
            for i in range(self.n):
                self.cost_matrix[i][j] -= min_val

    def find_uncovered_zero(self):
        for i in range(self.n):
            for j in range(self.m):
                if self.cost_matrix[i][j] == 0 and not self.row_covered[i] and not self.col_covered[j]:
                    return (i, j)
        return (-1, -1)

    def solve(self):
        self.reduce_matrix()
        # Placeholder implementation
        assignments = {i: i for i in range(min(self.n, self.m))}  # Example: Assign each row to the same column
        total_cost = sum(self.cost_matrix[i][i] for i in range(min(self.n, self.m)))
        
        return assignments, total_cost