import numpy as np
import pandas as pd

# 准备数据
data = np.array([[1, -1, 4], [2, 1, 3], [1, 3, -1]])

# 使用NumPy计算协方差矩阵
covariance_matrix = np.cov(data,rowvar=True)
print("NumPy协方差矩阵：")
for i in range(3):
    for j in range(3):
        print('%.2f'%covariance_matrix[i][j],end='   ')
    print()