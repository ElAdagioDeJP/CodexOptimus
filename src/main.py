from hungarian_solver import HungarianSolver
from transportation_solver import TransportationSolver
from server_allocation import ServerAllocationSolver
from data_handler import DataHandler

def main():
    # Ejemplo de uso para el módulo Húngaro
    Hdata = DataHandler.read_file('../data/input_hungarian.txt')
    cost_matrix = DataHandler.parse_hungarian(Hdata)
    hungarian = HungarianSolver(cost_matrix)
    assignments, cost = hungarian.solve()
    print(f"Asignaciones: {assignments}, Costo Total: {cost}")

    Tdata = DataHandler.read_file('../data/input_transportation.txt')
    cost_matrix, supply, demand = DataHandler.parse_transportation(Tdata)
    transportation = TransportationSolver(cost_matrix, supply, demand)
    initial_solution, total_cost = transportation.solve(method='northwest')
    print(f"Solución Inicial: {initial_solution}, Costo Total: {total_cost}")

    Sdata = DataHandler.read_file('../data/input_server.txt')
    cost_matrix, capacities, priorities = DataHandler.parse_server_allocation(Sdata)
    server_allocation = ServerAllocationSolver(cost_matrix, capacities, priorities)
    assignments, total_time = server_allocation.solve()
    print(f"Asignaciones: {assignments}, Tiempo Total: {total_time}")

main()