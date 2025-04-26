from hungarian_solver import HungarianSolver
from transportation_solver import TransportationSolver
from server_allocation import ServerAllocationSolver
from data_handler import DataHandler


def print_hungarian_result(assignments, cost_matrix):
    """
    Imprime en consola línea a línea:
      Programador X: Tarea Y (Coste Z)
    """
    print("Resultados del Módulo Húngaro:")
    for prog, tareas in assignments.items():
        for tarea in tareas:
            coste = cost_matrix[prog][tarea]
            # +1 para usar índices humanos (1…N en vez de 0…N-1)
            print(f"  Programador {prog+1}: Tarea {tarea+1} (Coste {coste})")
    print()  # línea en blanco al final


def main():
    Hdata = DataHandler.read_file('./data/input_hungarian.txt')
    n, m, cost_matrix = DataHandler.parse_hungarian(Hdata)
    # main.py (fragmento)
    hungarian = HungarianSolver(cost_matrix)
    assignments, total_cost = hungarian.solve()

    # PASAMOS cost_matrix en lugar de hungarian.original_matrix
    print_hungarian_result(assignments, cost_matrix)
    print(f"Costo Total Módulo Húngaro: {total_cost}\n")

    # Módulo de Transporte
    Tdata = DataHandler.read_file('./data/input_transportation.txt')
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
    Sdata = DataHandler.read_file('./data/input_server.txt')
    _, _, cost_matrix, capacities, priorities = DataHandler.parse_server_allocation(Sdata)
    server_allocation = ServerAllocationSolver(cost_matrix, capacities, priorities)
    assignments, total_time = server_allocation.solve()
    print("\n Módulo de Servidores")
    print(f"Asignaciones: {assignments}, Tiempo Total: {total_time}")

main()