import networkx as nx
import matplotlib.pyplot as plt


G = nx.wheel_graph(100)
print(nx.planarity.check_planarity(G)[0])


H = nx.complete_graph(5)
print(nx.planarity.check_planarity(H)[0])

