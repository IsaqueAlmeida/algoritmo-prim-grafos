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
