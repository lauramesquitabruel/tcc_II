import gurobipy as gp
from gurobipy import GRB

#https://github.com/FernandoFdeS/alocador_de_salas

#modelo
m = gp.Model()

#variáveis
x = {}

#restrições
m.addConstrs(
    gp.quicksum(x[[aresta.v1, aresta.v2]] for aresta in g.arestas_contem k()) + 
    gp.quicksum(x[[aresta.v1, aresta.v2]] for aresta in g.arestas_contem k()) = 1
    for k in range (0, len(S))
)