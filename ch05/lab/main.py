import pygame
import math
import random

# 初始化 Pygame
pygame.init()

# 获取屏幕分辨率并创建窗口
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置飞镖盘半径和颜色
radius = min(screen_width, screen_height) // 2
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

# 绘制四色飞镖盘
for i in range(4):
    color = colors[i]
    angle1 = i * math.pi / 2
    angle2 = (i + 1) * math.pi / 2
    x1, y1 = screen_width // 2 + int(radius * math.cos(angle1)), screen_height // 2 + int(radius * math.sin(angle1))
    x2, y2 = screen_width // 2 + int(radius * math.cos(angle2)), screen_height // 2 + int(radius * math.sin(angle2))
    pygame.draw.polygon(screen, color, [(screen_width // 2, screen_height // 2), (x1, y1), (x2, y2)])

# 绘制圆形飞镖盘
pygame.draw.circle(screen, (0, 0, 0), (screen_width // 2, screen_height // 2), radius // 2, 10)

# 进入主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 生成随机落点
            x = random.randrange(screen_width)
            y = random.randrange(screen_height)
            # 绘制落点
            if math.sqrt((x - screen_width // 2) ** 2 + (y - screen_height // 2) ** 2) < radius // 2:
                pygame.draw.circle(screen, (255, 255, 0), (x, y), 2)
            else:
                pygame.draw.circle(screen, (255, 0, 0), (x, y), 2)
            # 更新屏幕显示
            pygame.display.flip()


