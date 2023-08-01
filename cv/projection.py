"""
代码功能： 将3d点云投影到xyz等不同平面上
"""

import numpy as np
import mayavi.mlab as mlab


# 参数说明：
# - points：点云数据
# - flat：3d平面的参数，Ax+By+Cz+D=0，参数即为(A,B,C,D)
#         xy平面：(0 0 1 0) | xz平面：(0 1 0 0) | yz平面：(1 0 0 0)
def project_2d(points, flat):
    # 点云投影平面
    A, B, C, D = flat
    distance = A ** 2 + B ** 2 + C ** 2
    t = -(A * points[:, 0] + B * points[:, 1] + C * points[:, 2] + D) / distance
    x = A * t + points[:, 0]
    y = B * t + points[:, 1]
    z = C * t + points[:, 2]
    project_point = np.array([x, y, z]).T
    print(project_point.shape)

    # 投影展现
    mlab.figure(bgcolor=(0, 0, 0), size=(640, 640))

    # 将点坐标保存到txt文件
    data = np.column_stack((x, z))
    np.savetxt('x0z.txt', data, fmt='%f', delimiter='\t')
    # 在xy平面上的投影
    mlab.points3d(x, y, z, mode='point', colormap='spectral')

    mlab.show()


if __name__ == '__main__':
    txt_path = r"D:\code\matlab_code\david1.txt"
    points = np.loadtxt(txt_path, delimiter='\t ')
    project_2d(points, (0, 1, 0, 0))
