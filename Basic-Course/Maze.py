from turtle import * 
turtle = Turtle()
screen = Screen()
screen.bgcolor("black")
turtle.pencolor("red")
for i in range(100):  
  turtle.forward(i*5)
  turtle.left(90)