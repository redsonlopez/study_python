from random import choice


class Filhos:
    def __init__(self):
        # cria uma lista Python vazia
        self._vertices = list()

    def inserir(self, dado):
        vertice_novo = Vertice(dado)
        self._vertices.append(vertice_novo)
        return vertice_novo

    @property
    def quantidade(self):
        return len(self._vertices)

    def obter_filho(self, indice):
        # indice é valor 1 a quantidade de filhos
        # no entanto, as listas de python começam em 0
        # entao subtraimos 1
        return self._vertices[indice-1]


class Vertice:
    """
    Vertice de Arvore N-aria
    """
    def __init__(self, dado):
        # dado propriamente dito, conteúdo do vértice
        self.dado = dado
        # classe para instanciar filhos do vértice
        self.filhos = None

    def __str__(self):
        return str(self.dado)

    def inserir_filho(self, dado):
        """
        Inserir um filho no vértice atual
        """
        if self.filhos is None:
            self.filhos = Filhos()
        return self.filhos.inserir(dado)

    def obter_filho(self, indice):
        return self.filhos.obter_filho(indice)

    @property
    def quantidade_de_filhos(self):
        if self.filhos is None:
            return 0
        return self.filhos.quantidade


def obter_pontuacao_aleatoria():
    return choice([50, 90, 150, 300])


# criacao de objetos da classe Vertice
inicio = Vertice("Inicio")

# NÍVEL 1
vertice_a = inicio.inserir_filho(obter_pontuacao_aleatoria())
vertice_b = inicio.inserir_filho(obter_pontuacao_aleatoria())
vertice_c = inicio.inserir_filho(obter_pontuacao_aleatoria())

vertice_A1 = vertice_a.inserir_filho(obter_pontuacao_aleatoria())
vertice_A2 = vertice_a.inserir_filho(obter_pontuacao_aleatoria())
vertice_A3 = vertice_a.inserir_filho(obter_pontuacao_aleatoria())

vertice_B1 = vertice_b.inserir_filho(obter_pontuacao_aleatoria())
vertice_B2 = vertice_b.inserir_filho(obter_pontuacao_aleatoria())
vertice_B3 = vertice_b.inserir_filho(obter_pontuacao_aleatoria())

vertice_C1 = vertice_c.inserir_filho(obter_pontuacao_aleatoria())
vertice_C2 = vertice_c.inserir_filho(obter_pontuacao_aleatoria())
vertice_C3 = vertice_c.inserir_filho(obter_pontuacao_aleatoria())

s1 = vertice_A2.inserir_filho(obter_pontuacao_aleatoria())
s2 = vertice_A2.inserir_filho(obter_pontuacao_aleatoria())
s3 = vertice_A3.inserir_filho(obter_pontuacao_aleatoria())
s4 = vertice_A3.inserir_filho(obter_pontuacao_aleatoria())
s5 = vertice_B1.inserir_filho(obter_pontuacao_aleatoria())
s6 = vertice_B1.inserir_filho(obter_pontuacao_aleatoria())
s7 = vertice_B2.inserir_filho(obter_pontuacao_aleatoria())
s8 = vertice_B2.inserir_filho(obter_pontuacao_aleatoria())
s9 = vertice_C1.inserir_filho(obter_pontuacao_aleatoria())
s10 = vertice_C1.inserir_filho(obter_pontuacao_aleatoria())
s11 = vertice_C3.inserir_filho(obter_pontuacao_aleatoria())
s12 = vertice_C3.inserir_filho(obter_pontuacao_aleatoria())

s14 = s1.inserir_filho(obter_pontuacao_aleatoria())
s15 = s1.inserir_filho(obter_pontuacao_aleatoria())

s16 = s4.inserir_filho(obter_pontuacao_aleatoria())
s17 = s4.inserir_filho(obter_pontuacao_aleatoria())

s18 = s5.inserir_filho(obter_pontuacao_aleatoria())
s19 = s5.inserir_filho(obter_pontuacao_aleatoria())

s20 = s7.inserir_filho(obter_pontuacao_aleatoria())
s21 = s7.inserir_filho(obter_pontuacao_aleatoria())

s22 = s10.inserir_filho(obter_pontuacao_aleatoria())
s23 = s10.inserir_filho(obter_pontuacao_aleatoria())

s24 = s11.inserir_filho(obter_pontuacao_aleatoria())
s25 = s11.inserir_filho(obter_pontuacao_aleatoria())


PONTOS_MINIMOS = 500
atual = inicio
pontos = 0

while True:
    print("")
    print("{} pontos para vencer".format(PONTOS_MINIMOS))
    print("")
    
    if atual.quantidade_de_filhos == 0:
        print("Fim de jogo")
        print("Total {} pontos".format(pontos))
        if pontos < PONTOS_MINIMOS:
            print("Você perdeu 😢")
        else:
            print("Você venceu 🏆")
        break

    mensagem = "Escolha um número de 1 a {}: ".format(
        atual.quantidade_de_filhos)

    try:
        numero_da_opcao = int(input(mensagem))
        while numero_da_opcao not in range(1, atual.filhos.quantidade+1):
            # garante que o número é válido, se é 1-quantidade de filhos
            numero_da_opcao = int(input(mensagem))
    except ValueError:
        print("Você não inseriu um número. "
              "Entendemos que você não quer mais jogar")
        break

    atual = atual.obter_filho(numero_da_opcao)
    pontos += atual.dado

    print("Você ganhou {} pontos".format(atual.dado))
    print("Total {} pontos".format(pontos))


