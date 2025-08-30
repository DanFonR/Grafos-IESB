from GrafoDenso import GrafoDenso

if __name__ != "__main__":
    print(f"Execute {__file__} as main (on cli: python {__file__})")
    exit(1)

def matriz_adj():
    vertices: list[str] = list("ABCDE")
    arestas: list[tuple[str]] = [
        ("A", "B"), ("A", "C"), ("C", "D"),
        ("C", "E"), ("B", "D")
    ]

    grafo = GrafoDenso(vertices)

    for aresta in arestas:
        grafo.adicionar_aresta(aresta[0], aresta[1])
        print(f"Aresta adicionada entre {aresta[0]} e {aresta[1]}.")

    print("\nMatriz de Adjacencia:")
    grafo.imprimir()
    print()
    print(
        f"Numero de vertices: {grafo.numero_de_vertices()}",
        f"Numero de arestas: {grafo.numero_de_arestas()}",
        f"Sequencia de graus: {grafo.sequencia_de_graus()}",
        sep='\n'
    )

    aresta_removida: tuple[str] = ("A", "C")

    grafo.remover_aresta(*aresta_removida)
    print(f"Aresta removida entre {aresta_removida[0]} e {aresta_removida[1]}.")

    print("\nMatriz de Adjacencia:")
    grafo.imprimir()

def simples_nulo_completo():
    ...

def subgrafos():
    ...