import numpy as np
from PIL import Image

# 定义图片尺寸
width = 400
height = 400

# 创建画布
img = Image.new('RGB', (width, height), color='white')
pixels = img.load()

# 随机生成几个不同颜色的点
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]
num_points = 50
points = np.random.randint(0, width, (num_points, 2))
point_colors = [colors[i % len(colors)] for i in range(num_points)]

# 绘制点
for i in range(num_points):
    x, y = points[i]
    pixels[x, y] = point_colors[i]

# 随机生成一些不同颜色的线段
num_lines = 50
line_colors = [colors[i % len(colors)] for i in range(num_lines)]
lines = np.random.randint(0, width, (num_lines, 2, 2))

# 绘制线段
for i in range(num_lines):
    x1, y1 = lines[i][0]
    x2, y2 = lines[i][1]
    for t in np.linspace(0, 1, 100):
        x = int(x1 + t * (x2 - x1))
        y = int(y1 + t * (y2 - y1))
        pixels[x, y] = line_colors[i]

# 保存图片
img.save('abstract_art.png')
