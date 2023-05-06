import numpy as np

G = np.array(
    [[0,1,0],
    [1,0,1],
    [1,0,0]]
)

print(np.matmul(G,G))
print(np.matmul(G,np.matmul(G,G)))
