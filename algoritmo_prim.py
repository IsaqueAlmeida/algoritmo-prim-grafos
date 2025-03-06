# definindo o algoritmo de Prim

class Grafo:
    def __init__(self, orientado=False):
        self._lista_de_adjacencias = dict()
        self.orientado = orientado

    def vertices(self):  # retorna os nomes dos vértices
        return set(self._lista_de_adjacencias.keys())

    def arestas(self, v_origem=None):
        # retorna as arestas do vértices v_origem ou do grafo inteiro
        if v_origem:
            # obter as arestas do vértices
            return self.v_arestas(v_origem)
        # retorna as arestas do grafo inteiro
        arestas_do_grafo = []
        for v_origem in self.vertices():
            # acumulará as arestas de todos os vértices
            arestas_do_grafo += self.v_arestas(v_origem)
            return arestas_do_grafo

    def v_arestas(self, v_origem):
        # retorna as arestas do vértices v_origem
        # retorna as arestas de um vértices
        arestas = []
        for v_destino, custo in self._lista_de_adjacencias[v_origem]:
            arestas.append((v_origem, v_destino, custo))
        return arestas

    def inserir_arestas(self, u, v, custo):
        # cria uma aresta entre os vértices u e v
        # cria uma chave u com valor lista vazia no dicionário
        # se a chave u não existir
        self._lista_de_adjacencias.setdefault(u, [])

        # cria uma chave v com o valor lista vazia no dicionário
        # se a chave v não existir
        # se a chave v não existir
        self._lista_de_adjacencias.setdefault(v, [])

        # adiciona a aresta ao vértices u
        self._lista_de_adjacencias[u].append((v, custo))

        if not self.orientado:
            # se é um grafo orientado
            # adiciona a aresta ao vértices v
            self._lista_de_adjacencias[v].append((u, custo))

    def inserir_aresta(self, arestas):
        # insere todas as arestas no grafo
        for aresta in arestas:
            self.inserir_arestas(*aresta)

    def imprimir(self):
        total = 0
        for u, v, custo in self.arestas():
            print("({}, {}, {})".format(u, v, custo), end="")
            total += custo
        if not self.orientado:
            # divide por 2 para desconar a duplicidade
            total = total / 2
        print("")
        print("Custo: {}".format(total))
    
    def prim(grafo, inicio):

        # cria uma MST vazia
        mst = Grafo(True)
        mst.inserir_arestas(inicio, inicio, 0)
        ordenadas = []

        # atualiza o vértice atual com o vértice inicial
        v = inicio

        while set(mst.vertices) != set(grafo.vertices):
            print()
            MST_V = mst.vertices
            G_V_menos_MST_V = grafo.vertices - mst.vertices
            print('MST.V = {}'.format(MST_V))
            print('G.V - MST.V = {}'.format(G_V_menos_MST_V))
            print("Vértice atual: {}".format(v))
        
        # soma as arestas existente na fila com as arestas do vértice atual
        # e reordena
        print("Insere na fila as arestas que partem de {}".format(v))
        ordenadas = sorted(
            set(ordenadas + grafo.arestas(v)),
            key=lambda aresta: aresta[-1]
        )
