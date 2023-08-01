import matplotlib.pyplot as plt
from PIL import Image
"""
对侧视图的三角网格阈值图做旋转并添加图例
"""
# 加载图片
image_path = "image_0.3.png"
image = Image.open(image_path)

# 旋转图片
rotated_image = image.rotate(-90)

# 创建图形和坐标轴
fig, ax = plt.subplots()

# 显示旋转后的图片
ax.imshow(rotated_image)

# 添加图例
legend_text = "Threshold:0.3"
ax.text(0.5, 1.1, legend_text, horizontalalignment='center', verticalalignment='bottom', transform=ax.transAxes)

# 隐藏坐标轴
ax.axis('off')

# 展示图形
plt.show()
