import gurobipy as gp
from gurobipy import GRB
from grafo import Grafo

#https://github.com/FernandoFdeS/alocador_de_salas

def main():
    S = input()
    T = input()
    alfabeto = input()

    g1 = Grafo(len(S))
    g2 = Grafo(len(T))

    g1.cria_grafo_substrings_comuns(S, T)
    g2.cria_grafo_substrings_comuns(S, T)

    ge1 = Grafo(len(S))
    ge2 = Grafo(len(T))

    a1 = ge1.rotulos_abundantes(S, T, alfabeto)
    a2 = ge2.rotulos_abundantes(T, S, alfabeto)

    ge1.cria_grafo_blocos_exclusivos(S, a1)
    ge2.cria_grafo_blocos_exclusivos(T, a2)

    #modelo
    m = gp.Model()

    #variáveis
    x = {}

    #variáveis de decisão
    xt1 = m.addVars(vtype=GRB.BINARY, name="xt1")
    xte1 = m.addVars(vtype=GRB.BINARY, name="xte1")
    yt2 = m.addVars(vtype=GRB.BINARY, name="yt2")
    yte2 = m.addVars(vtype=GRB.BINARY, name="yte2")

    #arestas
    for t1 in g1.arestas:
        x[t1] = m.addVars(vtype=GRB.BINARY, name="t1")

    for t2 in g2.arestas:
        x[t2] = m.addVars(vtype=GRB.BINARY, name="t2")

    for e in ge1.arestas:
        te1 = m.addVars(vtype=GRB.BINARY, name="te1")

    for e in ge2.arestas:
        te2 = m.addVars(vtype=GRB.BINARY, name="te2")


    #restrições

    for k in range(len(S)):
        e1 = g1.arestas_contem_k(k)
        ee1 = ge1.arestas_contem_k(k)

        m.addConstrs(
            gp.quicksum(x[t1] for t1 in e1) + 
            gp.quicksum(x[te1] for te1 in ee1)  == 1,
            name="fatoração em blocos que não se sobrepõem"
        )