import time
from turtle import *
pensize(2)
pencolor("orange")
bgcolor("green")
fillcolor("blue")
hideturtle()
def halfPetal():
    forward(50)
    left(30)
    forward(75)
    left(30)
    forward(50)
    left(120)
def petal():
    for i in range(2):
        halfPetal()
def flower(num, i=1, depth=0):
    if i == 1:
        begin_fill()
    if num != depth:
        petal()
        left(360/num)
        flower(num,i=0,depth=depth+1)
    if i == 1:
        end_fill()
flower(12)
time.sleep(10)