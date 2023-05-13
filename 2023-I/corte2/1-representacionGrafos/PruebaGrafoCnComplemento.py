"""
Carlos A Delgado S
13 de Mayo de 2023
Prueba de grafo complementario
"""
import networkx as nx
from networkx.algorithms import tournament
import matplotlib.pyplot as plt
import numpy as np
np.set_printoptions(suppress=True)

for n in range(3,100):
    G = nx.cycle_graph(n)
    G = nx.complement(G)
    #nx.draw(G, pos = nx.spring_layout(G))
    #plt.show()
    print(n, nx.euler.is_eulerian(G))


for n in [23,34,55,66]:
  G = nx.cycle_graph(n)
  G = nx.complement(G) 
  adjMattix = nx.adjacency_matrix(G).todense()
  np.savetxt("cycle+"+str(n)+".txt",adjMattix,fmt="%i")
