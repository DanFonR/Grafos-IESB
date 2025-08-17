from Grafo import Grafo
from collections.abc import Iterable

class GrafoDenso(Grafo):
    __matriz: list[list[int]]
    __rotulos: dict[int|str, int]

    def __init__(self, vertices:int|Iterable[str]):
        if not isinstance(vertices, (int, Iterable)):
            raise TypeError("Tipo invalido")

        if isinstance(vertices, int):
            self.__rotulos = {i: i for i in range(vertices)}
        else:
            self.__rotulos = {
                rotulo: indice
                for (indice, rotulo) in enumerate(vertices)
            }

        qtd_arestas: int = len(self.__rotulos)

        self.__matriz = [[0 for j in range(qtd_arestas)]
                         for i in range(qtd_arestas)]

    def adicionar_aresta(self, u: int|str, v: int|str) -> None:
        self.__definir_valor_aresta(u, v, valor=1)

    def remover_aresta(self, u: int|str, v: int|str) -> None:
        self.__definir_valor_aresta(u, v, valor=0)

    def numero_de_arestas(self) -> int:
        return sum(
            self.__matriz[i][j] for i in range(len(self.__rotulos))
            for j in range(i, len(self.__rotulos))
        )

    def numero_de_vertices(self) -> int:
        return len(self.__rotulos)

    def sequencia_de_graus(self) -> list[int]:
        return sorted(
            [sum(1 for i in j if i) for j in self.__matriz]
        )

    def imprimir(self) -> None:
        valores_str: list[str]
        rotulos: list[str] = [str(i) for i in self.__rotulos.keys()]
        header: str = (" " * max(len(i) for i in rotulos)
                       + " | " + " | ".join(rotulos))

        print(header)
        print("-" * len(header))

        for (rotulo, valor) in self.__rotulos.items():
            valores_str = [str(i) for i in self.__matriz[valor]]

            print(f"{rotulo} | "
                  + " | ".join(valores_str))

    def __definir_valor_aresta(
            self, u: int|str, v: int|str, valor: int) -> None:
        if not isinstance(u, (int, str)) or not isinstance(v, (int, str)):
            raise TypeError("")

        U: int = self.__rotulos.get(u)
        V: int = self.__rotulos.get(v)

        if U == None or V == None:
            raise IndexError("Vertice nao existe")

        self.__matriz[U][V] = self.__matriz[V][U] = valor
