"""
Carlos A Delgado
13 de Mayo de 2023
Coloreo del grafo ciclo complemento
"""
import networkx as nx
import matplotlib.pyplot as plt
import math
def h(n):
    if n==3:
      return 1
    else:
       return math.ceil(n/2)

for n in range(3,100):
    G = nx.wheel_graph(n+1)
    G = nx.complement(G)
    numCol = len(set(nx.coloring.greedy_color(G).values()))
    hcol = h(n)
    print(n,numCol,hcol, numCol==hcol)
