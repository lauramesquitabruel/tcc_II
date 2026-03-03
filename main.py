import numpy as np
import pandas as pd

S = "atagct"
T = "ctaggcta"

n_s = len(S)
n_t = len(T)

matriz_substrings_comuns = np.zeros((n_s, n_t), dtype=int)

for i in range (0, n_s):
    for j in range(0, n_t):
        if S[i] == T[j]:
            matriz_substrings_comuns[i][j] = 1

df = pd.DataFrame(matriz_substrings_comuns, index=list(S), columns=list(T))
print(df)
