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
                if((i <= k <= j) and self.matriz_adj[i][j] != 0):
                    arestas.append(Aresta(i, j))
        return arestas
    
    def cria_grafo_substrings_comuns(self, S1, S2):
        for i in range(len(S1)):
            for j in range(i, len(S1)):
                substring_s = S1[i:j+1]
                if substring_s in S2:
                    self.insere_aresta(Aresta(i, j))

    def rotulos_abundantes(self, S1, S2, alfabeto):
        abuntantes = []
        for i in range (0, len(alfabeto)):
            occ_s1 = S1.count(alfabeto[i])
            occ_s2 = S2.count(alfabeto[i])
        
            if occ_s1 > occ_s2:
                abuntantes.append(alfabeto[i])
        return abuntantes
    
    def cria_grafo_blocos_exclusivos(self, str, a):
        abudantes = set(a)
        for i in range(len(str)):
            for j in range(i, len(str)):
                substring_s = str[i:j+1]
                validacao = set(substring_s)
                if validacao.issubset(abudantes):
                    self.insere_aresta(Aresta(i, j))

    def arestas(self):
        arestas = []
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if (self.matriz_adj[i][j] != 0):
                    arestas.append(Aresta(i, j))
        return arestas

    def imprime(self, str):
        for i in range(self.num_vertices):
            print(f"{str[i]}({i}): ", end="")
            for j in range(self.num_vertices): 
                if self.matriz_adj[i][j] != 0:
                    print(f" -> {str[j]}({j})", end="") 
            print()
        print("\n")
