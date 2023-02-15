import turtle

# Set up the turtle window
window = turtle.Screen()
window.bgcolor("light blue")

# Create a turtle object and set its parameters
t = turtle.Turtle()
t.color("white")
t.pensize(3)

# Draw the snowman using 3 circles of decreasing size
radius = 80
t.penup()
t.goto(0, -radius)
t.pendown()
t.circle(radius)

radius -= 30
t.penup()
t.goto(0, -radius)
t.pendown()
t.circle(radius)

radius -= 30
t.penup()
t.goto(0, -radius)
t.pendown()
t.circle(radius)

# Draw the snowman's face
t.penup()
t.goto(20, 20)
t.pendown()
t.dot(25, "black")
t.penup()
t.goto(-20, 20)
t.pendown()
t.dot(25, "black")
t.penup()
t.goto(0, 0)
t.pendown()
t.dot(40, "orange")

# Keep the window open until it is closed manually
turtle.done()
