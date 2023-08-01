import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

# 从txt文件中读取点云坐标
txt_path = "y0z.txt"
data = np.loadtxt(txt_path)

# 提取x和y坐标
x = data[:, 0]
y = data[:, 1]

# Delaunay三角剖分
points = np.column_stack((x, y))
tri = Delaunay(points)

# 绘制三角网格
plt.triplot(points[:, 0], points[:, 1], tri.simplices,color='blue')
#plt.plot(points[:, 0], points[:, 1], 'o')

# 设置坐标轴范围
plt.xlim(np.min(x), np.max(x))
plt.ylim(np.min(y), np.max(y))
# 隐藏坐标轴
plt.axis('off')

plt.gca().invert_yaxis()

# 显示图形
plt.show()
