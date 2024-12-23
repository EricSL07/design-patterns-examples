class SingletonMeta(type):
    """
    A classe Singleton pode ser implementada de diferentes maneiras em Python. Alguns
    métodos possíveis incluem: classe base, decorador, metaclasse. Usaremos a
    metaclasse porque é a mais adequada para este propósito.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possíveis alterações no valor do argumento `__init__` não afetam
        a instância retornada.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Finalmente, qualquer singleton deve definir alguma lógica de negócio, que pode ser
        executada em sua instância.
        """

        # ...


if __name__ == "__main__":
    # O código do cliente.

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton funciona, ambas as variáveis contêm a mesma instância.")
    else:
        print("Singleton falhou, as variáveis contêm instâncias diferentes.")