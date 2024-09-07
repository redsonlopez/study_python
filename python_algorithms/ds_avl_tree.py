class VerticeAVL:

    def __init__(self, chave, pai=None):
        self.chave = chave
        self.pai = pai
        self.esquerdo = None
        self.direito = None
        self._altura = 0

    def __str__(self):
        return str(self.chave)

    def __repr__(self):
        return str(self.chave)

    def imprimir_subarvore(self, recuo=0, sentido=""):
        # recursividade: chama `imprimir_subarvore` para o filho direito
        if self.direito:
            self.direito.imprimir_subarvore(recuo+10, sentido="/")    
        # imprime os dados do vértice
        print(
            "{}{}----> [{}] (h={},fb={})".format(
                " " * recuo,
                sentido,
                self.chave,
                self.altura,
                self.fator_de_balanceamento,
                self.pai,
            )
        )
        # recursividade: chama `imprimir_subarvore` para o filho esquerdo  
        if self.esquerdo:
            self.esquerdo.imprimir_subarvore(recuo+10, sentido="\\")

    def inserir(self, chave_nova):
        print("Inserir {} (atual={})".format(chave_nova, self.chave))
        if chave_nova == self.chave:
            return self

        raiz_da_subarvore = self
        if chave_nova < self.chave:
            # é menor, procura no lado esquerdo
            if self.esquerdo:
                # já tem filho no lado esquerdo, continua a procurar
                # recursividade
                raiz_da_subarvore = self.esquerdo.inserir(chave_nova)
            else:
                # não tem filho no lado esquerdo
                # cria o vértice e o atribui como filho
                self.esquerdo = VerticeAVL(chave_nova, self)
        elif chave_nova > self.chave:
            # é maior, procura no subarvore direita
            if self.direito:
                # já tem filho no subarvore direita, continua a procurar
                # recursividade
                raiz_da_subarvore = self.direito.inserir(chave_nova)
            else:
                # não tem filho no subarvore direita
                # cria o vértice e o atribui como filho
                self.direito = VerticeAVL(chave_nova, self)

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
        print("Remover folha. Sou {}, vértice folha, filho de {}".format(
            self.chave, self.pai.chave))
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
        print("Remover PAI de 1 filho. Sou {}, pai de {}".format(
            self.chave, (self.esquerdo or self.direito).chave))
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
        print("Remover PAI de 2 filhos. Sou {}, pai de {} e {}".format(
            self.chave, self.esquerdo.chave, self.direito.chave))
        # obter o vértice que tem a chave com menor valor (mais à esquerda)
        # na subárvore do subarvore direita
        esq = self.direito.buscar_vertice_menor_chave_na_subarvore()
        print("Menor chave: {}".format(str(esq)))

        # troca valor da chave entre o nó atual e o esq
        print("As chaves {} e {} trocam de vértice".format(self.chave, esq.chave))
        self.chave, esq.chave = esq.chave, self.chave

        # remover o esquerdo / recursividade
        return esq.remover(esq.chave)

    def remover(self, chave):
        print("Remover {} (chave atual: {})".format(chave, self.chave))
        if self.chave == chave:
            print("Achou {} para remover".format(chave))
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
        # retorna o pai do raiz_da_subarvore se existir, senão retorna raiz_da_subarvore
        return raiz_da_subarvore.pai or raiz_da_subarvore

    def buscar_vertice_menor_chave_na_subarvore(self):
        """
        Procura o vértice que tem a menor chave na subárvore,
        ou seja, o vértice que esteja à extrema esquerda na subárvore
        """
        print("Procurar vértice que tem a menor chave "
              "na subárvore de {}".format(str(self)))
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
        print("fb({})={}".format(self.chave, fb))
        if fb == 2:
            return self._balancear_subarvore_direita()
        if fb == -2:
            return self._balancear_subarvore_esquerda()
        return self

    def _balancear_subarvore_direita(self):
        """Resolve os casos RR e RL"""
        print("Balancear subarvore direita de {}".format(self.chave))
        if self.direito.fator_de_balanceamento == -1:
            # Caso RL: aplicar rotacao do filho direito para a direita
            # para ficar com a configuração do Caso RR
            print("Caso RL: Rotação de {} à direita + Rotação de {} à esqueda".format(
                str(self.direito), self.chave)
            )
            self.direito._rotacao_para_direita()
        
        # Caso RR: aplicar rotacao a esquerda
        nova_raiz = self._rotacao_para_esquerda()
        return nova_raiz

    def _balancear_subarvore_esquerda(self):
        """Resolve os casos LL e LR"""
        print("Balancear subarvore esquerda de {}".format(self.chave))
        if self.esquerdo.fator_de_balanceamento == 1:
            # Caso LR: aplicar rotacao do filho esquerdo para a esquerda
            # para ficar com a configuração do Caso LL
            print("Caso LR: Rotação de {} à esquerda + Rotação de {} à direita".format(
                str(self.esquerdo), self.chave)
            )
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
        self._rotacao_info("esquerda")
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

        self._rotacao_info("esquerda", v2)
    
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
        self._rotacao_info(sentido="direita")        
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

        self._rotacao_info("direita", v2)
        
        # retorna a nova raiz
        return v2

    def _rotacao_info(self, sentido="esquerda", nova_raiz_da_subarv=None):
        print("")
        if nova_raiz_da_subarv is None:
            caso = "LL" if sentido == "direita" else "RR"
            print("Caso {}: Rotação de {} à {}".format(caso, sentido, self.chave))
            print("Antes:")
        else:
            print("Depois:")

        atual = nova_raiz_da_subarv or self
        (atual.pai or atual).imprimir_subarvore()
        print("")
        if nova_raiz_da_subarv:
            print("Resultado de Rotação de {} à {}: nova_raiz={} (pai={})".format(
            self.chave, sentido, str(nova_raiz_da_subarv), str(nova_raiz_da_subarv.pai)))

# 360
class ArvoreAVL:

    def __init__(self):
        self._raiz = None

    def inserir(self, chave):
        if self._raiz is None:
            # árvore está vazia, cria o primeiro vértice
            self._raiz = VerticeAVL(chave)
        else:
            # árvore já tem vértices
            # executa `self._raiz.inserir(chave)`
            self._raiz = self._raiz.inserir(chave)
        self.imprimir()

    def remover(self, chave):
        if self._raiz is not None:
            # árvore não está vazia
            # então executa `self._raiz.remover(chave)`
            self._raiz = self._raiz.remover(chave)
            self.imprimir()
    
    def imprimir(self):
        print("")
        self._raiz.imprimir_subarvore()
        print("")


# Criação do objeto `arvore_avl` da classe ArvoreAVL
arvore_avl = ArvoreAVL()

# inserção de 50, 60, 70
# para inserir 70, o caminho percorrido é 50, 60.
# após a inserção de 70, a subárvore do vértice 50 fica desbalanceada
# para balancear, executa a rotação do vértice 50 para a esquerda
# a nova raiz da subárvore e também da árvore é 60
arvore_avl.inserir(50)
arvore_avl.inserir(60)
arvore_avl.inserir(70)

# inserção de 40
arvore_avl.inserir(40)
# para inserir 30, o caminho percorrido é 50, 40.
# após a inserção de 30, a subárvore do vértice 50 fica desbalanceada
# para balancear, executa a rotação do vértice 50 para a direita
# a nova raiz da subárvore é 40, a raiz da árvore continua sendo 60
arvore_avl.inserir(30)

# inserção de 80
arvore_avl.inserir(80)
# para inserir 75, o caminho percorrido é 60, 70, 80.
# após a inserção de 75, a subárvore do vértice 70 fica desbalanceada
# para balancear, executa a rotação do vértice 80 para a direita
# e a rotação do vértice 70 para a esquerda
# a nova raiz da subárvore é 75, a raiz da árvore continua sendo 60
arvore_avl.inserir(75)

# Inserção de 45
arvore_avl.inserir(45)
# para inserir 47, o caminho percorrido é 60, 40, 50, 45.
# após a inserção de 47, a subárvore do vértice 50 fica desbalanceada
# para balancear, executa a rotação do vértice 45 para a esquerda
# e a rotação do vértice 50 para a direita
# a nova raiz da subárvore é 47, a raiz da árvore continua sendo 60
arvore_avl.inserir(47)

# Remoção de 30, vertice folha
arvore_avl.remover(30)

# Remoção de 40, vertice pai de 1 filho
arvore_avl.remover(40)

# Remoção de 60, vertice pai de 2 filhos
arvore_avl.remover(60)

# Remoção de 75
arvore_avl.remover(75)

# Remoção de 80
arvore_avl.remover(80)

