import turtle

def draw_eq_shape(turtle, num_sides, side_length):
    angle = 360.0 / num_sides
    for i in range(num_sides):
        turtle.forward(side_length)
        turtle.right(angle)

# 创建一只绿色的乌龟
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("green")

# 获取用户输入并确保输入正确的类型
num_sides = int(input("请输入多边形的边数："))
side_length = float(input("请输入多边形的边长："))

# 绘制形状
draw_eq_shape(my_turtle, num_sides, side_length)
