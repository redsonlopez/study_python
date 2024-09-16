class Dados:
    """permite a criação de uma estrutura para gravar dados"""

    def __init__(self):
        self.itens = []

    def __repr__(self):
        return str(self.itens)

    def insere(self, valor):
        """ adiciona itens a sua lista de dados"""

        self.itens.append(valor)

    def remove(self):

        # modifica o valor do último item
        self.itens.pop()


def main():

    # cria um novo objeto do tipo Dados
    dados = Dados()

    # adicionando itens
    dados.insere(1)
    dados.insere(2)
    dados.insere(3)  # último item adicionado

    print(dados)  # [1, 2, 3]

    # removendo itens
    dados.remove()

    print(dados)  # [1, 2]


if __name__ == "__main__":
    main()

