from turtle import *
turtle = Turtle()
turtle.speed(100)
screen = Screen()
turtle.pencolor("red")
for i in range(100):
  turtle.circle(i*2)
  turtle.right(90)
