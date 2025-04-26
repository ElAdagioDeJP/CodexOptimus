from hungarian_solver import HungarianSolver
from transportation_solver import TransportationSolver
from server_allocation import ServerAllocationSolver
from data_handler import DataHandler


def print_hungarian_result(assignments, cost_matrix):
    print("Resultados del Módulo Húngaro:")
    for prog, tareas in assignments.items():
        for tarea in tareas:
            coste = cost_matrix[prog][tarea]
            print(f"  Programador {prog+1}: Tarea {tarea+1} (Coste {coste})")
    print()


def print_transportation_result(solution, total_cost, method):
    print(f"\nMódulo de Transporte ({method}):")
    print("Asignación:")
    for i, row in enumerate(solution):
        print(f"  - Programador {i+1}: {row}")
    print(f"Costo Total Módulo de Transporte: {total_cost}\n")
    # Generar reporte detallado si está disponible


def print_server_allocation_result(results):
    assignments = results['assignments']
    total_time = results['total_time']
    workload = results['workload']
    details = results['details']

    print("\nMódulo de Servidores:")
    print("Asignaciones óptimas de solicitudes a servidores:")
    for req, serv in assignments.items():
        print(f"  - Solicitud {req+1} -> Servidor {serv+1}")

    print(f"Tiempo Total de procesamiento: {total_time}\n")
    print("Carga de trabajo por servidor:")
    for serv, load in workload.items():
        print(f"  - Servidor {serv+1}: {load} solicitudes")

    print("\nDetalles por prioridad (descendente):")
    for req, serv, cost, priority in details:
        print(f"  Solicitud {req+1} (Prioridad {priority}): Servidor {serv+1}, Coste {cost}")
    print()


def main():
    # Módulo Húngaro
    Hdata = DataHandler.read_file('./data/input_hungarian.txt')
    _, _, cost_matrix_h = DataHandler.parse_hungarian(Hdata)
    hungarian = HungarianSolver(cost_matrix_h)
    assignments_h, total_cost_h = hungarian.solve()
    print_hungarian_result(assignments_h, cost_matrix_h)
    print(f"Costo Total Módulo Húngaro: {total_cost_h}\n")

    # Módulo de Transporte
    Tdata = DataHandler.read_file('./data/input_transportation.txt')
    _, _, cost_matrix_t, supply, demand = DataHandler.parse_transportation(Tdata)
    transportation = TransportationSolver(cost_matrix_t, supply, demand)
    method = 'vogel'  # opciones: 'northwest', 'min_cost', 'vogel'
    solution_t, total_cost_t = transportation.solve(method=method)
    print_transportation_result(solution_t, total_cost_t, method)
    transportation.generate_detailed_report(solution_t)

    # Módulo de Asignación a Servidores
    Sdata = DataHandler.read_file('./data/input_server.txt')
    _, _, cost_matrix_s, capacities, priorities = DataHandler.parse_server_allocation(Sdata)
    server_allocation = ServerAllocationSolver(cost_matrix_s, capacities, priorities)
    results_s = server_allocation.solve()
    print_server_allocation_result(results_s)

if __name__ == '__main__':
    main()
