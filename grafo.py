import numpy as np
from aresta import Aresta

class Grafo:
    def __init__(self, vertices):
        self.num_vertices = vertices
        self.num_arestas = 0
        self.matriz_adj = np.zeros((vertices, vertices))

    def tem_aresta(self, aresta):
        if self.matriz_adj[aresta.v1][aresta.v2]:
            return True
        return False
    
    def insere_aresta(self, aresta):
        if self.tem_aresta(aresta):
            return

        self.matriz_adj[aresta.v1][aresta.v2] = 1
        self.num_arestas = self.num_arestas + 1

    def remove_aresta(self, aresta):
        if not self.tem_aresta(aresta):
            return
    
        self.matriz_adj[aresta.v1][aresta.v2] = 0
        self.num_arestas = self.num_arestas - 1

    def arestas_contem_k(self, k):
        arestas = []
        for i in range(self.num_vertices):
            for j in range(self.num_vertices): 
                if ((i <= k <= j) and self.matriz_adj[i][j] == 1):
                    arestas.append((Aresta(i, j)))
        return arestas
    
    def arestas(self):
        arestas = []
        for i in range(self.num_vertices):
            for j in range(self.num_vertices): 
                if (self.matriz_adj[i][j] == 1):
                    arestas.append((Aresta(i, j)))
        return arestas
                    
    def imprime(self, str):
        for i in range(self.num_vertices):
            print(f"{str[i]}({i}): ", end="")
            for j in range(self.num_vertices): 
                if self.matriz_adj[i][j] != 0:
                    print(f" -> {str[j]}({j})", end="") 
            print()
        print("\n")
