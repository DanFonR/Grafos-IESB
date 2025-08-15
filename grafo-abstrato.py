from abc import ABC, abstractmethod

class Grafo(ABC):
    @abstractmethod
    def numero_de_vertices(self) -> int:
        pass

    @abstractmethod
    def numero_de_arestas(self) -> int:
        pass

    @abstractmethod
    def sequencia_de_graus(self) -> list:
        pass

    @abstractmethod
    def adicionar_aresta(self, u, v) -> None:
        pass

    @abstractmethod
    def remover_aresta(self, u, v) -> None:
        pass

    @abstractmethod
    def imprimir(self) -> None:
        pass
