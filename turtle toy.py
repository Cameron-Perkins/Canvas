import turtle
from turtle import Screen
import random
import sys


def recursive_turtle(t,depth,a):
    print(depth)
    if depth == 0:
        return
    t1 = t.clone()
    t2 = t.clone()
    
    t1.color(random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
    t2.color(random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))

    t1.setheading(0)
    t1.forward(100)
    t1.setheading(270)
    t1.forward(100)


    t2.setheading(180)
    t2.forward(100)
    t2.setheading(270)
    t2.forward(100)

    recursive_turtle(t1, depth-1, a+2)
    recursive_turtle(t2, depth-1, a+2)


t = turtle.Turtle()

screen = turtle.Screen()

t.setpos(0, screen.window_width() / 2)
random.setstate(random.getstate())

t.color('#000000')
t.pensize(3)

turtle.colormode(255)
R = random.randrange(0, 256)
B = random.randrange(0, 256)
G = random.randrange(0, 256)

t.color(R, B, G)
recursive_turtle(t,10,a=1)

turtle.done()