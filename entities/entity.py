class Produto:
    def __init__(
        self,
        nome: str,
        preco: float,
        quantidade: int,
        id: int | None = None,
    ):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade