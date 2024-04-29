# app/utilities/file_processor.py

from collections import defaultdict, deque

def validate_file_contents(filepath):
    """
    Valida que cada línea del archivo dado tenga exactamente tres caracteres numéricos.

      Esta función lee del archivo especificado y verifica cada línea para asegurarse de que contenga
      exactamente tres caracteres y que todos los caracteres sean dígitos. Esto se utiliza para validar
      el formato de los datos antes de procesarlos para extraer el código secreto.

      Parámetros:
      - filepath (str): Ruta al archivo a validar.

      Devoluciones:
      - bool: Verdadero si todas las líneas son válidas, Falso en caso contrario.
    """

    # Trata de abrir y leer el archivo
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()  # Lee todas las lineas del archivo
    except IOError as e:
        # Si hay un error de IO (por ejemplo, archivo no encontrado, problema de permiso), imprime el error y devuelva Falso
        print(f"Error al abrir o leer el archivo: {e}")
        return False

    # Iterar sobre cada línea leída del archivo
    for line in lines:
        stripped_line = line.strip()  # Elimine los espacios en blanco iniciales o finales
        
        # Comprueba si la línea tiene exactamente tres caracteres y todos son dígitos
        if len(stripped_line) != 3 or not stripped_line.isdigit():
            return False  # Si alguna línea no se ajusta, devuelve False inmediatamente

    # Si todas las líneas se ajustan al formato esperado, devuelve Verdadero
    return True

def process_file(filepath):

    """
   Procese el archivo para determinar el código secreto más corto de los intentos de inicio de sesión exitosos.

     Parámetros:
     - filepath (str): ruta al archivo que contiene los intentos de inicio de sesión.

     Devoluciones:
     - str: el código secreto más corto deducido del archivo.
    """
     
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
        raise ValueError("Hay un ciclo en el gráfico, verifique los datos de entrada.")