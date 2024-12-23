class Target:
    """
    O Target define a interface específica do domínio usada pelo código do cliente.
    """

    def request(self) -> str:
        return "Target: O comportamento padrão do target."


class Adaptee:
    """
    O Adaptee contém algum comportamento útil, mas sua interface é incompatível
    com o código do cliente existente. O Adaptee precisa de alguma adaptação antes
    que o código do cliente possa usá-lo.
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    """
    O Adapter torna a interface do Adaptee compatível com a interface do Target
    via herança múltipla.
    """

    def request(self) -> str:
        return f"Adapter: (TRADUZIDO) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    """
    O código do cliente suporta todas as classes que seguem a interface Target.
    """

    print(target.request(), end="")


if __name__ == "__main__":
    print("Cliente: Eu posso trabalhar bem com os objetos Target:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Cliente: A classe Adaptee tem uma interface estranha. "
          "Veja, eu não entendo isso:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Cliente: Mas eu posso trabalhar com ela através do Adapter:")
    adapter = Adapter()
    client_code(adapter)