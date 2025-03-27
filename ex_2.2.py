import math

def distancia(cidade1, cidade2):
    x1, y1 = cidade1
    x2, y2 = cidade2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def tsp_vizinho_mais_proximo(cidades, inicio):
    nao_visitadas = set(cidades.keys())
    rota = [inicio]
    nao_visitadas.remove(inicio)

    cidade_atual = inicio

    while nao_visitadas:
        proxima_cidade = min(nao_visitadas, key=lambda cidade: distancia(cidades[cidade_atual], cidades[cidade]))
        rota.append(proxima_cidade)
        nao_visitadas.remove(proxima_cidade)
        cidade_atual = proxima_cidade

    return rota

cidades = {
    "A": (0, 0),
    "B": (1, 5),
    "C": (5, 2),
    "D": (6, 6),
    "E": (8, 3)
}

cidade_inicial = "A"
rota = tsp_vizinho_mais_proximo(cidades, cidade_inicial)

print(f"Rota encontrada: {' -> '.join(rota)}")
