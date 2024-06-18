from Vetor_Ordenado_Adj import VetorOrdenadoAdj
from Grafo import Grafo

class AEstrela:
  def __init__(self, objetivo):
    self.objetivo = objetivo
    self.encontrado = False

  def buscar(self, atual):
    print('------------------')
    print('Atual: {}'.format(atual.rotulo))
    atual.visitado = True

    if atual == self.objetivo:
      self.encontrado = True
    else:
      vetor_ordenado = VetorOrdenadoAdj(len(atual.adjacentes))
      for adjacente in atual.adjacentes:
        if adjacente.vertice.visitado == False:
          adjacente.vertice.visitado = True
          vetor_ordenado.insere(adjacente)
      vetor_ordenado.imprime()

      if vetor_ordenado.valores[0] != None:
        self.buscar(vetor_ordenado.valores[0].vertice)

# grafo = Grafo()
# vetor = VetorOrdenadoAdj(20)
# vetor.insere(grafo.arad.adjacentes[0])
# vetor.insere(grafo.arad.adjacentes[1])
# vetor.insere(grafo.arad.adjacentes[2])

# busca_aestrela = AEstrela(grafo.bucharest)
# busca_aestrela.buscar(grafo.arad)