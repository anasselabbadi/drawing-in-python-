from turtle import *
n = Turtle()
for i in range (10):
    n.left(45+i)
    n.forward(90+i)
    n.circle(45, 180)
    n.right(90+i)
    n.circle(45, 180)
    n.forward(90+i)

