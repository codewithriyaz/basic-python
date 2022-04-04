from turtle import *
turtle = Turtle()
turtle.speed(300)
turtle.color("green")
for i in range(100):
  turtle.circle(100)
  turtle.left(i*5)