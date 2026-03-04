import numpy as np
import pandas as pd
from grafo import Grafo
from aresta import Aresta

S = "atagct"
T = "ctaggcta"

n_s = len(S)
n_t = len(T)

grafo_s = Grafo(n_s)
grafo_t = Grafo(n_t)

matriz_substrings_comuns = np.zeros((n_s, n_t), dtype=int)

for i in range (0, n_s):
    for j in range(0, n_t):
        if S[i] == T[j]:
            matriz_substrings_comuns[i][j] = 1

for i in range(len(S)):
    for j in range(i, len(S)):
        substring_s = S[i:j+1]
        if substring_s in T:
            grafo_s.insere_aresta(Aresta(i, j))

for i in range(len(T)):
    for j in range(i, len(T)):
        substring_t = T[i:j+1]
        if substring_t in S:
            grafo_t.insere_aresta(Aresta(i, j))

df = pd.DataFrame(matriz_substrings_comuns, index=list(S), columns=list(T))
print(df)

print('\n')
grafo_s.imprime()
grafo_t.imprime()
