import pygame
import random

# 初始化pygame
pygame.init()

# 设置屏幕尺寸
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("game")

# 设置颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 设置圆心坐标和半径
circle_center = (screen_width // 2, screen_height // 2)
circle_radius = 150

# 绘制圆形
pygame.draw.circle(screen, WHITE, circle_center, circle_radius, 5)

# 初始化分数
score_red = 0
score_blue = 0

# 定义一个变量，用于轮流投掷飞镖
player_turn = 1  # 1表示红色玩家，2表示蓝色玩家

# 游戏循环
for round in range(10):
    print(f"第{round+1}轮")

    # 如果轮到红色玩家投掷
    if player_turn == 1:
        print("red......")
        # 为飞镖落地点随机生成坐标
        dart_x = random.randrange(0, screen_width)
        dart_y = random.randrange(0, screen_height)

        # 判断飞镖是否在圆内
        if (dart_x - circle_center[0]) ** 2 + (dart_y - circle_center[1]) ** 2 < circle_radius ** 2:
            # 在圆内，红色玩家得分
            score_red += 1
            dart_color = RED
            print("got it！")
        else:
            # 不在圆内，蓝色玩家得分
            score_blue += 1
            dart_color = BLUE
            print("missed！")
        # 轮到蓝色玩家投掷
        player_turn = 2
    else:
        print("blue......")
        dart_x = random.randrange(0, screen_width)
        dart_y = random.randrange(0, screen_height)

        if (dart_x - circle_center[0]) ** 2 + (dart_y - circle_center[1]) ** 2 < circle_radius ** 2:
            score_blue += 1
            dart_color = BLUE
            print("got！")
        else:
            score_red += 1
            dart_color = RED
            print("missed！")
        player_turn = 1

    # 在屏幕上画出飞镖落地点
    pygame.draw.circle(screen, dart_color, (dart_x, dart_y), 3)

    # 刷新屏幕
    pygame.display.flip()

# 输出最终结果
print("gg")
print(f"red player：{score_red}")

