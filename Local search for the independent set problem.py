import random

def local_search_independent_set(graph):
    # Начинаем со случайного независимого множества
    vertices = list(graph.keys())
    current_set = set()
    
    # Создаем случайное начальное независимое множество
    random.shuffle(vertices)
    for vertex in vertices:
        # Проверяем, можно ли добавить вершину без нарушения независимости
        can_add = True
        for neighbor in graph[vertex]:
            if neighbor in current_set:
                can_add = False
                break
        if can_add:
            current_set.add(vertex)
    
    improved = True
    while improved:
        improved = False
        
        # Пытаемся добавлять вершины, если они не смежны с текущим множеством
        random.shuffle(vertices)
        for vertex in vertices:
            if vertex not in current_set:
                # Проверяем, что вершина не смежна ни с одной вершиной в текущем множестве
                can_add = True
                for neighbor in graph[vertex]:
                    if neighbor in current_set:
                        can_add = False
                        break
                
                if can_add:
                    current_set.add(vertex)
                    improved = True
    
    return current_set

# Граф с 12 вершинами
graph = {
    0: [1, 2, 3],
    1: [0, 4, 5],
    2: [0, 3, 6],
    3: [0, 2, 7],
    4: [1, 5, 8],
    5: [1, 4, 9],
    6: [2, 7, 10],
    7: [3, 6, 11],
    8: [4, 9],
    9: [5, 8, 10],
    10: [6, 9, 11],
    11: [7, 10]
}

# Запускаем локальный поиск
independent_set = local_search_independent_set(graph)

# Выводим результат
print("Найденное независимое множество:", sorted(independent_set))
print("Размер независимого множества:", len(independent_set))

# Проверка корректности
def verify_independent_set(graph, solution):
    for vertex in solution:
        for neighbor in graph[vertex]:
            if neighbor in solution:
                return False
    return True

print("Множество корректно:", verify_independent_set(graph, independent_set))
вывод:
Найденное независимое множество: [0, 4, 6, 8, 11]
Размер независимого множества: 5
Множество корректно: True
