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