import gurobipy as gp
from gurobipy import GRB
from grafo import Grafo

#https://github.com/FernandoFdeS/alocador_de_salas

def main():
    S = "ebacded"
    T = "bdcdebedd"
    alfabeto = "abcde"

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

    print(ge2)    
    #modelo
    m = gp.Model()

    #variáveis
    x = {}
    y = {}
    xe = {}
    ye = {}

    E1 = g1.arestas()
    E2 = g2.arestas()

    #arestas
    for t1 in E1:
        x[t1.v1, t1.v2] = m.addVar(vtype=GRB.BINARY, name=f"x[{t1.v1},{t1.v2}]")

    for t2 in E2:
        y[t2.v1, t2.v2] = m.addVar(vtype=GRB.BINARY, name=f"y[{t2.v1},{t2.v2}]")

    for te1 in ge1.arestas():
        xe[te1.v1, te1.v2] = m.addVar(vtype=GRB.BINARY, name=f"xe[{te1.v1},{te1.v2}]")

    for te2 in ge2.arestas():
        ye[te2.v1, te2.v2] = m.addVar(vtype=GRB.BINARY, name=f"ye[{te2.v1},{te2.v2}]")
    

    #restrições
    # m.addConstrs(gp.quicksum(x[t1]for t1 in E1) == gp.quicksum(y[t2] for t2 in E2) * y[t2],
    #              name="fatoração em números iguais de blocos")

    #para string S
    for k in range(len(S)):
        e1 = g1.arestas_contem_k(k)
        print(e1)
        ee1 = ge1.arestas_contem_k(k)
        print(ee1)

        if(len(e1) > 0 and len(ee1) > 0):
            m.addConstr(
                gp.quicksum(x[t1.v1, t1.v2] for t1 in e1) + 
                gp.quicksum(xe[te1.v1, te1.v2] for te1 in ee1)  == 1,
                name=f"n_sobrep[{k}]"
            )
        else:
            if (len(e1) > 0):
                m.addConstr(
                    gp.quicksum(x[t1.v1, t1.v2] for t1 in e1) == 1,
                    name=f"n_sobrep[{k}]"
                )
            elif (len(ee1) > 0):
                m.addConstr(
                    gp.quicksum(xe[te1.v1, te1.v2] for te1 in ee1)  == 1,
                    name=f"n_sobrep[{k}]"
                )
            else:
                print("sem restrição de não sobreposição")

    # #para astring T
    # for k in range(len(T)):
    #     e2 = g2.arestas_contem_k(k)
    #     ee2 = ge2.arestas_contem_k(k)

    #     m.addConstrs(
    #         gp.quicksum(y[t2] for t2 in e2) + 
    #         gp.quicksum(y[te2] for te2 in ee2)  == 1,
    #         name="fatoração em blocos que não se sobrepõem"
    #     )

    m.write("problem.lp")

main()