from turtle import *
turtle = Turtle()
turtle.speed(10)
screen = Screen()
turtle.pencolor("red")
for i in range(100): 
  turtle.circle(i*1)
  turtle.right(90) 