import numpy as np
#输入矩阵
A = np.array([[2, 1],
              [4, 5]])
 
#求解特征值和其对应的特征向量
eigval,eigvec = np.linalg.eig(A)
for i in range(len(eigval)):
    print(f'特征值：{eigval[i]}\n对应的特征向量:\n{eigvec[i]}\n')
 