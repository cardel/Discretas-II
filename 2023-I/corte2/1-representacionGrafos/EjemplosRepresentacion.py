"""
Ejemplos representación grafos
Carlos A Delgado
06 de Mayo de 2023
"""
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

g1 = np.array(
    [
        [0,1,0,1],
        [1,0,1,1],
        [0,1,0,0],
        [1,1,0,0]
    ]
)

G = nx.Graph(g1)
print(nx.adjacency_matrix(G).todense())


H = nx.Graph()
H.add_nodes_from(["A","B","C","D","E"])
H.add_edges_from([
    ["A","B"],
    ["B","C"],
    ["D","E"],
    ["A","A"]
])
print(nx.adjacency_matrix(H).todense())

nx.draw(G, pos=nx.spring_layout(G),)
plt.show()

opciones = {
    "width": 2,
    "node_size": 3000,
    "with_labels": True,
    "node_color": "red",
}
nx.draw(H, pos=nx.spring_layout(H),**opciones)
plt.show()


