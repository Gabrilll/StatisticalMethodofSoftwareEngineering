# 绘制pca降维以后的4个维度和难度指数的散点图
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('pca_of_matrix.csv')

plt.subplot(2, 2, 1)
plt.scatter(data.M1, data.difficulty_index, s=2, c='green', alpha=0.5)
plt.title("pca_M1")

plt.subplot(2, 2, 2)
plt.scatter(data.M2, data.difficulty_index, s=2, c='green', alpha=0.5)
plt.title("pca_M2")

plt.subplot(2, 2, 3)
plt.scatter(data.M3, data.difficulty_index, s=2, c='green', alpha=0.5)
plt.title("pca_M3")

plt.subplot(2, 2, 4)
plt.scatter(data.M4, data.difficulty_index, s=2, c='green', alpha=0.5)
plt.title("pca_M4")

plt.show()
