#part A race 1 
import turtle
import random

# 创建屏幕
screen = turtle.Screen()

# 创建两只海龟
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()

# 将海龟移动到它们的起始位置
turtle1.penup()
turtle1.goto(-100, 20)
turtle1.pendown()

turtle2.penup()
turtle2.goto(-100, -20)
turtle2.pendown()

# 让海龟在屏幕上移动
for i in range(100):
    # 对每个海龟对象使用一次调用forward
    turtle1.forward(random.randint(1, 100))
    turtle2.forward(random.randint(1, 100))

# 将海龟重置到它们的起始位置
turtle1.penup()
turtle1.goto(-100, 20)
turtle1.pendown()

turtle2.penup()
turtle2.goto(-100, -20)
turtle2.pendown()

# 关闭窗口
screen.exitonclick()

import turtle
import random

# 创建屏幕
screen = turtle.Screen()

# 创建两只海龟
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()

# 将海龟移动到它们的起始位置
turtle1.penup()
turtle1.goto(-100, 20)
turtle1.pendown()

turtle2.penup()
turtle2.goto(-100, -20)
turtle2.pendown()

# 第一场比赛开始
for i in range(10):
    # 为每只海龟使用不同的随机值
    move1 = random.randrange(1, 11)
    move2 = random.randrange(1, 11)

    # 调用 forward() 方法移动海龟
    turtle1.forward(move1)
    turtle2.forward(move2)

# 将海龟重置到各自的起始位置
turtle1.penup()
turtle1.goto(-100, 20)
turtle1.pendown()

turtle2.penup()
turtle2.goto(-100, -20)
turtle2.pendown()

# race 2 
for i in range(10):
    # 为每只海龟使用不同的随机值
    move1 = random.randrange(1, 11)
    move2 = random.randrange(1, 11)

    # 调用 forward() 方法移动海龟
    turtle1.forward(move1)
    turtle2.forward(move2)

# 将海龟重置到各自的起始位置
turtle1.penup()
turtle1.goto(-100, 20)
turtle1.pendown()

turtle2.penup()
turtle2.goto(-100, -20)
turtle2.pendown()

# 关闭窗口
screen.exitonclick()


#part B
import pygame

# 初始化 Pygame
pygame.init()

# 设置窗口大小
size = (700, 500)
screen = pygame.display.set_mode(size)

# 设置窗口标题
pygame.display.set_caption("绘制多边形列表")

# 设置颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 定义多边形列表
shapes = [
    {"sides": 3, "color": RED},
    {"sides": 4, "color": WHITE},
    {"sides": 6, "color": BLACK},
    {"sides": 20, "color": RED},
    {"sides": 100, "color": BLACK},
    {"sides": 360, "color": WHITE}
]

# 循环绘制多边形
for shape in shapes:
    # 创建一个空的点列表
    points = []

    # 计算多边形的顶点坐标
    for i in range(shape["sides"]):
        x = 100 + 100 * shape["sides"] * (i % 5)
        y = 100 + 100 * shape["sides"] * (i // 5)
        points.append([x, y])

    # 使用 pygame.draw.polygon() 绘制多边形
    pygame.draw.polygon(screen, shape["color"], points)

    # 刷新屏幕
    pygame.display.flip()

    # 等待一段时间
    pygame.time.wait(1000)

    # 清空屏幕
    screen.fill(BLACK)

# 关闭 Pygame
pygame.quit()
