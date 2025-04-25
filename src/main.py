from hungarian_solver import HungarianSolver
from transportation_solver import TransportationSolver
from server_allocation import ServerAllocationSolver
from data_handler import DataHandler

def main():
    # Ejemplo de uso para el módulo Húngaro
    data = DataHandler.read_file('data/input_hungarian.txt')
    n, m, cost_matrix = DataHandler.parse_hungarian(data)
    hungarian = HungarianSolver(cost_matrix)
    assignments, cost = hungarian.solve()
    print(f"Asignaciones: {assignments}, Costo Total: {cost}")

if __name__ == "__main__":
    main()