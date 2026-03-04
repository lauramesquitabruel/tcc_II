import numpy as np
import pandas as pd
from grafo import Grafo
from aresta import Aresta

S = "atagct"
T = "ctaggcta"
ALFABETO = ['a', 't', 'g', 'c']
n_s = len(S)
n_t = len(T)

grafo_s = Grafo(n_s)
grafo_t = Grafo(n_t)

matriz_substrings_comuns = np.zeros((n_s, n_t), dtype=int)

for i in range (0, n_s):
    for j in range(0, n_t):
        if S[i] == T[j]:
            matriz_substrings_comuns[i][j] = 1

for i in range(n_s):
    for j in range(i, n_s):
        substring_s = S[i:j+1]
        if substring_s in T:
            grafo_s.insere_aresta(Aresta(i, j))

for i in range(n_t):
    for j in range(i, n_t):
        substring_t = T[i:j+1]
        if substring_t in S:
            grafo_t.insere_aresta(Aresta(i, j))

df = pd.DataFrame(matriz_substrings_comuns, index=list(S), columns=list(T))
print(df)

print('\n GRAFOS DE SUBSTRINGS COMUNS')
grafo_s.imprime(S)
grafo_t.imprime(T)

a_s = []
a_t = []

for i in range (0, len(ALFABETO)):
    occ_s = S.count(ALFABETO[i])
    occ_t = T.count(ALFABETO[i])
        
    if occ_s > occ_t:
        a_s.append(ALFABETO[i])
    if occ_t > occ_s:
        a_t.append(ALFABETO[i])

print(f'ROTULOS ABUNDANTES \n T: {a_t} \n S: {a_s}')

grafo_exclusivos_s = Grafo(n_s)
grafo_exclusivos_t = Grafo(n_t)

abudantes = set(a_s)
for i in range(n_s):
    for j in range(i, n_s):
        substring_s = S[i:j+1]
        validacao = set(substring_s)
        if validacao.issubset(abudantes):
            grafo_exclusivos_s.insere_aresta(Aresta(i, j))

abudantes = set(a_t)
for i in range(n_t):
    for j in range(i, n_t):
        substring_t = T[i:j+1]
        validacao = set(substring_t)
        if validacao.issubset(abudantes):
            grafo_exclusivos_t.insere_aresta(Aresta(i, j))

print('\n GRAFOS DE BLOCOS EXCLUSIVOS')
grafo_exclusivos_s.imprime(S)
grafo_exclusivos_t.imprime(T)
