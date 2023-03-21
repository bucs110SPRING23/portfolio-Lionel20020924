import random
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")        # set the window background color

tess = turtle.Turtle()
tess.color("blue")              # make tess blue
tess.pensize(4)  

tess = turtle.Turtle()


screen = turtle.Screen()
screen.setup(width=600, height=600)


tess.penup()
tess.goto(0, 0)
tess.pendown()


#while True:

    coin = random.choice(['heads', 'tails'])
    if coin == 'heads':
        tess.left(90)
    else:
        tess.right(90)
    

    t.forward(50)
    
   
    x, y = t.position()
    if abs(x) > 300 or abs(y) > 300:
        break


turtle.done()
#  my pc is lovw charge , gonna finish it at night 