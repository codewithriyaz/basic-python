# Start Code Here
from turtle import *
turtle = Turtle()
def drawCircle (size,color,angle):
  turtle.left(angle)
  turtle.fillcolor(color)
  turtle.begin_fill()
  turtle.circle(size)
  turtle.end_fill()
drawCircle(100,'red',50)
drawCircle(100,'blue',80)
drawCircle(100,'green',100)
drawCircle(100,'yellow',40)
drawCircle(100,'cyan',50)
