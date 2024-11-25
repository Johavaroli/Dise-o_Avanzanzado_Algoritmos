# -*- coding: utf-8 -*-
"""
Spyder Editor

Johanna Vargas.

"""
import time
import heapq

# definimos la clase resolver
class PuzzleSolver:
    """
    Esta clase representa una solución al puzzle de las losetas.
    
    """
    def __init__(self, estado_inicial, estado_objetivo):
        # Inicialización del problema con el estado inicial y el estado objetivo.
        self.estado_inicial = estado_inicial
        self.estado_objetivo = estado_objetivo
        self.size = len(estado_inicial)
        # Las posibles movidas para cada casilla.
        self.moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def is_valid_move(self, row, col):
        """
       Este método verifica si el movimiento está dentro de los límites del tablero.
        
        """
        return 0 <= row < self.size and 0 <= col < self.size

    def generate_moves(self, state):
        """
        Este método genera los posibles movimientos a partir del estado actual.
        
        """
        zero_pos = [(i, row.index(0)) for i, row in enumerate(state) if 0 in row][0]
        for move in self.moves:
            new_row, new_col = zero_pos[0] + move[0], zero_pos[1] + move[1]
            if self.is_valid_move(new_row, new_col):
                yield (new_row, new_col)

    def apply_move(self, state, move):
        """
        Este método aplica un movimiento al estado actual para generar un nuevo estado.
        
        """
        row, col = move
        zero_pos = [(i, row.index(0)) for i, row in enumerate(state) if 0 in row][0]
        new_state = [list(row) for row in state]
        new_state[zero_pos[0]][zero_pos[1]], new_state[row][col] = new_state[row][col], new_state[zero_pos[0]][zero_pos[1]]
        return tuple(tuple(row) for row in new_state)

    def is_goal_state(self, state):
        """
        Este método verifica si el estado actual es el estado objetivo.
        
        """
        return state == self.estado_objetivo

    def solve(self):
        """
        Inicialización de variables para medir el tiempo y manejar la cola de prioridad.
        
        """
        start_time = time.time()
        priority_queue = [(0, self.estado_inicial, [])]
        visited_states = set()

        # Bucle principal de búsqueda.
        while priority_queue:
            cost, current_state, path = heapq.heappop(priority_queue)

        # Si se encuentra el estado objetivo, se imprime el tiempo, la solución y el número total de movimientos.
            if self.is_goal_state(current_state):
                end_time = time.time()
                print(f"la solución fue encontrada en: {end_time - start_time:.5f} segundos.")
                print(f"El número total de movimientos realizados fue: {len(path)}")

                return current_state

            # Si el estado ya fue visitado, se omite.
            if current_state in visited_states:
                continue

            # el estado actual se marca como visitado.
            visited_states.add(current_state)

            # En este segmento se generan los posibles movimientos y se agregan a la cola de prioridad.
            for move in self.generate_moves(current_state):
                new_state = self.apply_move(current_state, move)
                new_path = path + [move]
                heapq.heappush(priority_queue, (cost + 1, new_state, new_path))

                #  En este segmento se muestra el paso a paso de cada movimiento.
                print(f"\nMovimiento {len(new_path)}: Mueve la ficha de 0 a {move}")

                print_puzzle(new_state)

        #  En este segmento se imprime el mensaje si no se encuentra solución.
        print("No se encontró la solución.")
        return None

def print_puzzle(state):
    """
    Esta función imprime en el tablero el método más legible.
    
    """
    for row in state:
        print(row)

# Ejemplo de un puzzle inicial en desorden que muestra la solución:
initial_state = (
    (5, 7, 2, 0),
    (1,13, 3, 10),
    (9, 8, 11, 12),
    (6, 14, 15, 4)
)

goal_state = (
    (1, 2, 3, 4),
    (5, 6, 7, 8),
    (9, 10, 11, 12),
    (13, 14, 15, 0)
)

puzzle_solver = PuzzleSolver(initial_state, goal_state)
solution = puzzle_solver.solve()

if solution:
    print("\nSolución Final:")
    print_puzzle(solution)
