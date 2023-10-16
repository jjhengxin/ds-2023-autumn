import numpy as np

A = np.array([[2, 1],
              [4, 5]])
x = np.ones(A.shape[0])
for k in range(20): # 幂迭代，迭代次数为10
    x = A @ x
x = x / np.linalg.norm(x)
print('Dominant eigenvector:')
print(x)
print('Dominant eigenvalue:')
lambda1 = A @ x @ x / (x @ x) # 瑞利商
print(lambda1)