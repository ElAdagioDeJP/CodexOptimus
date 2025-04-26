class DataHandler:
    @staticmethod
    def read_file(filename):
        with open(filename, 'r') as file:
            data = file.readlines()
        return [list(map(int, line.strip().split())) for line in data]

    @staticmethod
    def parse_hungarian(data):
        n = data[0][0]
        m = data[0][1]
        cost_matrix = data[1:n+1]
        return n, m, cost_matrix
    
    @staticmethod
    def parse_transportation(data):
        n = data[0][0]
        m = data[0][1]
        cost_matrix = data[1:n+1]
        supply = data[n+1][0:m]
        demand = data[n+2][0:m]
        return n, m, cost_matrix, supply, demand
    
    @staticmethod
    def parse_server_allocation(data):
        s = data[0][0]
        r = data[0][1]
        cost_matrix = data[1:s+1]
        capacities = data[s+1][0:s]
        priorities = data[s+2][0:r]
        return s, r, cost_matrix, capacities, priorities
