from abc import ABC, abstractmethod

class Grafo(ABC):
    @abstractmethod
    def numero_de_vertices(self) -> int:
        pass

    @abstractmethod
    def numero_de_arestas(self) -> int:
        pass

    @abstractmethod
    def sequencia_de_graus(self) -> list[int]:
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

    @abstractmethod
    def is_simples(self) -> bool:
        pass

    @abstractmethod
    def is_nulo(self) -> bool:
        pass

    @abstractmethod
    def is_completo(self) -> bool:
        pass

    @abstractmethod
    def get_vertices(self) -> list[str]:
        pass

    @abstractmethod
    def get_arestas(self) -> list[tuple[str, str]]:
        pass

    @abstractmethod
    def is_subgrafo(self, outro_grafo) -> bool:
        pass

    @abstractmethod
    def is_subgrafo_gerador(self, outro_grafo) -> bool:
        pass

    @abstractmethod
    def is_subgrafo_induzido(self, outro_grafo) -> bool:
        pass
