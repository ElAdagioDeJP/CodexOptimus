class ServerAllocationSolver:
    def __init__(self, cost_matrix, capacities, priorities):
        self.cost_matrix = cost_matrix
        self.capacities = capacities
        self.priorities = priorities
        self.s = len(capacities)
        self.r = len(priorities)

    def solve(self):
        sorted_requests = sorted(enumerate(self.priorities), key=lambda x: -x[1])
        remaining_capacities = self.capacities.copy()
        assignments = {}
        total_time = 0

        for req_idx, _ in sorted_requests:
            min_cost = float('inf')
            selected_server = -1
            for server_idx in range(self.s):
                if remaining_capacities[server_idx] > 0 and self.cost_matrix[server_idx][req_idx] < min_cost:
                    min_cost = self.cost_matrix[server_idx][req_idx]
                    selected_server = server_idx
            if selected_server == -1:
                raise ValueError("No hay servidor disponibles.")
            assignments[req_idx] = selected_server
            remaining_capacities[selected_server] -= 1
            total_time += min_cost

        return assignments, total_time