class Item:
  """ insere um item em uma lista """
  def __init__(self, valor=None, anterior=None):
    self.valor = valor
    self.anterior = anterior
  def __repr__(self):
    return "%s\n%s"% (self.valor, self.anterior)

class Pilha:
  """permite a criação de uma pilha"""
  def __init__(self):
    self.topo = None
  def __repr__(self):
    return "TOPO\n%s\nRODAPÉ" % (self.topo)

  def push(self, valor):
    # Cria um novo objeto Item
    item_novo = Item(valor)
    # o anterior passa a ser o antigo topo
    item_novo.anterior = self.topo
    # o topo da pilha passa a ser o item novo
    self.topo = item_novo

  def pop(self):
    assert self.topo, "Erro: pilha vazia."
    # modifica o valor do topo
    self.topo = self.topo.anterior

def main():
  # cria um novo objeto do tipo Pilha
  pilha = Pilha()
  # Vamos inserir alguns valores
  pilha.push('a')
  pilha.push('b')
  pilha.push('c')
  pilha.push('d')
  print(pilha)
  # removendo os dois últimos itens
  pilha.pop() # remove d
  pilha.pop() # remove c
  print(pilha)

if __name__ == "__main__":
    main()


