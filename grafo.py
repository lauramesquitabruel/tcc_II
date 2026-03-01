from aresta import Aresta

class Grafo:
    def __init__(self, vertices):
        self.num_vertices = vertices
        self.num_arestas = 0
        self.matriz_adj = [self.num_vertices][self.num_vertices]

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

    def imprime(self):
        for i in range (0, self.num_vertices, i +1):
            print("{i}: ")
            for j in range (0, self.num_vertices, j +1): 
                if (self.matriz_adj[i][j] != 0):
                    print("   {j}") 
            
            print("\n")
