import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import time

G = nx.watts_strogatz_graph(100,3,0.5)
MR = nx.adjacency_matrix(G).todense()
print(MR)

def mult_matrices(G,H):
    R = np.zeros((G.shape[0],G.shape[1]))
    for i in range(G.shape[0]):
        for j in range(G.shape[1]):
            suma = 0
            for k in range(G.shape[0]):
                suma += G[i,k]*H[k,j]
            R[i,j] = suma
    return R
          

def aplicar_disyuncion(G,H):
    R = np.zeros((G.shape[0],G.shape[1]))
    for i in range(G.shape[0]):
        for j in range(G.shape[1]):
            R[i,j] = G[i,j] or H[i,j]

    return R


def matriz_conectividad(G):
    M = G
    C = G
    for k in range(G.shape[0]):
        M = mult_matrices(M,G)
        C = aplicar_disyuncion(C,M)

    return C

t1 = time.time()
Mat1=matriz_conectividad(MR)
tiempo1 = time.time()-t1

def warshall_algoritmo(MR):
    W = MR
    for k in range(MR.shape[0]):
      Want = W.copy()
      for i in range(MR.shape[0]):
          for j in range(MR.shape[1]):
               W[i,j] = Want[i,j] or (Want[i,k] and Want[k,j])

    return W

t2 = time.time()
Mat2 = warshall_algoritmo(MR)
tiempo2 = time.time()-t2

print(tiempo1,tiempo2)
