# app/utilities/file_processor.py

from collections import defaultdict, deque

def process_file(filepath):
    # Leer el archivo y construir el grafo
    with open(filepath, 'r') as file:
        lines = file.read().strip().split()
    
    graph = defaultdict(set)
    in_degree = defaultdict(int)

    # Construir el grafo y calcular los grados de entrada
    for line in lines:
        a, b, c = line[0], line[1], line[2]
        if b not in graph[a]:
            graph[a].add(b)
            in_degree[b] += 1
        if c not in graph[b]:
            graph[b].add(c)
            in_degree[c] += 1

        # Asegurarnos de que todos los caracteres están en el grado de entrada
        if a not in in_degree:
            in_degree[a] = 0
        if b not in in_degree:
            in_degree[b] = 0
        if c not in in_degree:
            in_degree[c] = 0

    # Aplicar ordenamiento topológico
    return topological_sort(graph, in_degree)

def topological_sort(graph, in_degree):
    # Inicializar la cola para el ordenamiento topológico
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    top_order = []

    while queue:
        node = queue.popleft()
        top_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(top_order) == len(in_degree):
        return ''.join(top_order)
    else:
        raise ValueError("There is a cycle in the graph, check the input data")
