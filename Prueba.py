from collections import deque

# Definición del grafo
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


def bfs(graph, start):
    # Crear una cola para los nodos que necesitan ser explorados
    queue = deque([start])
    # Crear un conjunto para rastrear los nodos visitados
    visited = set([start])

    # Lista para mantener el orden de visita de los nodos
    result = []

    while queue:
        # Extraer el nodo actual de la cola
        current = queue.popleft()
        result.append(current)

        # Explorar todos los vecinos del nodo actual
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


# Ejecución de la búsqueda por anchura desde el nodo 'A'
visited_order = bfs(graph, 'A')
print("Nodos visitados en orden:", visited_order)