from service.services import Services


class UI:

    def __init__(self, services):
        self.services = services

    def show_principal_menu(self):
        while True:
            print("\n===== MENU DE PRODUTOS =====")
            print("(1) Cadastrar produto")
            print("(2) Listar produtos")
            print("(3) Consultar produto")
            print("(4) Atualizar produto")
            print("(5) Excluir produto")
            print("(0) Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.cadastrar_produto()
            elif opcao == "2":
                self.listar_produtos()
            elif opcao == "3":
                self.consultar_produto()
            elif opcao == "4":
                self.atualizar_produto()
            elif opcao == "5":
                self.excluir_produto()
            elif opcao == "0":
                print("Encerrando o sistema...")
                break
            else:
                print("Opção inválida!")

    def cadastrar_produto(self):
        print("\n--- Cadastrar Produto ---")

        try:
            nome = input("Nome: ")
            preco = float(input("Preço: ").replace(",", "."))
            quantidade = int(input("Quantidade: "))

            produto = self.services.create(nome, preco, quantidade)
            print(f"Produto cadastrado com sucesso! ID: {produto.id}")

        except ValueError as e:
            print(f"Erro: {e}")

    def listar_produtos(self):
        print("\n--- Lista de Produtos ---")

        produtos = self.services.list()

        if not produtos:
            print("Nenhum produto cadastrado.")
            return

        for produto in produtos:
            print(
                f"ID: {produto.id} | "
                f"Nome: {produto.nome} | "
                f"Preço: R$ {produto.preco:.2f} | "
                f"Quantidade: {produto.quantidade}"
            )

    def consultar_produto(self):
        print("\n--- Consultar Produto ---")

        try:
            produto_id = int(input("ID: "))
            produto = self.services.get(produto_id)

            print(f"ID: {produto.id}")
            print(f"Nome: {produto.nome}")
            print(f"Preço: R$ {produto.preco:.2f}")
            print(f"Quantidade: {produto.quantidade}")

        except ValueError as e:
            print(f"Erro: {e}")

    def atualizar_produto(self):
        print("\n--- Atualizar Produto ---")

        try:
            produto_id = int(input("ID: "))
            produto = self.services.get(produto_id)

            print(f"Produto encontrado: {produto.nome}")

            nome = input("Novo nome: ")
            preco = float(input("Novo preço: ").replace(",", "."))
            quantidade = int(input("Nova quantidade: "))

            self.services.update(produto_id, nome, preco, quantidade)
            print("Produto atualizado com sucesso!")

        except ValueError as e:
            print(f"Erro: {e}")

    def excluir_produto(self):
        print("\n--- Excluir Produto ---")

        try:
            produto_id = int(input("ID: "))
            produto = self.services.get(produto_id)

            print(f"Produto: {produto.nome}")
            print(f"Preço: R$ {produto.preco:.2f}")
            print(f"Quantidade: {produto.quantidade}")

            confirmacao = input("Deseja excluir? (s/n): ")

            if confirmacao.lower() == "s":
                self.services.delete(produto_id)
                print("Produto excluído com sucesso!")
            else:
                print("Exclusão cancelada.")

        except ValueError as e:
            print(f"Erro: {e}")