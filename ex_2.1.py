def mochila_gulosa(itens, capacidade):
    itens.sort(key=lambda x: x[1] / x[0], reverse=True)

    peso_total = 0
    valor_total = 0
    itens_selecionados = []

    for peso, valor, nome in itens:
        if peso_total + peso <= capacidade:
            itens_selecionados.append(nome)
            peso_total += peso
            valor_total += valor

    return itens_selecionados, valor_total

itens = [
    (2, 40, "item1"),
    (3, 50, "item2"),
    (5, 100, "item3"),
    (4, 90, "item4")
]

capacidade_mochila = 8
selecionados, valor_maximo = mochila_gulosa(itens, capacidade_mochila)

print(f"Itens selecionados: {selecionados}")
print(f"Valor total: {valor_maximo}")
