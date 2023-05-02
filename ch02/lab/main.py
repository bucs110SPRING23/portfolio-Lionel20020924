#part a 
import turtle
import random

# 创建屏幕
screen = turtle.Screen()
screen.setup(500, 500)

# 创建两只海龟
turtle1 = turtle.Turtle(shape="turtle")
turtle2 = turtle.Turtle(shape="turtle")

# 将海龟移动到起始位置
turtle1.penup()
turtle1.goto(-100, 20)
turtle1.pendown()

turtle2.penup()
turtle2.goto(-100, -20)
turtle2.pendown()

# 移动海龟并重置
for i in range(5):
    for turtle in [turtle1, turtle2]:
        turtle.forward(random.randint(1, 100))

        # 判断是否超出边界
        if turtle.xcor() > 250:
            turtle.goto(-100, turtle.ycor())

    # 等待 1 秒
    turtle.delay(1000)

# 重置海龟到起始位置
turtle1.penup()
turtle1.goto(-100, 20)
turtle1.pendown()

turtle2.penup()
turtle2.goto(-100, -20)
turtle2.pendown()

# 等待 1 秒
turtle.delay(1000)

# 关闭屏幕
turtle.done()

# race b 
import turtle
import random

# 创建屏幕
screen = turtle.Screen()
screen.setup(500, 500)

# 创建两只海龟
turtle1 = turtle.Turtle(shape="turtle")
turtle2 = turtle.Turtle(shape="turtle")

# 将海龟移动到起始位置
turtle1.penup()
turtle1.goto(-100, 20)
turtle1.pendown()

turtle2.penup()
turtle2.goto(-100, -20)
turtle2.pendown()

# 让海龟移动并重置
for i in range(5):
    # 为每个海龟调用单独的 forward() 函数，并使用不同的随机值
    turtle1.forward(random.randrange(1, 10))
    turtle2.forward(random.randrange(1, 10))

    # 判断是否超出边界
    if turtle1.xcor() > 250:
        turtle1.goto(-100, 20)

    if turtle2.xcor() > 250:
        turtle2.goto(-100, -20)

    # 等待 1 秒
    turtle.delay(1000)

# 重置海龟到起始位置
turtle1.penup()
turtle1.goto(-100, 20)
turtle1.pendown()

turtle2.penup()
turtle2.goto(-100, -20)
turtle2.pendown()

# 等待 1 秒
turtle.delay(1000)

# 关闭屏幕
turtle.done()




# PART B - complete part B here
import pygame
import math

# 初始化 Pygame
pygame.init()

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 设置屏幕尺寸
size = (700, 500)
screen = pygame.display.set_mode(size)

# 设置窗口标题
pygame.display.set_caption("绘制正多边形")

# 循环标志
done = False

# 游戏循环
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # 清屏
    screen.fill(WHITE)

    # 绘制三角形
    pygame.draw.polygon(screen, BLACK, [(100, 100), (150, 150), (50, 150)], 2)
    pygame.display.flip()

    # 绘制正方形
    pygame.draw.polygon(screen, BLACK, [(250, 100), (350, 100), (350, 200), (250, 200)], 2)

    # 绘制六边形
    x = 500
    y = 150
    radius = 50
    points = []
    for i in range(6):
        angle = math.radians(60 * i)
        x_i = x + radius * math.cos(angle)
        y_i = y + radius * math.sin(angle)
        points.append((x_i, y_i))
    pygame.draw.polygon(screen, BLACK, points, 2)
    pygame.display.flip()

    # 绘制二十边形
    x = 100
    y = 350
    radius = 50
    points = []
    for i in range(20):
        angle = math.radians(18 * i)
        x_i = x + radius * math.cos(angle)
        y_i = y + radius * math.sin(angle)
        points.append((x_i, y_i))
    pygame.draw.polygon(screen, BLACK, points, 2)
    pygame.display.flip()

    # 绘制100面形
    x = 300
    y = 350
    radius = 50
    points = []
    for i in range(100):
        angle = math.radians(3.6 * i)
        x_i = x + radius * math.cos(angle)
        y_i = y + radius * math.sin(angle)
        points.append((x_i, y_i))
    pygame.draw.polygon(screen, BLACK, points, 2)
    pygame.display.flip()

    # 绘制圆形
    pygame.draw.circle(screen, RED, (550, 350), 50, 2)

    # 刷新屏幕
    pygame.display.flip()

# 退出 Pygame
pygame.quit()
