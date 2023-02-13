import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")        # set the window background color

tess = turtle.Turtle()
tess.color("blue")              # make tess blue
tess.pensize(9)                 # set the width of her pen
sides = input("what's the sides number")
lengths = input("give me the length u want")
sides = int(sides)
lengths = int(lengths)
total_angle = (sides - 2) * 180
angle1 = (180 - total_angle / sides)
tess.forward(lengths)
for sides in range (0,sides) :
    tess.left(angle1)
    tess.forward(lengths)
    #tess.forward(lengths)
    sides = sides + 1  
else :
    print("end")


wn.exitonclick()  