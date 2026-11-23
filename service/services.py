from entities.entity import Produto


class Services:

    def __init__(self, repository):
        self.repository = repository

    def create(self, nome, preco, quantidade):
        if not nome or not nome.strip():
            raise ValueError("O nome do produto é obrigatório.")

        if preco < 0:
            raise ValueError("O preço não pode ser negativo.")

        if type(quantidade) is not int or quantidade < 0:
            raise ValueError("A quantidade deve ser um inteiro não negativo.")

        produto = Produto(nome.strip(), preco, quantidade)
        return self.repository.create(produto)

    def list(self):
        return self.repository.find_all()

    def get(self, produto_id):
        if type(produto_id) is not int or produto_id <= 0:
            raise ValueError("Digite um ID válido.")

        produto = self.repository.find_by_id(produto_id)

        if not produto:
            raise ValueError(f"Produto com ID {produto_id} não existe.")

        return produto

    def update(self, produto_id, nome, preco, quantidade):
        if not nome or not nome.strip():
            raise ValueError("O nome do produto é obrigatório.")

        if preco < 0:
            raise ValueError("O preço não pode ser negativo.")

        if type(quantidade) is not int or quantidade < 0:
            raise ValueError("A quantidade deve ser um inteiro não negativo.")

        produto = self.get(produto_id)

        produto.nome = nome.strip()
        produto.preco = preco
        produto.quantidade = quantidade

        if not self.repository.update(produto):
            raise ValueError(f"Produto com ID {produto_id} não existe.")

    def delete(self, produto_id):
        self.get(produto_id)

        if not self.repository.delete(produto_id):
            raise ValueError(f"Produto com ID {produto_id} não existe.")