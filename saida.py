import re
from grafo import Grafo
from aresta import Aresta

S = "ebacded"
T = "bdcdebedd"
alfabeto = "abcde"

g1 = Grafo(len(S))
g2 = Grafo(len(T))

g1.cria_grafo_substrings_comuns(S, T)
g2.cria_grafo_substrings_comuns(T, S)
ge1 = Grafo(len(S))
ge2 = Grafo(len(T))

a1 = ge1.rotulos_abundantes(S, T, alfabeto)
a2 = ge2.rotulos_abundantes(T, S, alfabeto)

ge1.cria_grafo_blocos_exclusivos(S, a1)
ge2.cria_grafo_blocos_exclusivos(T, a2)

E1 = g1.arestas()
E2 = g2.arestas()
Ee1 = ge1.arestas()
Ee2 = ge2.arestas()

def imprime_particao(E, Ee, str, nome):
    p = []
    for t in E:
        p.append(str[t.v1:(t.v2)+1])
    for t in Ee:
        p.append(str[t.v1:(t.v2)+1])
    p = set(p)

    print(f"{nome} = ({p})")


def imprime_saida(S, T, E1, E2, Ee1, Ee2):
    s1_formatada = ""
    for char in S:
        s1_formatada += f" {char.upper()}"
    print(f'S1 = ({s1_formatada} )')

    s2_formatada = ""
    for char in T:
        s2_formatada += f" {char.upper()}"
    print(f'S2 = ({s2_formatada} )')

    imprime_particao(E1, Ee1, S, "S'1")
    imprime_particao(E2, Ee2, T, "S'2")

    file_path = 'solution.sol'
    
    grupos = {
        "S1_p": [],
        "S2_p": [],
        "X": [],
        "Y": []
    }

    formato = re.compile(r"([a-z]+)\[(?:[^,]+,)?(\d+),(\d+)\]\s+(1)\n")

    try:
        with open(file_path, 'r') as file:
            conteudo = file.read()
            for match in formato.finditer(conteudo):
                conjunto, i1, i2, val = match.groups()
        
                i1 = int(i1)
                i2 = int(i2)

                if conjunto == "x":
                    grupos["S1_p"].append(S[i1:(i2+1)])
                elif conjunto == "y":
                    grupos["S2_p"].append(T[i1:(i2+1)])
                elif conjunto == "xe":
                    grupos["X"].append(S[i1:(i2+1)])
                elif conjunto == "ye":
                    grupos["Y"].append(T[i1:(i2+1)])
            
            for conjunto, items in grupos.items():
                saida_formada = ", ".join(items)
                print(f"{conjunto} = ( {saida_formada} )")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


imprime_saida(S, T, E1, E2, Ee1, Ee2)