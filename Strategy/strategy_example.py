from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Context():
    """
    O Context define a interface de interesse para os clientes.
    """

    def __init__(self, strategy: Strategy) -> None:
        """
        Normalmente, o Context aceita uma estratégia através do construtor, mas
        também fornece um setter para alterá-la em tempo de execução.
        """

        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        O Context mantém uma referência a um dos objetos Strategy. O
        Context não conhece a classe concreta de uma estratégia. Ele deve funcionar
        com todas as estratégias através da interface Strategy.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Normalmente, o Context permite substituir um objeto Strategy em tempo de execução.
        """

        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        """
        O Context delega algum trabalho para o objeto Strategy em vez de
        implementar várias versões do algoritmo por conta própria.
        """

        # ...

        print("Context: Ordenando dados usando a estratégia (não tenho certeza de como ela fará isso)")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))

        # ...


class Strategy(ABC):
    """
    A interface Strategy declara operações comuns a todas as versões suportadas
    de algum algoritmo.

    O Context usa essa interface para chamar o algoritmo definido por Estratégias Concretas.
    """

    @abstractmethod
    def do_algorithm(self, data: List):
        pass


"""
Estratégias Concretas implementam o algoritmo seguindo a interface base Strategy.
A interface as torna intercambiáveis no Context.
"""


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))


if __name__ == "__main__":
    # O código do cliente escolhe uma estratégia concreta e a passa para o contexto.
    # O cliente deve estar ciente das diferenças entre as estratégias para
    # fazer a escolha certa.

    context = Context(ConcreteStrategyA())
    print("Cliente: A estratégia está definida para ordenação normal.")
    context.do_some_business_logic()
    print()

    print("Cliente: A estratégia está definida para ordenação reversa.")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()
