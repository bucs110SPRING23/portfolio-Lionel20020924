import turtle

# create screen and turtles
screen = turtle.Screen()
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()

# set starting positions
turtle1.penup()
turtle1.goto(-100, 20)
turtle1.pendown()

turtle2.penup()
turtle2.goto(-100, -20)
turtle2.pendown()

# move turtles across the screen
for i in range(150):
    turtle1.forward(5)
    turtle2.forward(5)

# exit the screen
turtle.done()

