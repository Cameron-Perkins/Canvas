import turtle
from turtle import Screen
from queue import PriorityQueue
from queue import Queue

def recursive_turtle(q):
    
    item = q.get()
    depth = item[0]
    t = item[1]

    t1 = t.clone()
    t2 = t.clone()

    t1.right(90)
    t2.left(90)
    t1.forward(300/(2*depth))
    t2.forward(300/(2*depth))

    t1.left(90)
    t2.right(90)
    t1.forward(300/(2*depth))
    t2.forward(300/(2*depth))

    q.put((depth+1, t1))
    q.put((depth+1, t2))

    return q


T = turtle.Turtle()

T.setpos(-500, 0)

screen = turtle.Screen()

depth = 1
q = Queue()
q.put((depth, T))

for i in range(100):
    q = recursive_turtle(q)

screen.exitonclick()