"""
Carlos A Delgado
13 de Mayo de 2023
Coloreo del grafo ciclo complemento
"""
import networkx as nx
import matplotlib.pyplot as plt
import math

for n in range(3,100):
    G = nx.complete_graph(n)
    numCol = len(set(nx.coloring.greedy_color(G).values()))
    print(n,numCol)
