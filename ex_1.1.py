import heapq

def menor_caminho(mapa, origem):
    menor_distancia = {ponto: float('inf') for ponto in mapa}
    menor_distancia[origem] = 0
    
    fila_prioridade = [(0, origem)]
    
    while fila_prioridade:
        custo_atual, local_atual = heapq.heappop(fila_prioridade)
        
        if custo_atual > menor_distancia[local_atual]:
            continue
        
        for vizinho, custo in mapa[local_atual]:
            novo_custo = custo_atual + custo
            
            if novo_custo < menor_distancia[vizinho]:
                menor_distancia[vizinho] = novo_custo
                heapq.heappush(fila_prioridade, (novo_custo, vizinho))
    
    return menor_distancia

mapa = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

ponto_inicial = 'A'
resultado = menor_caminho(mapa, ponto_inicial)

for destino, custo in resultado.items():
    print(f"Menor distância até {destino}: {custo}")
