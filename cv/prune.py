import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
"""
输入二维点云txt文件，输出裁剪后的结果
"""
# 从txt文件中读取点云坐标
txt_path = "y0z.txt"
data = np.loadtxt(txt_path)

# 提取x和y坐标
x = data[:, 0]
y = data[:, 1]

# 执行Delaunay三角剖分
points = np.column_stack((x, y))
tri = Delaunay(points)


# 计算三角形的面积
def triangle_area(vertices):
    a, b, c = vertices
    return 0.5 * np.abs((a[0] - c[0]) * (b[1] - a[1]) - (a[0] - b[0]) * (c[1] - a[1]))


# 定义面积阈值
area_threshold = 0.3  # 面积阈值，大于该阈值的三角形将被移除

# 根据面积阈值进行修剪
triangles_to_keep = np.array([triangle_area(points[triangle]) < area_threshold for triangle in tri.simplices])
triangles = tri.simplices[triangles_to_keep]

# 绘制修剪后的三角网格
fig, ax = plt.subplots()
ax.set_aspect('equal')

# 翻转y轴坐标范围
ax.set_ylim(-2, 2)
ax.invert_yaxis()

for triangle in triangles:
    ax.fill(points[triangle, 0], points[triangle, 1], 'b')

# 添加图例
#ax.text(0.5, -0.05, f"Threshold: {area_threshold}", horizontalalignment='center', verticalalignment='top', transform=ax.transAxes)



plt.axis('off')
# 显示图形
plt.show()
