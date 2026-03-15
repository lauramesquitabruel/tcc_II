import gurobipy as gp
from gurobipy import GRB
from grafo import Grafo
from aresta import Aresta
from bloco import Bloco

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
    xb = {}
    yb = {}

    E1 = g1.arestas()
    E2 = g2.arestas()

    #arestas
    for t1 in E1:
        x[t1.v1, t1.v2] = m.addVar(vtype=GRB.BINARY, name=f"x[{t1.v1},{t1.v2}]")
        #blocos para matchList
        b1 = Bloco('S1', t1.v1, t1.v2)
        xb[b1.id, b1.v1, b1.v2] = m.addVar(vtype=GRB.BINARY, name=f"xb[{b1.id},{b1.v1},{b1.v2}]")

    for t2 in E2:
        y[t2.v1, t2.v2] = m.addVar(vtype=GRB.BINARY, name=f"y[{t2.v1},{t2.v2}]")

    for te1 in ge1.arestas():
        xe[te1.v1, te1.v2] = m.addVar(vtype=GRB.BINARY, name=f"xe[{te1.v1},{te1.v2}]")

    for te2 in ge2.arestas():
        ye[te2.v1, te2.v2] = m.addVar(vtype=GRB.BINARY, name=f"ye[{te2.v1},{te2.v2}]")
    
    for t1 in E2:
        b2 = Bloco('S2', t1.v1, t1.v2)
        yb[b2.id, b2.v1, b2.v2] = m.addVar(vtype=GRB.BINARY, name=f"xb[{b2.id},{b2.v1},{b2.v2}]")

    #restrições

    #5.2
    m.addConstr(gp.quicksum(x[t1.v1, t1.v2]for t1 in E1) == gp.quicksum(y[t2.v1, t2.v2] for t2 in E2),
                name="fat_blocos_guais")

    #para string S (5.3)
    for k in range(len(S)):
        e1 = g1.arestas_contem_k(k)
        ee1 = ge1.arestas_contem_k(k)

        if(len(e1) > 0 and len(ee1) > 0):
            m.addConstr(
                gp.quicksum(x[t1.v1, t1.v2] for t1 in e1) + 
                gp.quicksum(xe[te1.v1, te1.v2] for te1 in ee1)  == 1,
                name=f"n_sobrep_s1[{k}]"
            )
        else:
            if (len(e1) > 0):
                m.addConstr(
                    gp.quicksum(x[t1.v1, t1.v2] for t1 in e1) == 1,
                    name=f"n_sobrep_s1[{k}]"
                )
            elif (len(ee1) > 0):
                m.addConstr(
                    gp.quicksum(xe[te1.v1, te1.v2] for te1 in ee1)  == 1,
                    name=f"n_sobrep_s1[{k}]"
                )
            else:
                print("sem restrição de não sobreposição")

    #para string T (5.4)
    for k in range(len(T)):
        e2 = g2.arestas_contem_k(k)
        ee2 = ge2.arestas_contem_k(k)

        if(len(e2) > 0 and len(ee2) > 0):
            m.addConstr(
                gp.quicksum(y[t2.v1, t2.v2] for t2 in e2) + 
                gp.quicksum(ye[te2.v1, te2.v2] for te2 in ee2) == 1,
                name=f"n_sobrep_s2[{k}]"
            )
        else:
            if (len(e2) > 0):
                m.addConstr(
                    gp.quicksum(y[t2.v1, t2.v2] for t2 in e2) == 1,
                    name=f"n_sobrep_s2[{k}]"
                )
            elif (len(ee2) > 0):
                m.addConstr(
                    gp.quicksum(ye[te2.v1, te2.v2] for te2 in ee2)  == 1,
                    name=f"n_sobrep_s2[{k}]"
                )
            else:
                print("sem restrição de não sobreposição")

    #para string S (5.5)
    sig1 = g1.arestas_saida(0)
    sige1 = ge1.arestas_saida(0)

    if(len(sig1) > 0 and len(sige1) > 0):
            m.addConstr(
                gp.quicksum(x[t1.v1, t1.v2] for t1 in sig1) + 
                gp.quicksum(xe[te1.v1, te1.v2] for te1 in sige1) == 1,
                name=f"n_sobrep_saida_s1[{k}]"
            )
    else:
        if (len(sig1) > 0):
            m.addConstr(
                gp.quicksum(x[t1.v1, t1.v2] for t1 in sig1) == 1,
                name=f"n_sobrep_saida_s1[{k}]"
            )
        elif (len(sige1) > 0):
            m.addConstr(
                gp.quicksum(xe[te1.v1, te1.v2] for te1 in sige1)  == 1,
                name=f"n_sobrep_saida_s1[{k}]"
            )
        else:
            print("sem restrição de não sobreposição das arestas de saída de v0 em S1")

    # para string S (5.6)
    for v in range(len(S) - 1):
        sig1_en = g1.arestas_entrada(v)
        sige1_en = ge1.arestas_entrada(v)

        sig1_en_prox = g1.arestas_entrada(v + 1)
        sige1_en_prox = ge1.arestas_entrada(v + 1)

        #verifica se tem pelo menos um conjunto não vazio e calcula o valor de cada lado antes de montar a equação
        total_edges = len(sig1_en) + len(sige1_en) + len(sig1_en_prox) + len(sige1_en_prox)
        if total_edges > 0:
            lhs = gp.quicksum(x[t1.v1, t1.v2] for t1 in sig1_en) + gp.quicksum(xe[te1.v1, te1.v2] for te1 in sige1_en)
            rhs = gp.quicksum(x[t1.v1, t1.v2] for t1 in sig1_en_prox) + gp.quicksum(xe[te1.v1, te1.v2] for te1 in sige1_en_prox)
        
            m.addConstr(lhs == rhs, name=f"n_sobrep_entrada_s1[{v}]")
       
    #para string T (5.7)
    sig2 = g2.arestas_saida(0)
    sige2 = ge2.arestas_saida(0)

    if(len(sig2) > 0 and len(sige2) > 0):
            m.addConstr(
                gp.quicksum(y[t2.v1, t2.v2] for t2 in sig2) + 
                gp.quicksum(ye[te2.v1, te2.v2] for te2 in sige2) == 1,
                name=f"n_sobrep_saida_s2[{k}]"
            )
    else:
        if (len(sig2) > 0):
            m.addConstr(
                gp.quicksum(y[t2.v1, t2.v2] for t2 in sig2) == 1,
                name=f"n_sobrep_saida_s2[{k}]"
            )
        elif (len(sige2) > 0):
            m.addConstr(
                gp.quicksum(ye[te2.v1, te2.v2] for te2 in sige2)  == 1,
                name=f"n_sobrep_saida_s2[{k}]"
            )
        else:
            print("sem restrição de não sobreposição das arestas de saída de v0 em S2")

    # para string T (5.8)
    for v in range(len(T) - 1):
        sig2_en = g2.arestas_entrada(v)
        sige2_en = ge2.arestas_entrada(v)

        sig2_en_prox = g2.arestas_entrada(v + 1)
        sige2_en_prox = ge2.arestas_entrada(v + 1)

        #verifica se tem pelo menos um conjunto não vazio e calcula o valor de cada lado antes de montar a equação
        total_edges = len(sig2_en) + len(sige2_en) + len(sig2_en_prox) + len(sige2_en_prox)
        if total_edges > 0:
            lhs = gp.quicksum(y[t2.v1, t2.v2] for t2 in sig2_en) + gp.quicksum(ye[te2.v1, te2.v2] for te2 in sige2_en)
            rhs = gp.quicksum(y[t2.v1, t2.v2] for t2 in sig2_en_prox) + gp.quicksum(ye[te2.v1, te2.v2] for te2 in sige1_en_prox)
        
            m.addConstr(lhs == rhs, name=f"n_sobrep_entrada_s2[{v}]")
       
    #5.9
    matchList_e1 = []
    matchList_e2 = []

    for t1 in E1:
        for b1 in xb.keys():
            if S[t1.v1:t1.v2] == S[b1[1]:b1[2]]:
                matchList_e1.append(b1)
        for b2 in yb.keys():
            if S[t1.v1:t1.v2] == T[b2[1]:b2[2]]:
                matchList_e2.append(b2)
        m.addConstr(gp.quicksum(xb[b1] for b1 in matchList_e1) == gp.quicksum(yb[b2] for b2 in matchList_e2),
                    name=f"blocos_correspontes_{t1.v1},{t1.v2}")
        
    matchList_e1.clear()
    matchList_e2.clear()

    m.write("problem.lp")

main()