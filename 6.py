import numpy as np
#输入矩阵
A = np.array([[6.33, 2.50, -5.00],
[2.50, 1.00, -2.00],
[-5.00, -2.00, 4.00]])

#求解特征值和其对应的特征向量
eigval,eigvec = np.linalg.eig(A)
for i in range(len(eigval)):
    print(f'特征值：{eigval[i]}\n对应的特征向量:\n{eigvec[i]}\n')
 