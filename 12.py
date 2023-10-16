import numpy as np
import matplotlib.pyplot as plt

# 生成正态分布数据
mean = 0
std = 1
num_samples = 100
data = np.random.normal(mean, std, num_samples)

# 绘制直方图
plt.hist(data, bins=10, density=True, alpha=0.6, color='Aquamarine', edgecolor='k')

# 绘制分布函数
plt.plot(np.sort(data), 1/(std * np.sqrt(2 * np.pi)) * np.exp( - (np.sort(data) - mean)**2 / (2 * std**2) ), color='Plum')

# 显示图像
plt.show()