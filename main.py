from GrafoDenso import GrafoDenso
from sys import stderr

if __name__ != "__main__":
    print(f"Execute {__file__} como main", file=stderr)
    exit(1)

def tee(exercicio: str): # imprime tanto para arquivo quanto para console
    def intee(funcao_exercicio):
        def wrapper():
            with open("resultado.txt", "w") as resultado:
                print(f"{exercicio}".center(20, '-'), file=resultado)
                print(file=resultado)
                funcao_exercicio(file=resultado)
                print("\n", file=resultado)

            print(f"{exercicio}".center(20, '-'))
            print()
            funcao_exercicio()
            print("\n")
        return wrapper
    return intee

@tee("Atividade 1")
def matriz_adj(file=None) -> None:
    """Atividade 1"""

    vertices: list[str] = list("ABCDE")
    arestas: list[tuple[str]] = [
        ("A", "B"), ("A", "C"), ("C", "D"),
        ("C", "E"), ("B", "D")
    ]

    grafo = GrafoDenso(vertices)

    for aresta in arestas:
        grafo.adicionar_aresta(aresta[0], aresta[1])
        print(f"Aresta adicionada entre {aresta[0]} e {aresta[1]}.", file=file)

    print("\nMatriz de Adjacencia:", file=file)
    grafo.imprimir(file=file)
    print(file=file)
    print(
        f"Numero de vertices: {grafo.numero_de_vertices()}",
        f"Numero de arestas: {grafo.numero_de_arestas()}",
        f"Sequencia de graus: {grafo.sequencia_de_graus()}",
        sep='\n',
        file=file
    )

    aresta_removida: tuple[str] = ("A", "C")

    grafo.remover_aresta(*aresta_removida)
    print(f"Aresta entre {aresta_removida[0]} e {aresta_removida[1]} "
          "removida", file=file)

    print("\nMatriz de Adjacencia:", file=file)
    grafo.imprimir(file=file)

@tee("Atividade 2")
def simples_nulo_completo(file=None) -> None:
    """Atividade 2"""
    ...

@tee("Atividade 3")
def subgrafos(file=None) -> None:
    """Atividade 3"""
    ...

@tee("Atividade 4")
def isomorfo(file=None) -> None:
    """Atividade 4"""
    ...

matriz_adj()
