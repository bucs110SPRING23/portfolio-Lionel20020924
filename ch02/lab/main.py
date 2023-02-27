import turtle

# 创建屏幕
screen = turtle.Screen()

# 设置屏幕大小和标题
screen.setup(500, 500)
screen.title("Turtle Race")

# 创建两只海龟
turtle1 = turtle.Turtle(shape="turtle")
turtle2 = turtle.Turtle(shape="turtle")

# 将海龟移动到它们的起始位置
turtle1.penup()
turtle1.goto(-100, 20)
turtle1.pendown()

turtle2.penup()
turtle2.goto(-100, -20)
turtle2.pendown()

# 让他们在屏幕上移动
for i in range(100):
    turtle1.forward(2)
    turtle2.forward(2)

# 保持窗口打开，直到手动关闭
turtle.done()

