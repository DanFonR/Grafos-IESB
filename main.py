from GrafoDenso import GrafoDenso
from GrafoEsparso import GrafoEsparso
from collections.abc import Callable
from typing import TextIO
from sys import stderr

if __name__ != "__main__":
    print(f"Execute {__file__} como main", file=stderr)
    exit(1)

def exec_all(*funcs: Callable[[None], None]) -> None:
    func: Callable[[None], None]

    for func in funcs:
        func()

def tee(exercicio: str) -> Callable[[None], None]:
    """
    Imprime tanto para um arquivo 
    (resultado.txt) quanto para o console
    """

    def intee(funcao_exercicio:
              Callable[[TextIO|None], None]) -> Callable[[None], None]:
        def wrapper() -> None:
            resultado: TextIO

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
def matriz_adj(file: TextIO|None=None) -> None:
    """
    Atividade 1

    Criacao de Grafo Denso, adicao de arestas, 
    exibicao de suas caracteristicas, remocao de uma aresta, 
    e exibicao de sua matriz de adjacencia
    """

    vertices: list[str] = list("ABCDE")
    arestas: list[tuple[str, str]] = [
        ("A", "B"), ("A", "C"), ("C", "D"),
        ("C", "E"), ("B", "D")
    ]
    aresta: tuple[str, str]

    grafo: GrafoDenso = GrafoDenso(vertices)

    for aresta in arestas:
        grafo.adicionar_aresta(aresta[0], aresta[1])
        print(f"Aresta adicionada entre {aresta[0]} e {aresta[1]}.",
              file=file)

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

    aresta_removida: tuple[str, str] = ("A", "C")

    grafo.remover_aresta(*aresta_removida)
    print(f"Aresta entre {aresta_removida[0]} e {aresta_removida[1]} "
          "removida", file=file)

    print("\nMatriz de Adjacencia:", file=file)
    grafo.imprimir(file=file)

@tee("Atividade 2")
def simples_nulo_completo(file: TextIO|None=None) -> None:
    """
    Atividade 2

    Metodos para determinar certas caracteristicas de um grafo:
        - Simples: sem ciclos ou mais de uma aresta por par de vertices
        - Nulo: existem arestas
        - Completo: grafo simples e todos os vertices possuem arestas entre si
    """

    denso: GrafoDenso = GrafoDenso(5)
    aresta: tuple[str, str]

    print("Matriz de Adjacencia:", file=file)
    denso.imprimir(file=file)

    print(
        f"\nSimples? {"Sim" if denso.is_simples() else "Nao"}",
        f"Nulo? {"Sim" if denso.is_nulo() else "Nao"}",
        f"Completo? {"Sim" if denso.is_completo() else "Nao"}\n",
        sep='\n',
        file=file
    )

    aresta = ("0", "2")
    denso.adicionar_aresta(*aresta)
    print(f"Aresta adicionada entre {aresta[0]} e {aresta[1]}\n", file=file)

    print("Matriz de Adjacencia:", file=file)
    denso.imprimir(file=file)

    print(
        f"\nSimples? {"Sim" if denso.is_simples() else "Nao"}",
        f"Nulo? {"Sim" if denso.is_nulo() else "Nao"}",
        f"Completo? {"Sim" if denso.is_completo() else "Nao"}\n",
        sep='\n',
        file=file
    )

    for i in map(tuple, ["01", "03", "04", "12", "13", "14", "23", "24", "34"]):
        denso.adicionar_aresta(*i)

    print("Matriz de Adjacencia:", file=file)
    denso.imprimir(file=file)

    print(
        f"\nSimples? {"Sim" if denso.is_simples() else "Nao"}",
        f"Nulo? {"Sim" if denso.is_nulo() else "Nao"}",
        f"Completo? {"Sim" if denso.is_completo() else "Nao"}\n",
        sep='\n',
        file=file
    )

    denso.adicionar_aresta("1", "1")

    print("Matriz de Adjacencia:", file=file)
    denso.imprimir(file=file)

    print(
        f"\nSimples? {"Sim" if denso.is_simples() else "Nao"}",
        f"Nulo? {"Sim" if denso.is_nulo() else "Nao"}",
        f"Completo? {"Sim" if denso.is_completo() else "Nao"}\n",
        sep='\n',
        file=file
    )

@tee("Atividade 3")
def subgrafos(file: TextIO|None=None) -> None:
    """
    Atividade 3

    
    """

    ...

@tee("Atividade 4")
def isomorfo(file: TextIO|None=None) -> None:
    """
    Atividade 4

    
    """

    ...

@tee("Atividade 5")
def colorir(file: TextIO|None=None) -> None:
    """
    Atividade 5

    Metodo para colorir um grafo usando _backtracking_. 
    Reporta quantidade de cores minima e a cor de cada vertice (inteiros 0-N)
    """

    denso: GrafoDenso = GrafoDenso(tuple("MACFQP"))
    arestas: list[tuple[str, str]] = [
        ("C", "F"), ("C", "A"), ("F", "A"), ("M", "P"),
        ("M", "A"), ("P", "A"), ("Q", "F")
    ]

    for aresta in arestas:
        denso.adicionar_aresta(*aresta)

    print("Matriz de Adjacencia", file=file)
    denso.imprimir(file=file)
    print(file=file)

    qtd_cores: int
    cores: dict[str, int]
    qtd_cores, cores = denso.colorir_grafo()

    print(f"\nnumero de cores: {qtd_cores}\n"
          f"cores: {cores}", file=file)

exec_all(
    matriz_adj,
    simples_nulo_completo,
    # subgrafos,
    # isomorfo,
    colorir
)
