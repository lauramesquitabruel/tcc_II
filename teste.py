from utils.grafo import Grafo
from utils.saida import imprime_saida

def teste(S, T, alfabeto):
    g1 = Grafo(len(S))
    g2 = Grafo(len(T))

    g1.cria_grafo_substrings_comuns(S, T)
    print("grafo1 comum")
    g1.imprime(S)

    g2.cria_grafo_substrings_comuns(T, S)
    print("grafo2 comum")
    g2.imprime(T)

    ge1 = Grafo(len(S))
    ge2 = Grafo(len(T))

    a1 = ge1.rotulos_abundantes(S, T, alfabeto)
    a2 = ge2.rotulos_abundantes(T, S, alfabeto)

    ge1.cria_grafo_blocos_exclusivos(S, a1)
    print("grafo1 exclusivo")
    ge1.imprime(S)

    ge2.cria_grafo_blocos_exclusivos(T, a2)
    print("grafo2 exclusivo")
    ge2.imprime(T)

    imprime_saida(S, T)

    
