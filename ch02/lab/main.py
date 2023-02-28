import turtle #1. import modules
import random

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
import turtle

screen = turtle.Screen()

turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()

turtle1.penup()
turtle1.goto(-100, 20)
turtle1.pendown()

turtle2.penup()
turtle2.goto(-100, -20)
turtle2.pendown()

for i in range(100):
    turtle1.forward(i)
    turtle2.forward(i)






# race 2 
# this code include both race 1 and 2  so u can pick any one and miss the other one 
import turtle
import random


screen = turtle.Screen()


turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()


turtle1.penup()
turtle1.goto(-100, 20)
turtle1.pendown()

turtle2.penup()
turtle2.goto(-100, -20)
turtle2.pendown()

# race 1 
'''
turtle1.forward(random.randrange(1, 101))
turtle2.forward(random.randrange(1, 101))
'''

for i in range(100):
    turtle1.forward(random.randrange(1, 11))
    turtle2.forward(random.randrange(1, 11))


turtle1.penup()
turtle1.goto(-100, 20)
turtle1.pendown()

turtle2.penup()
turtle2.goto(-100, -20)
turtle2.pendown()


if turtle1.xcor() > turtle2.xcor():
    print("turtle1 win！")
elif turtle2.xcor() > turtle1.xcor():
    print("turtle 2 win！")
else:
    print("same！")

turtle.done()



# PART B - complete part B here
mport pygame
import math


pygame.init()


screen_width = 800
screen_height = 600


window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("drawing")


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)


xpos = 200
ypos = 200
side_length = 100
num_sides = 5


points = []


for i in range(num_sides):
   
    angle = 360 / num_sides

    radians = math.radians(angle * i)
    
    x = xpos + side_length * math.cos(radians)
    
    y = ypos + side_length * math.sin(radians)
    
    points.append([x, y])


pygame.draw.polygon(window, white, points, 2)


pygame.draw.polygon(window, red, points)


pygame.display.flip()


pygame.time.wait(1000)


window.fill(black)
pygame.display.flip()

pygame.quit()


window.exitonclick()