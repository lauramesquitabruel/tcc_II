import gurobipy as gp
from gurobipy import GRB

#https://github.com/FernandoFdeS/alocador_de_salas

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
for e in g1.arestas:
    t1 = m.addVars(vtype=GRB.BINARY, name="t1")

for e in g2.arestas:
    t2 = m.addVars(vtype=GRB.BINARY, name="t2")

for e in ge1.arestas:
    te1 = m.addVars(vtype=GRB.BINARY, name="te1")

for e in ge2.arestas:
    te2 = m.addVars(vtype=GRB.BINARY, name="te2")


#restrições
m.addConstrs(
    gp.quicksum(x[[t1.v1, t1.v2]] for t1 in g1.arestas_contem_k(k)) * xt1 + 
    gp.quicksum(x[[te1.v1, te1.v2]] for te1 in ge1.arestas_contem k(k)) * xte1 = 1
    for k in range (0, len(S)-1)
)