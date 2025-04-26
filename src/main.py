from hungarian_solver import HungarianSolver
from transportation_solver import TransportationSolver
from server_allocation import ServerAllocationSolver
from data_handler import DataHandler

def main():
    # Ejemplo de uso para el módulo Húngaro
    Hdata = DataHandler.read_file('../data/input_hungarian.txt')
    _, _, cost_matrix = DataHandler.parse_hungarian(Hdata)
    hungarian = HungarianSolver(cost_matrix)
    assignments, cost = hungarian.solve()
    print("\n Módulo Húngaro")
    print(f"Asignaciones: {assignments}, Costo Total: {cost}")

    # Módulo de Transporte
    Tdata = DataHandler.read_file('../data/input_transportation.txt')
    _, _, cost_matrix, supply, demand = DataHandler.parse_transportation(Tdata)
    transportation = TransportationSolver(cost_matrix, supply, demand)

    # Puedes elegir entre: 'northwest', 'min_cost', 'vogel'
    method = 'vogel'
    solution, total_cost = transportation.solve(method=method)

    print(f"\n Módulo de Transporte ({method})")
    print("Asignación:")
    for i, row in enumerate(solution):
        print(f"  - Programador {i+1}: {row}")
    
    # Reporte detallado
    transportation.generate_detailed_report(solution)

    # Módulo de Asignación a Servidores
    Sdata = DataHandler.read_file('../data/input_server.txt')
    _, _, cost_matrix, capacities, priorities = DataHandler.parse_server_allocation(Sdata)
    server_allocation = ServerAllocationSolver(cost_matrix, capacities, priorities)
    assignments, total_time = server_allocation.solve()
    print("\n Módulo de Servidores")
    print(f"Asignaciones: {assignments}, Tiempo Total: {total_time}")

main()