import heapq

def prim_mst(graph, start):
    mst = []
    visited = set()
    min_heap = [(0, start, None)]
    
    while min_heap:
        weight, current, previous = heapq.heappop(min_heap)
        
        if current in visited:
            continue
        
        visited.add(current)
        if previous is not None:
            mst.append((previous, current, weight))
        
        for neighbor, edge_weight in graph[current]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current))
    
    return mst

graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 3), ('B', 1), ('D', 5)],
    'D': [('B', 4), ('C', 5)]
}

mst = prim_mst(graph, 'A')
for u, v, w in mst:
    print(f"{u} - {v} com peso {w}")