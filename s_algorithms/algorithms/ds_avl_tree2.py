from random import choice

class VerticeAVL:

    def __init__(self, chave, dado, pai=None):
        self.chave = chave
        self.dado = dado
        self.pai = pai
        self.esquerdo = None
        self.direito = None
        self._altura = 0

    def __str__(self):
        return "{} {}".format(self.chave, self.dado)

    def __repr__(self):
        return str(self.chave)

    def imprimir(self):
        # recursividade: chama `imprimir` para o filho esquerdo
        if self.esquerdo:
            self.esquerdo.imprimir()
        # imprime os dados do vértice
        print("{} {}".format(self.chave, self.dado))
        # recursividade: chama `imprimir` para o filho direito
        if self.direito:
            self.direito.imprimir()

    def inserir(self, chave_nova, dado):
        if chave_nova == self.chave:
            return self

        raiz_da_subarvore = self
        if chave_nova < self.chave:
            # é menor, procura no lado esquerdo
            if self.esquerdo:
                # já tem filho no lado esquerdo, continua a procurar
                # recursividade
                raiz_da_subarvore = self.esquerdo.inserir(chave_nova, dado)
            else:
                # não tem filho no lado esquerdo
                # cria o vértice e o atribui como filho
                self.esquerdo = VerticeAVL(chave_nova, dado, self)
        elif chave_nova > self.chave:
            # é maior, procura no subarvore direita
            if self.direito:
                # já tem filho no subarvore direita, continua a procurar
                # recursividade
                raiz_da_subarvore = self.direito.inserir(chave_nova, dado)
            else:
                # não tem filho no subarvore direita
                # cria o vértice e o atribui como filho
                self.direito = VerticeAVL(chave_nova, dado, self)

        # depois de inserir o filho, seja no subarvore direita ou esquerdo
        # atualizar a altura do vértice atual (raiz_da_subarvore)
        raiz_da_subarvore.atualizar_altura()
        # balancear
        raiz_da_subarvore = raiz_da_subarvore.balancear()
        return raiz_da_subarvore.pai or raiz_da_subarvore

    def _remover_folha(self):
        """
        Remove o vértice folha
        :return: nova raiz
        """
        pai = self.pai
        if self.pai:
            # tem pai, então não sou a raiz
            if self.pai.esquerdo is self:
                # sou filho da esquerda, me desvincula da esquerda
                self.pai.esquerdo = None
            else:
                # sou filho da direita, me desvincula da direita
                self.pai.direito = None
            # me desvinculo do meu pai
            self.pai = None
        return pai

    def _remover_pai_de_um_filho(self):
        """
        Remove o vértice que tem um filho direito ou esquerdo
        :return: nova raiz
        """
        # identifico meu pai
        meu_pai = self.pai
        # tenho só 1 filho, identifico meu filho (esquerdo ou direito)
        meu_filho = self.esquerdo or self.direito

        if meu_pai is None:
            # sou raiz, a árvore está apontando para mim,
            # não posso ser removido
            # então, vou trocar de lugar com meu filho
            meu_filho.chave, self.chave = self.chave, meu_filho.chave

            # agora estou no lugar do meu filho e posso ser removido
            # a recursividade tratará a forma como serei removido
            return meu_filho.remover(meu_filho.chave)

        # meu pai, é pai do meu filho
        meu_filho.pai = meu_pai
        # meu filho, passa a ser filho do meu pai
        if meu_pai.esquerdo is self:
            # sou filho da direita,
            # meu filho passa a ser seu filho da direita
            meu_pai.esquerdo = meu_filho
        else:
            # sou filho da esquerda,
            # meu filho passa a ser seu filho da esquerda
            meu_pai.direito = meu_filho

        # me desvinculo do meu pai e do meu filhho
        self.pai = None
        self.esquerdo = None
        self.direito = None
        return meu_pai

    def _remover_pai_de_dois_filhos(self):
        """
        Remove o vértice que tem 2 filhos
        :return: nova raiz
        """
        # obter o vértice que tem a chave com menor valor (mais à esquerda)
        # na subárvore do subarvore direita
        esq = self.direito.buscar_vertice_menor_chave_na_subarvore()

        # troca valor da chave entre o nó atual e o esq
        self.chave, esq.chave = esq.chave, self.chave

        # remover o esquerdo / recursividade
        return esq.remover(esq.chave)

    def remover(self, chave):
        if self.chave == chave:
            # encontrou a chave a ser removida

            if self.esquerdo and self.direito:
                # tem ambos filhos
                raiz_da_subarvore = self._remover_pai_de_dois_filhos()
            elif self.esquerdo or self.direito:
                # tem ou filho esquerdo ou filho direito
                raiz_da_subarvore = self._remover_pai_de_um_filho()
            else:
                # nao tem filhos
                raiz_da_subarvore = self._remover_folha()
            # retorna o pai
            return raiz_da_subarvore

        raiz_da_subarvore = self
        if chave < self.chave:
            # se esquerdo existe, continua a busca pelo esquerdo
            # senão a busca encerra e None é retornado
            raiz_da_subarvore = self.esquerdo and self.esquerdo.remover(chave)
        elif chave > self.chave:
            # se direito existe, continua a busca pelo direito
            # senão a busca encerra e None é retornado
            raiz_da_subarvore = self.direito and self.direito.remover(chave)

        if raiz_da_subarvore:
            raiz_da_subarvore.atualizar_altura()
            raiz_da_subarvore = raiz_da_subarvore.balancear()

        # retorna o pai do raiz_da_subarvore se existir
        # senão retorna raiz_da_subarvore
        if raiz_da_subarvore:
            return raiz_da_subarvore.pai or raiz_da_subarvore

    def buscar_vertice_menor_chave_na_subarvore(self):
        """
        Procura o vértice que tem a menor chave na subárvore,
        ou seja, o vértice que esteja à extrema esquerda na subárvore
        """
        if self.esquerdo:
            # recursividade
            return self.esquerdo.buscar_vertice_menor_chave_na_subarvore()
        return self

    @property
    def altura(self):
        return self._altura

    def atualizar_altura(self):
        # pega a maior altura entre as duas subárvores e soma 1
        self._altura = 1 + max([self.altura_esquerda, self.altura_direita])

    @property
    def altura_esquerda(self):
        if self.esquerdo:
            return self.esquerdo.altura
        return -1

    @property
    def altura_direita(self):
        if self.direito:
            return self.direito.altura
        return -1

    @property
    def fator_de_balanceamento(self):
        return self.altura_direita - self.altura_esquerda

    def balancear(self):
        fb = self.fator_de_balanceamento
        if fb == 2:
            return self._balancear_subarvore_direita()
        if fb == -2:
            return self._balancear_subarvore_esquerda()
        return self

    def _balancear_subarvore_direita(self):
        """Resolve os casos RR e RL"""
        if self.direito.fator_de_balanceamento == -1:
            # Caso RL: aplicar rotacao do filho direito para a direita
            # para ficar com a configuração do Caso RR
            self.direito._rotacao_para_direita()

        # Caso RR: aplicar rotacao a esquerda
        nova_raiz = self._rotacao_para_esquerda()
        return nova_raiz

    def _balancear_subarvore_esquerda(self):
        """Resolve os casos LL e LR"""
        if self.esquerdo.fator_de_balanceamento == 1:
            # Caso LR: aplicar rotacao do filho esquerdo para a esquerda
            # para ficar com a configuração do Caso LL
            self.esquerdo._rotacao_para_esquerda()

        # Caso LL: aplicar rotacao direita
        nova_raiz = self._rotacao_para_direita()
        return nova_raiz

    def _rotacao_para_esquerda(self):
        """
        Caso RR (Right Right Case) - rotação única
        Caso LR (Left Right Case) - primeira rotação
             v1                            v2
            /  \\                       /     \\
           s1   v2                    v1        v3
              /  \\        ->       /  \\     /  \\
            s2   v3                s1   s2    s3   s4
                /  \\
              s3    s4
        """
        # identifica os vértices envolvidos:
        # pai da subarvore, v1 (raiz da subarvore), v2 (nova raiz da subarvore) e s2 
        raiz_da_subarvore = self
        pai_da_subarvore = raiz_da_subarvore.pai
        v1 = raiz_da_subarvore
        v2 = v1.direito
        s2 = v2.esquerdo
        # executa a rotação / atualiza os relacionamentos entre os vértices
        if pai_da_subarvore:
            if raiz_da_subarvore is pai_da_subarvore.direito:
                # raiz da subarvore é filho direito
                pai_da_subarvore.direito = v2
            else:
                pai_da_subarvore.esquerdo = v2
        v1.pai = v2
        v1.direito = s2
        v2.pai = pai_da_subarvore
        v2.esquerdo = v1
        if s2:
            s2.pai = v1

        # atualizar alturas
        v1.atualizar_altura()
        v2.atualizar_altura()

        # retorna a nova raiz
        return v2

    def _rotacao_para_direita(self):
        """
        Caso LL (Left Left Case) - rotação única
        Caso RL (RightLeft Case) - primeira rotação
                  |                           |
                  v3 (self)                  v2
                /  \\                      /    \\
               v2  s4          ->       v1       v3
             /  \\                    /  \\     /  \\
            v1  s3                   s1  s2    s3   s4
           / \\
        s1   s2
        """
        # identfica os vértices envolvidos
        raiz_da_subarvore = self
        v3 = raiz_da_subarvore
        pai_da_subarvore = raiz_da_subarvore.pai
        v2 = v3.esquerdo
        s3 = v2.direito

        # Faz a rotação / atualiza os relacionamentos entre os vértices
        if pai_da_subarvore:
            if raiz_da_subarvore is pai_da_subarvore.direito:
                pai_da_subarvore.direito = v2
            else:
                pai_da_subarvore.esquerdo = v2
        v2.pai = pai_da_subarvore
        v2.direito = v3
        v3.pai = v2
        v3.esquerdo = s3
        if s3:
            s3.pai = v3

        # atualizar alturas
        v3.atualizar_altura()
        v2.atualizar_altura()

        # retorna a nova raiz
        return v2

    def buscar(self, chave_procurada):
        if chave_procurada == self.chave:
            return self

        if chave_procurada < self.chave:
            # é menor, procura no lado esquerdo
            if self.esquerdo:
                # já tem filho no lado esquerdo, continua a procurar
                # recursividade
                return self.esquerdo.buscar(chave_procurada)
        elif chave_procurada > self.chave:
            # é maior, procura no subarvore direita
            if self.direito:
                # já tem filho no subarvore direita, continua a procurar
                # recursividade
                return self.direito.buscar(chave_procurada)


class ArvoreAVL:

    def __init__(self):
        self._raiz = None

    def inserir(self, chave, dado):
        if self._raiz is None:
            # árvore está vazia, cria o primeiro vértice
            self._raiz = VerticeAVL(chave, dado)
        else:
            # árvore já tem vértices
            # executa `self._raiz.inserir(chave)`
            self._raiz = self._raiz.inserir(chave, dado)

    def remover(self, chave):
        if self._raiz is not None:
            # árvore não está vazia
            # então executa `self._raiz.remover(chave)`
            nova_raiz = self._raiz.remover(chave)
            if nova_raiz:
                self._raiz = nova_raiz

    def imprimir(self):
        print("")
        if self._raiz is not None:
            self._raiz.imprimir()
        print("")

    def buscar(self, chave):
        if self._raiz is not None:
            # árvore não está vazia
            # então executa `self._raiz.remover(chave)`
            return self._raiz.buscar(chave)


class LeitorLivro:

    def __init__(self):
        self.avl = ArvoreAVL()

    def inserir_anotacoes(self, posicao, anotacao):
        self.avl.inserir(posicao, anotacao)

    def obter_anotacao(self, posicao):
        vertice = self.avl.buscar(posicao)
        if vertice:
            print("Anotação de {}: {}".format(posicao, vertice.dado))
        else:
            print("Não há anotação nesta {}".format(posicao))

    def remover_anotacao(self, posicao):
        print("Remover: {}".format(posicao))
        self.avl.remover(posicao)

    def obter_anotacoes(self):
        print("Anotações:")
        self.avl.imprimir()

    @property
    def sem_anotacoes(self):
        return self.avl._raiz is None


leitor = LeitorLivro()

# simula um livro com 10 a 30 mil linhas
total_linhas = choice(range(10000, 30000))

# acoes que o usuario pode fazer
acoes = [
    "inserir_anotacoes",
    "obter_anotacoes",
    "remover_anotacao",
    "obter_anotacao",
]

# coloca as instruções em repetição até que o usuário digite CTRL+C
while True:

    try:
        acao = choice(acoes)

        if acao == "inserir_anotacoes":
            linha_atual = choice(range(1, total_linhas + 1))
            entrada = input(
                "Escreva um anotacao na linha {}: ".format(linha_atual))
            leitor.inserir_anotacoes(linha_atual, entrada)
            continue

        if leitor.sem_anotacoes:
            continue

        if acao == "obter_anotacoes":
            leitor.obter_anotacoes()
            continue

        if acao == "remover_anotacao":
            linha = input("Escreva o número da linha da qual quer remover "
                          "a anotação: ")
            leitor.remover_anotacao(int(linha))
            continue

        if acao == "obter_anotacao":
            linha = input("Escreva o número da linha que quer consultar "
                          "a anotação: ")

            leitor.obter_anotacao(int(linha))
    # except KeyboardInterrupt:
    except Exception:
        print("Usuário interrompeu execução")
        break


